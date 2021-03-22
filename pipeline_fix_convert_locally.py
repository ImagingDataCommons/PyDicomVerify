import json
import logging
import logging.config
import os
import re
import psutil
import pydicom
import shutil
import time
import common.common_tools as ctools
import conversion as conv
from collections.abc import Callable
from multiprocessing import freeze_support
from common.parallelization import (
    # CLASSES
    Periodic,
    ProcessPool,
    TryAfterTimeout,
    # FUNCTIONS
    install_mp_handler,
    # VARIABLES
    MAX_NUMBER_OF_THREADS,
)
from datetime import (
    # CLASSES
    datetime,
    timedelta,
)
from dicom_fix_issue_info import (
    # CLASSES
    DataInfo,
    Datalet,
    DicomFileInfo,
    FixCollection,
    IssueCollection,
    PerformanceMeasure,
    ProcessPerformance,
    table_quota,
    organize_dcmvfy_errors,
)
from gcloud.BigQueryStuff import (
    # FUNCTIONS
    create_all_tables,
    create_bq_dataset,
    query_string,
    query_string_with_result,
    delete_table,
    schema_fix,
    schema_issue,
    schema_defective,
    schema_originated_from,
    stream_insert_with_ids,
)
from gcloud.DicomStoreStuff import (
    # FUNCTIONS
    recreate_dicom_store,
    exists_dataset,
    exists_dicom_store,
    export_dicom_instance_bigquery,
    import_dicom_bucket,
)
from gcloud.StorageBucketStuff import (
    # FUNCTIONS
    create_bucket,
    download_blob,
    upload_blob,
    list_blobs,
    delete_bucket,
    exists_bucket,
    delete_blob,
    get_blob,
)
from highdicom.legacy.sop import (
    # CLASSES
    FrameSetCollection,
)
from pydicom.uid import (
    # FUNCTIONS
    generate_uid,
)
from pydicom.charset import python_encoding
from rightdicom.dcmfix.study_dependent_patches import *
from rightdicom.dcmfix.anatomy import *
from rightdicom.dcmfix.fix_all import (
    # FUNCTIONS
    fix_dicom,
)
from typing import (
    # VARIABLES
    List,
    Tuple,
)
from multiprocessing import Manager
from anatomy_query import (
    # FUNCTIONS
    get_anatomy_info,
    query_anatomy_from_tables,
    fix_SOPReferencedMacro,
)
from ref_query import QueryReferencedStudySequence
# ---------------- Global Vars --------------------------:
max_number_of_study_processes = 1
max_number_of_fix_processes = MAX_NUMBER_OF_THREADS
max_number_of_up_down_load_processes = MAX_NUMBER_OF_THREADS
max_number_of_bq_processes = MAX_NUMBER_OF_THREADS
max_number_of_frameset_processes = MAX_NUMBER_OF_THREADS
max_number_of_conversion_processes = MAX_NUMBER_OF_THREADS
ref_info = {}
fix_report_tq = None
issue_report_tq = None
org_report_tq = None
defect_report_tq = None
processes_to_monitor = []
flaw_query_form = '''(
        "{}",-- COLLECTION_NAME
        "{}",-- STUDY_INSTANCE_UID
        "{}",-- SERIES_INSTANCE_UID
        "{}",-- SOP_INSTANCE_UID
        "{}"-- FLAW
            )
            '''
# Logger setup --------------------------------------------------------
current_folder = os.path.dirname(__file__)
def namer(name=''):

    if name == '':
        dt_string = datetime.now().strftime("[%d-%m-%Y]")
        file_name = './Logs/{}.log'.format(dt_string)
    else:
        dt_string = datetime.now().strftime("[%d-%m-%Y][%H-%M-%S.%f]")
        base = os.path.basename(name)
        dir_ = os.path.dirname(name)
        prev_file_name = re.sub(r'\.log.*', '', base)
        file_name = os.path.join(
            dir_, '{}_ended_at_{}.log'.format(prev_file_name, dt_string))
    return file_name


file_name = namer()
folder = os.path.dirname(file_name)
if not os.path.exists(folder):
    os.makedirs(folder)
with open(os.path.join(current_folder, 'log_config.json')) as json_file:
    logger_config_dict = json.load(json_file)
logger_config_dict["handlers"]['file']['filename'] = file_name
logger_config_dict["root"]["handlers"].append("console")
logging.config.dictConfig(logger_config_dict)
hs = logging.RootLogger.root.handlers
for h in hs:
    if h.name == 'file':
        h.namer = namer
# install_mp_handler()
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.CRITICAL)
# -----------------------------------------------------------------------


def VER(file: str, log: list, char_set: str = 'ascii'):
    file_name = os.path.basename(file)
    if file_name.endswith('.dcm'):
        file_name = file_name[:-4]
    dcm_verify = "/Users/afshin/Documents/softwares"\
        "/dicom3tools/most_recent_exe/dciodvfy"
    if not os.path.exists(dcm_verify):
        dcm_verify = shutil.which('dciodvfy')
        if dcm_verify is None:
            print("Error: install dciodvfy into system path")
            assert(False)
    err_log = []
    ctools.RunExe([dcm_verify, '-filename', file], '', '', errlog=err_log,
                  char_encoding=char_set)
    organize_dcmvfy_errors(err_log, log)
    # my_code_output = verify_dicom(file, False, '')


def FixFile(dicom_file: str, dicom_fixed_file: str,
            log_fix: list, log_david_pre: list, log_david_post: list,
            anatomy: tuple):
    ds = pydicom.read_file(dicom_file)
    char_set = DicomFileInfo.get_charset_val_from_dataset(ds)
    # log_mine = []
    VER(dicom_file, log_david_pre, char_set=char_set)
    if len(anatomy) == 2:
        add_anatomy(ds, anatomy[0], anatomy[1], log_fix)
    fix_SOPReferencedMacro(ds, log_fix, ref_info)
    fix_dicom(ds, log_fix)
    # fix_report = PrintLog(log_fix)
    pydicom.write_file(dicom_fixed_file, ds)
    VER(dicom_fixed_file, log_david_post, char_set=char_set)
    return ds


def BuildQueries1(table_q_info: table_quota, qs: list, dataset_id: str,
                 return_: bool = True, processes: ProcessPool=None) -> list:
    logger = logging.getLogger(__name__)
    out_q = []
    row_limit = 500
    elem_q = []
    n = 0
    rn = 0
    for q in qs:
        rn += 1
        if rn < row_limit:
            elem_q.append(q)
        else:
            # if n > 0:
            #     header = header_ptrn.format(table_q_info.get_table(), '{}')
            n += 1
            out_q.append(elem_q)
            elem_q = [q]  # for the next round
            rn = 0
            if processes is None:
                stream_insert_with_ids(
                    table_q_info.table_base_id, out_q[-1], table_q_info.schema)
            else:
                # logger.info('putting in queue')
                processes.queue.put(
                    (
                        stream_insert_with_ids,
                        (
                            table_q_info.table_base_id,
                            out_q[-1], table_q_info.schema)
                    )
                )
    out_q.append(elem_q)
    if processes is None:
        stream_insert_with_ids(
            table_q_info.table_base_id, out_q[-1], table_q_info.schema)
    else:
        # logger.info('putting in queue')
        processes.queue.put(
            (
                stream_insert_with_ids,
                (table_q_info.table_base_id, out_q[-1], table_q_info.schema)
            )
        )
    if return_:
        return out_q
    else:
        return []


def BuildQueries(table_q_info: table_quota, qs: list, dataset_id: str,
                 return_: bool = True, processes: ProcessPool=None) -> list:
    logger = logging.getLogger(__name__)
    # m = re.search("\.(.*)\n", header)
    # if m is not None:
    #     table_name = m.group(1)
    # else:
    #     table_name = ''
    out_q = []
    ch_limit = 1024 * 1000
    row_limit = 1000
    elem_q = ''
    n = 0
    rn = 0
    header_ptrn = """
        INSERT INTO {0}
        VALUES {1}
        """
    header = header_ptrn.format(table_q_info.get_table(), '{}')
    for q in qs:
        if isinstance(q, tuple):
            q = q[0]
        rn += 1
        if len(elem_q) + len(q) + len(header) < ch_limit and rn < row_limit:
            elem_q = q if elem_q == '' else '{},{}'.format(q, elem_q)
        else:
            if n > 0:
                header = header_ptrn.format(table_q_info.get_table(), '{}')
            n += 1
            out_q.append(header.format(elem_q))
            elem_q = q  # for the next round
            rn = 0
            if processes is None:
                query_string(out_q[-1], '', project_id='idc-tcia')
            else:
                # logger.info('putting in queue')
                processes.queue.put(
                    (
                        query_string,
                        (out_q[-1], '', True, 'idc-tcia')
                    )
                )
    header = header_ptrn.format(table_q_info.get_table(), '{}')
    out_q.append(header.format(elem_q))
    if processes is None:
        query_string(out_q[-1], '', project_id='idc-tcia')
    else:
        # logger.info('putting in queue')
        processes.queue.put(
                    (
                        query_string,
                        (out_q[-1], '', True, 'idc-tcia')
                    )
                )
    if return_:
        return out_q
    else:
        return []


def fix_one_instance(org_file_path: str,
                     fx_file_path: str,
                     input_table_name: str,
                     fixed_table_name: str,
                     anatomy: tuple,
                     org_bucket_name = '',
                     org_series_uid: str = '',
                     org_study_uid: str = '') -> tuple:
    logger = logging.getLogger(__name__)
    fix_log = []
    pre_fix_issues = []
    post_fix_issues = []
    curr_study_uid = org_study_uid
    curr_series_uid = org_series_uid
    curr_instance_uid = ''
    try:
        fx_ds = FixFile(
            org_file_path, fx_file_path, fix_log,
            pre_fix_issues,
            post_fix_issues, anatomy)
        curr_study_uid = fx_ds.StudyInstanceUID
        curr_series_uid = fx_ds.SeriesInstanceUID
        curr_instance_uid = fx_ds.SOPInstanceUID
        # as a trick to workaround pickling problem
        fx_dicom_ds = fx_ds
    except BaseException as err:
        msg = str(err)
        msg += '\n{}'.format(org_file_path)
        logger.error(msg, exc_info=True)
        return([], [], [], flaw_query_form.format(
            org_bucket_name, curr_study_uid,
            curr_series_uid, curr_instance_uid, 'FIX'),
            curr_instance_uid, curr_series_uid, curr_study_uid)
    fixes_all = FixCollection(
        fix_log, curr_study_uid,
        curr_series_uid, curr_instance_uid)
    fix_queries = fixes_all.GetQuery()
    pre_issues = IssueCollection(
        pre_fix_issues,
        input_table_name,
        curr_study_uid,
        curr_series_uid,
        curr_instance_uid)
    issue_queries = pre_issues.GetQuery()
    post_issues = IssueCollection(
        post_fix_issues,
        fixed_table_name,
        curr_study_uid,
        curr_series_uid,
        curr_instance_uid)
    issue_queries.extend(post_issues.GetQuery())
    fixed_input_relation = conv.ParentChildDicoms(
        [pre_issues.SOPInstanceUID],
        post_issues.StudyInstanceUID,
        post_issues.SeriesInstanceUID,
        post_issues.SOPInstanceUID,
        fx_file_path)
    origin_queries = fixed_input_relation.GetQuery(
        input_table_name,
        fixed_table_name)
    return(fix_queries, issue_queries, origin_queries, '',
    curr_instance_uid, curr_series_uid, curr_study_uid)


def frameset_for_one_series(single_frame_file_path: List[str],
                            series_folder_prifix: str,
                            single_frame_series_uid: str):
    logger = logging.getLogger(__name__)
    # All frames set created out of one series must have the same series
    #   instance uid. So I have to create on sereies instance uid and a
    #   destination folder for future multiframe images
    # ------------------------------------------------
    multi_frame_series_uid = generate_uid(
        prefix="1.3.6.1.4.1.43046.3" + ".1.9.",
        entropy_srcs=[single_frame_series_uid])
    multi_frame_series_folder = os.path.join(
        series_folder_prifix,
        multi_frame_series_uid)
    if not os.path.exists(multi_frame_series_folder):
        os.makedirs(multi_frame_series_folder)
    ds_list = []
    for f_bl in single_frame_file_path:
        ds_list.append(pydicom.read_file(f_bl))
    try:
        fs_collection = FrameSetCollection(ds_list)
        fs = fs_collection.FrameSets
    except BaseException as err:
        msg = str(err)
        msg += '\n The first sample out of {}:\n{}'.format(
            len(single_frame_file_path), str(single_frame_file_path[0]))
        logger.error(msg, exc_info=True)
        fs = []
    return(fs, multi_frame_series_uid, multi_frame_series_folder)


def get_rows_and_insert_ids(q_list: list, insert_id_start: int):
    if len(q_list) == 0:
        return [], [], insert_id_start
    rows = []
    ids = list(range(insert_id_start, insert_id_start + len(q_list)))
    insert_id_start += len(ids)
    for q_elem in q_list:
        rows.append(q_elem[1])
    return (rows, ids, insert_id_start)


def fix_convert_one_sereis(
        original_files: list,
        fx_local_series_path: str,
        mf_local_study_path: str,
        fx_gc_info, mf_gc_info, anatomy: tuple,
        in_bgq_table_name: str,
        in_collection_name: str = '',
        in_instance_uid: list = [],
        in_series_uid: str = '',
        in_study_uid: str = '',
       ):
    logger = logging.getLogger(__name__)
    try:
        fix_convert_one_sereis.counter += 1
    except AttributeError:
        fix_convert_one_sereis.counter = 1
    
    if len(original_files) == 0:
        logger.debug('The input is empty')
        return([], [], [], [], 0, 0)
    current_pid = os.getpid()
    insert_id = int('1{:05d}{:04d}00000'.format(
        current_pid,fix_convert_one_sereis.counter)
        )
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    single_frames = []
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    blob_address_form = '{}/dicom/{}/{}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject,
        in_study_uid,
        in_series_uid)
    defective_study_series = []
    fixed_files_size = 0
    mf_files_size = 0
    upload_time_for_one_instance = 300
    if not os.path.exists(fx_local_series_path):
        os.makedirs(fx_local_series_path)
    if not os.path.exists(mf_local_study_path):
        os.makedirs(mf_local_study_path)

    
    for i, obj in enumerate(original_files):
        if i < len(in_instance_uid):
            fbase = in_instance_uid[i]
        else:
            fbase = os.path.basename(obj)
        fx_file_path = os.path.join(fx_local_series_path, fbase + '.dcm')
        (fix_q, iss_q, org_q, flaw,
        fx_instance_uid, fx_series_uid,
        fx_study_uid) = fix_one_instance(
            obj,
            fx_file_path,
            in_bgq_table_name, fx_table_name, anatomy,
            in_collection_name, in_series_uid, in_study_uid)
        
        bgq_db_id = fx_gc_info.BigQuery.GetBigQueryStyleDatasetAddress(False)
        fix_report_table_id = '{}.{}'.format(bgq_db_id, 'FIX_REPORT')
        issue_report_table_id = '{}.{}'.format(bgq_db_id, 'ISSUE')
        orig_report_table_id = '{}.{}'.format(bgq_db_id, 'ORIGINATED_FROM')
        if flaw == '':
            fix_queries.extend(fix_q)
            issue_queries.extend(iss_q)
            origin_queries.extend(org_q)
            single_frames.append(fx_file_path)
            blob_address = blob_address_form.format(in_instance_uid[i])
            logger.debug(
                'Start uploading the fixed file {}'.format(fx_file_path))
            # success = upload_blob(
            #     fx_gc_info.Bucket.ProjectID,
            #     fx_gc_info.Bucket.Dataset,
            #     blob_address,
            #     fx_file_path)
            upload_process = TryAfterTimeout(
                upload_blob,
                (
                    fx_gc_info.Bucket.ProjectID,
                    fx_gc_info.Bucket.Dataset,
                    blob_address,
                    fx_file_path
                ),
                timeout_in_sec=upload_time_for_one_instance,
                max_trial=5
            )
            outs = upload_process.start()
            if not outs:
                success = False
            else:
                success = outs[0]
            if not success:
                flaw_queries.append(flaw_query_form.format(
                    fx_gc_info.Bucket.Dataset, in_study_uid,
                    in_series_uid, in_instance_uid[i],
                    'UPLOAD')
                )
            
        else:
            flaw_queries.append(flaw)
            defective_study_series.append(
                (fx_study_uid, fx_series_uid))
    # The code is not gonna proceed to conversion if there is any fix issue
    if len(flaw_queries) != 0:
        # rm((in_local_series_path, fx_local_series_path), False)
        return([], [], [], flaw_queries, 0, 0)
    # Now I want to extract framesets from fixed sereis:
    
    (fsets, mf_series_uid, mf_series_dir) = frameset_for_one_series(
        single_frames,
        mf_local_study_path,
        fx_series_uid)
    logger.debug('Start conversion process for {} frameset'.format(len(fsets)))
    number_of_all_converted_mf = 0
    if len(fsets) == 0:
        for fx_file_path in single_frames:
            f_query = flaw_query_form.format(
                in_collection_name, fx_study_uid,
                fx_series_uid, fx_instance_uid, 'FRAMESET')
            flaw_queries.append(f_query)
    else:
        mf_study_uid = fx_study_uid
        char_set = DicomFileInfo.get_charset_val_from_dataset(single_frames[0])
        for fset in fsets:
            frameset_sop_uids = fset.GetSOPInstanceUIDList()
            frameset_sop_uids.sort()
            mf_instace_uid = generate_uid(
                prefix="1.3.6.1.4.1.43046.3" + ".1.9.",
                entropy_srcs=frameset_sop_uids
            )
            mf_file_path = os.path.join(
                mf_series_dir, '{}.dcm'.format(mf_instace_uid))
            pr_ch = conv.ConvertFrameset(
                fset,
                mf_file_path,
                mf_study_uid,
                mf_series_uid,
                mf_instace_uid)
            if pr_ch is None:
                for fr in fset.Frames:
                    st_id = fr.StudyInstanceUID
                    se_id = fr.SeriesInstanceUID
                    sop_id = fr.SOPInstanceUID
                f_query = flaw_query_form.format(
                    in_collection_name,
                    st_id, se_id, sop_id, 'CONVERSION')
                flaw_queries.append(f_query)
            else:
                mf_files_size += os.path.getsize(pr_ch.child_dicom_file)
                number_of_all_converted_mf += 1
                org_q = pr_ch.GetQuery(fx_table_name, mf_table_name)
                origin_queries.extend(org_q)
                multiframe_log = []
                VER(pr_ch.child_dicom_file, multiframe_log, char_set=char_set)
                mf_issues = IssueCollection(
                    multiframe_log, mf_table_name,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_sop_instance_uid, )
                q_iss = mf_issues.GetQuery()
                issue_queries.extend(q_iss)
                mf_blob_path = '{}/dicom/{}/{}/{}.dcm'.format(
                        mf_gc_info.Bucket.DataObject,
                        pr_ch.child_study_instance_uid,
                        pr_ch.child_series_instance_uid,
                        pr_ch.child_sop_instance_uid)
                # success = upload_blob(
                #     mf_gc_info.Bucket.ProjectID,
                #     mf_gc_info.Bucket.Dataset,
                #     mf_blob_path, pr_ch.child_dicom_file)
                upload_process = TryAfterTimeout(
                    upload_blob,
                    (
                        mf_gc_info.Bucket.ProjectID,
                        mf_gc_info.Bucket.Dataset,
                        mf_blob_path, pr_ch.child_dicom_file
                    ),
                    timeout_in_sec=upload_time_for_one_instance * len(single_frames),
                    max_trial=5
                )
                outs = upload_process.start()
                if not outs:
                    success = False
                else:
                    success = outs[0]
                if not success:
                    flaw_queries.append(flaw_query_form.format(
                        mf_gc_info.Bucket.Dataset, pr_ch.study_uid,
                        pr_ch.series_uid, pr_ch.instance_uid,
                        'UPLOAD'))
    # Now I can remove the series:
    rm((fx_local_series_path, mf_series_dir), True)
    logging.info('fixed = {}, converted = {} orig = {}'.format(
        len(original_files),
        number_of_all_converted_mf,
        len(origin_queries)))
    return(fix_queries, issue_queries, origin_queries, flaw_queries,
            len(fsets), number_of_all_converted_mf)


def get_status_str(header, used, free, total):
    u = ctools.get_human_readable_string(used)
    f = ctools.get_human_readable_string(free)
    t = ctools.get_human_readable_string(total)
    tt = 1 if total == 0 else total
    return '{} -> used:{}({:.1%}) free: {}({:.1%}) total:{}'.format(
        header, u, used/tt, f, free/tt, t)


def log_status():
    logger = logging.getLogger(__name__)
    vr = psutil.virtual_memory()
    if isinstance(processes_to_monitor, ProcessPool):
        logger.info(processes_to_monitor.get_status())
    status = get_status_str('RAM', vr.used, vr.free, vr.total)
    logger.info(status)
    hdd = psutil.disk_usage('/')
    status = get_status_str('HardDisk', hdd.used, hdd.free, hdd.total)
    logger.info(status)

def rm(folders, log: bool = True):
    # print(folders)
    if type(folders) == str:
        folders = (folders, )
    for a in folders:
        if os.path.exists(a):
            if log:
                logging.info(' XXX -> REMOVING FOLDER {}'.format(a))
            shutil.rmtree(a)
        else:
            if log:
                logging.info("FOLDER {} DOESN'T EXIST TO BE ROMOVED".format(a))

def partition_series(series_dict: dict, from_the_last: int):
    fist_part = {}
    second_part = {}
    l = len(series_dict)
    for i, (key, val) in enumerate(series_dict.items(), 0):
        if i < (l - from_the_last):
            fist_part[key] = val
        else:
            second_part[key] = val
    return(fist_part, second_part)


def create_datainfos(dataset_name: str = 'test_dataset00') -> tuple:
    fx = DataInfo(
        Datalet('idc-tcia',      # Bucket
                'us',
                dataset_name,
                'FIXED'),
        Datalet('idc-tcia',      # Dicom Store
                'us',
                dataset_name,
                'FIXED'),
        Datalet('idc-tcia',      # Bigquery
                'us',
                dataset_name,
                'FIXED')
        )
    mf = DataInfo(
        Datalet('idc-tcia',      # Bucket
                'us',
                dataset_name,
                'MULTIFRAME'),
        Datalet('idc-tcia',      # Dicom Store
                'us',
                dataset_name,
                'MULTIFRAME'),
        Datalet('idc-tcia',      # Bigquery
                'us',
                dataset_name,
                'MULTIFRAME')
        )
    return (fx, mf)


def create_bucket_tables(dataset_name: str):
    logger = logging.getLogger(__name__)
    fx_dicoms, mf_dicoms = create_datainfos(dataset_name)
    print('creating all tables')
    create_all_tables('{}.{}'.format(
        fx_dicoms.BigQuery.ProjectID, fx_dicoms.BigQuery.Dataset),
        fx_dicoms.BigQuery.CloudRegion, True, 
        project_id=fx_dicoms.BigQuery.ProjectID)
    print('creating all fx_bucket')
    if not exists_bucket(fx_dicoms.Bucket.ProjectID, fx_dicoms.Bucket.Dataset):
        create_bucket(
            fx_dicoms.Bucket.ProjectID,
            fx_dicoms.Bucket.Dataset,
            False)
    else:
        logger.warning(
            'The bucket {} already exists. Possible occurence of mix-up'.format(
                fx_dicoms.Bucket.Dataset))
    print('creating all mf_bucket')
    if not exists_bucket(mf_dicoms.Bucket.ProjectID, mf_dicoms.Bucket.Dataset):
        create_bucket(
            mf_dicoms.Bucket.ProjectID,
            mf_dicoms.Bucket.Dataset,
            False)
    else:
        logger.warning(
            'The bucket {} already exists. Possible occurence of mix-up'.format(
                mf_dicoms.Bucket.Dataset))


def create_dicomstores(dataset_name: str):
    fx_dicoms, mf_dicoms = create_datainfos(dataset_name)
    # --> recreated dicomstores
    recreate_dicom_store(
        fx_dicoms.DicomStore.ProjectID,
        fx_dicoms.DicomStore.CloudRegion,
        fx_dicoms.DicomStore.Dataset,
        fx_dicoms.DicomStore.DataObject)
    recreate_dicom_store(
        mf_dicoms.DicomStore.ProjectID,
        mf_dicoms.DicomStore.CloudRegion,
        mf_dicoms.DicomStore.Dataset,
        mf_dicoms.DicomStore.DataObject)
    delete_table(
        fx_dicoms.BigQuery.ProjectID,
        fx_dicoms.BigQuery.Dataset,
        fx_dicoms.BigQuery.DataObject)
    delete_table(
        mf_dicoms.BigQuery.ProjectID,
        mf_dicoms.BigQuery.Dataset,
        mf_dicoms.BigQuery.DataObject)
    
    # --> import/export dicom data
    import_dicom_bucket(
        fx_dicoms.DicomStore.ProjectID,
        fx_dicoms.DicomStore.CloudRegion,
        fx_dicoms.DicomStore.Dataset,
        fx_dicoms.DicomStore.DataObject,
        fx_dicoms.Bucket.ProjectID,
        fx_dicoms.Bucket.Dataset,
        fx_dicoms.Bucket.DataObject)
    import_dicom_bucket(
        mf_dicoms.DicomStore.ProjectID,
        mf_dicoms.DicomStore.CloudRegion,
        mf_dicoms.DicomStore.Dataset,
        mf_dicoms.DicomStore.DataObject,
        mf_dicoms.Bucket.ProjectID,
        mf_dicoms.Bucket.Dataset,
        mf_dicoms.Bucket.DataObject)
    export_dicom_instance_bigquery(
        fx_dicoms.DicomStore.ProjectID,
        fx_dicoms.DicomStore.CloudRegion,
        fx_dicoms.DicomStore.Dataset,
        fx_dicoms.DicomStore.DataObject,
        fx_dicoms.BigQuery.ProjectID,
        fx_dicoms.BigQuery.Dataset,
        fx_dicoms.BigQuery.DataObject)
    export_dicom_instance_bigquery(
        mf_dicoms.DicomStore.ProjectID,
        mf_dicoms.DicomStore.CloudRegion,
        mf_dicoms.DicomStore.Dataset,
        mf_dicoms.DicomStore.DataObject,
        mf_dicoms.BigQuery.ProjectID,
        mf_dicoms.BigQuery.Dataset,
        mf_dicoms.BigQuery.DataObject)


def fix_convert_all(dataset_name, 
         series_list: list,
         input_table_name: str,
         in_local_series_paths: list,
         local_data_path: str
         ):

    fx_dicoms, mf_dicoms = create_datainfos(dataset_name)
    db_dataset_address =\
        fx_dicoms.BigQuery.GetBigQueryStyleDatasetAddress(False)

    fix_report_tq = table_quota(
        1500, '{}.{}'.format(
            db_dataset_address, 'FIX_REPORT'), schema_fix)
    issue_report_tq = table_quota(
        1500, '{}.{}'.format(
            db_dataset_address, 'ISSUE'), schema_issue)
    org_report_tq = table_quota(
        1500, '{}.{}'.format(
            db_dataset_address, 'ORIGINATED_FROM'),
        schema_originated_from)
    defect_report_tq = table_quota(
        1500, '{}.{}'.format(
            db_dataset_address, 'DEFECTIVE'),
        schema_originated_from)

    fix_queries = []
    issue_queries = []
    origin_queries = []
    flaw_queries = []
    frameset_number = 0
    multiframe_number = 0
    
    fx_local_study_path = os.path.join(local_data_path, fx_dicoms.Bucket.DataObject)
    mf_local_study_path = os.path.join(local_data_path, mf_dicoms.Bucket.DataObject)
    if os.path.exists(fx_local_study_path):
        rm(fx_local_study_path)
    if os.path.exists(mf_local_study_path):
        rm(mf_local_study_path)
    for series_info, series_path in zip(series_list, in_local_series_paths):
        files = [os.path.join(series_path, i) for i in os.listdir(
            series_path) if i.endswith('.dcm')]
        fx_series_folder = '{}/dicom/{}/{}'.format(
            fx_local_study_path,
            series_info['StudyInstanceUID'],
            series_info['SeriesInstanceUID']
            )
        mf_study_folder = '{}/dicom/{}'.format(
            mf_local_study_path,
            series_info['StudyInstanceUID'],
            )
        # I am using a single process to avoid running down on RAM
        # processes = ProcessPool(1, 'single_proce')
        # processes.queue.put((
        #     fix_convert_one_sereis,
        #     (
        #         files,
        #         fx_series_folder,
        #         mf_study_folder,
        #         fx_dicoms, mf_dicoms, {}, input_table_name,
        #         series_info['COLLECTION_ID'],
        #         series_info['INSTANCES'],
        #         series_info['SeriesInstanceUID'],
        #         series_info['StudyInstanceUID']),
        # ))
        # processes.queue.join()
        # processes.kill_them_all(60 * 5)
        # argus, outs = processes.output[0]

        # outs = fix_convert_one_sereis(
        #     files,
        #     fx_series_folder,
        #     mf_study_folder,
        #     fx_dicoms, mf_dicoms, {}, input_table_name,
        #     series_info['COLLECTION_ID'],
        #     series_info['INSTANCES'],
        #     series_info['SeriesInstanceUID'],
        #     series_info['StudyInstanceUID'])


        my_process = TryAfterTimeout(
            fix_convert_one_sereis,
            (
                files,
                fx_series_folder,
                mf_study_folder,
                fx_dicoms, mf_dicoms, {}, input_table_name,
                series_info['COLLECTION_ID'],
                series_info['INSTANCES'],
                series_info['SeriesInstanceUID'],
                series_info['StudyInstanceUID']),
            timeout_in_sec=3600,
            max_trial=1
        )
        outs = my_process.start()
        fq, isq, orq, flq, fs, ms = outs[0]
        fix_queries.extend(fq)
        issue_queries.extend(isq)
        origin_queries.extend(orq)
        flaw_queries.extend(flq)
        frameset_number += fs
        multiframe_number += ms
    dataset_id = '{}.{}'.format(
        fx_dicoms.BigQuery.ProjectID,
        fx_dicoms.BigQuery.Dataset)
    if len(fix_queries) != 0:
        BuildQueries1(
            fix_report_tq,
            fix_queries,
            dataset_id, False)
    if len(issue_queries) != 0:
        BuildQueries1(
            issue_report_tq,
            issue_queries,
            dataset_id, False)
    if len(origin_queries) != 0:
        BuildQueries1(
            org_report_tq,
            origin_queries,
            dataset_id, False)

    if len(flaw_queries) != 0:
        BuildQueries(
            org_report_tq,
            flaw_queries,
            dataset_id, False)
    
    # Wait unitl populating bigquery stops
    
def main_fix_multiframe_convert(
        json_file: str,
        series_folders: list,
        input_table_name: str,
        result_bucket_name: str,
        local_data_path: str
        ):
    with open(json_file) as jfile:
        jcontent = json.load(jfile)
    series = jcontent['data']
    status_logger = Periodic(log_status, None, 60)
    status_logger.start()
    try:
        
        
        fix_convert_all(
            result_bucket_name, 
            series,
            input_table_name,
            series_folders,
            local_data_path
        )
        status_logger.kill_timer()

    finally:
        status_logger.kill_timer()

# if __name__ == '__main__':
#     freeze_support()
#     j_file_name =  'gitexcluded_local/0001.json'
#     with open(j_file_name) as jfile:
#         jcontent = json.load(jfile)
#     series = jcontent['data']
#     result_bucket_name = 'afshin_terra_test00'
#     input_table_name = 'canceridc-data.idc_views.dicom_all'
#     local_study_path = 'gitexcluded_data_res'
#     folders = []
#     for se in series:
#         folders.append(os.path.dirname(se['SERIES_PATH'][0]))
#     create_bucket_tables(result_bucket_name)
#     main_fix_multiframe_convert(
#         j_file_name, folders, input_table_name, result_bucket_name,
#         local_study_path
#         )
    # ctools.RunExe([
    #     'gsutil' ,'cp', '-r', local_study_path + '/*', #os.path.join(fx_local_study_path, 'dicom'), 
    #     'gs://{}'.format(result_bucket_name)],
    #     log_std_out=True, log_std_err=True)
    # create_dicomstores(result_bucket_name)