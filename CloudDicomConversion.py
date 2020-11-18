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
from common.parallelization import (
    # CLASSES
    Periodic,
    ProcessPool,
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
    stream_insert,
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
    quey_anatomy_from_tables,
)
# ---------------- Global Vars --------------------------:
max_number_of_study_processes = 1
max_number_of_fix_processes = MAX_NUMBER_OF_THREADS
max_number_of_up_down_load_processes = MAX_NUMBER_OF_THREADS
max_number_of_bq_processes = MAX_NUMBER_OF_THREADS
max_number_of_frameset_processes = MAX_NUMBER_OF_THREADS
max_number_of_conversion_processes = MAX_NUMBER_OF_THREADS
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
def namer(name=''):
    pid = os.getpid()
    if name == '':
        dt_string = datetime.now().strftime("[%d-%m-%Y][%H-%M-%S]")
        file_name = './Logs/log{}pid{:05d}.log'.format(dt_string, pid)
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
with open('log_config.json') as json_file:
    logger_config_dict = json.load(json_file)
logger_config_dict["handlers"]['file']['filename'] = file_name
# with open('log_config.json', 'w') as json_file:
#     json.dump(logger_config_dict, json_file, indent=4)
logging.config.dictConfig(logger_config_dict)
hs = logging.RootLogger.root.handlers
for h in hs:
    if h.name == 'file':
        h.namer = namer
install_mp_handler()
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
    ctools.RunExe([dcm_verify, '-filename', file], '', '', errlog = log,
                  char_encoding=char_set)
    # my_code_output = verify_dicom(file, False, '')


def FixFile(dicom_file: str, dicom_fixed_file: str,
            log_fix: list, log_david_pre: list, log_david_post: list,
            anatomy: tuple):
    ds = pydicom.read_file(dicom_file)
    char_set = DicomFileInfo.get_chaset_val_from_dataset(ds)
    # log_mine = []
    prelog = []
    VER(dicom_file, prelog, char_set=char_set)
    organize_dcmvfy_errors(prelog, log_david_pre)
    add_anatomy(ds, anatomy[0], anatomy[1], log_fix)
    fix_dicom(ds, log_fix)
    # fix_report = PrintLog(log_fix)
    pydicom.write_file(dicom_fixed_file, ds)
    postlog = []
    VER(dicom_fixed_file, postlog, char_set=char_set)
    organize_dcmvfy_errors(postlog, log_david_post)
    return ds


def BuildQueries1(table_q_info: table_quota, qs: list, dataset_id: str,
                 return_: bool = True, processes: ProcessPool=None) -> list:
    logger = logging.getLogger(__name__)
    rows = []
    for q in qs:
        rows.append(q[1])
    stream_insert(table_q_info.table_base_id, rows, table_q_info.schema)


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
                query_string(out_q[-1], '')
            else:
                # logger.info('putting in queue')
                processes.queue.put(
                    (
                        query_string,
                        (out_q[-1], '')
                    )
                )
    header = header_ptrn.format(table_q_info.get_table(), '{}')
    out_q.append(header.format(elem_q))
    if processes is None:
        query_string(out_q[-1], '')
    else:
        # logger.info('putting in queue')
        processes.queue.put(
                    (
                        query_string,
                        (out_q[-1], '')
                    )
                )
    if return_:
        return out_q
    else:
        return []


def fix_one_instance(inst_info: DicomFileInfo,
                     fx_inst_info: DicomFileInfo,
                     input_table_name: str,
                     fixed_table_name: str,
                     anatomy: tuple) -> tuple:
    logger = logging.getLogger(__name__)
    fix_log = []
    pre_fix_issues = []
    post_fix_issues = []
    try:
        fx_ds = FixFile(
            inst_info.file_path, fx_inst_info.file_path, fix_log,
            pre_fix_issues,
            post_fix_issues, anatomy)
        fx_inst_info.study_uid = fx_ds.StudyInstanceUID
        fx_inst_info.sereies_uid = fx_ds.SeriesInstanceUID
        fx_inst_info.instance_uid = fx_ds.SOPInstanceUID
        # as a trick to workaround pickling problem
        fx_inst_info.dicom_ds = fx_ds
    except BaseException as err:
        msg = str(err)
        msg += '\n{}'.format(str(inst_info))
        logger.error(msg, exc_info=True)
        return([], [], [], flaw_query_form.format(
            inst_info.bucket_name, inst_info.study_uid,
            inst_info.series_uid, inst_info.instance_uid, 'FIX'))
    fixes_all = FixCollection(
        fix_log, fx_inst_info.study_uid,
        fx_inst_info.series_uid, fx_inst_info.instance_uid)
    fix_queries = fixes_all.GetQuery()
    pre_issues = IssueCollection(
        pre_fix_issues,
        input_table_name,
        inst_info.study_uid,
        inst_info.series_uid,
        inst_info.instance_uid)
    issue_queries = pre_issues.GetQuery()
    post_issues = IssueCollection(
        post_fix_issues,
        fixed_table_name,
        fx_inst_info.study_uid,
        fx_inst_info.series_uid,
        fx_inst_info.instance_uid)
    issue_queries.extend(post_issues.GetQuery())
    fixed_input_relation = conv.ParentChildDicoms(
        [pre_issues.SOPInstanceUID],
        post_issues.StudyInstanceUID,
        post_issues.SeriesInstanceUID,
        post_issues.SOPInstanceUID,
        fx_inst_info.file_path)
    origin_queries = fixed_input_relation.GetQuery(
        input_table_name,
        fixed_table_name)
    return(fix_queries, issue_queries, origin_queries, '')


def frameset_for_one_series(file_blob_pairs: List[DicomFileInfo],
                            series_folder_prifix: str):
    logger = logging.getLogger(__name__)
    # All frames set created out of one series must have the same series
    #   instance uid. So I have to create on sereies instance uid and a
    #   destination folder for future multiframe images
    # ------------------------------------------------
    multi_frame_series_uid = generate_uid(
        prefix="1.3.6.1.4.1.43046.3" + ".1.9.")
    multi_frame_series_folder = os.path.join(
        series_folder_prifix,
        multi_frame_series_uid)
    if not os.path.exists(multi_frame_series_folder):
        os.makedirs(multi_frame_series_folder)
    ds_list = []
    for f_bl in file_blob_pairs:
        ds_list.append(f_bl.dicom_ds)
    try:
        fs_collection = FrameSetCollection(ds_list)
        fs = fs_collection.FrameSets
    except BaseException as err:
        msg = str(err)
        msg += '\n The first sample out of {}:\n{}'.format(
            len(file_blob_pairs), str(file_blob_pairs[0]))
        logger.error(msg, exc_info=True)
        fs = []
    return(fs, multi_frame_series_uid, multi_frame_series_folder)


def extract_convert_framesets_for_bunch_of_studies(
        study_series_dict,
        mf_local_study_path: str,
        fx_gc_info, mf_gc_info) -> tuple:
    # Now I want to extract framesets from fixed sereis:
    logger = logging.getLogger(__name__)
    logger.info('Start finding the framesets')
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    tic = time.time()
    frameset_processes = ProcessPool(
        max_number_of_frameset_processes, 'frset')
    for study_uid, series_dict in study_series_dict.items():
        study_folder = mf_local_study_path.format(study_uid)
        for series_uid, file_blob_pairs in series_dict.items():
            frameset_processes.queue.put(
                (
                    frameset_for_one_series,
                    (
                        file_blob_pairs,
                        study_folder)
                )
            )
    frameset_processes.queue.join()
    frameset_processes.kill_them_all()
    toc = time.time()
    frameset_elapsed_time = toc - tic
    results = frameset_processes.output
    flaw_queries = []
    issue_queries = []
    origin_queries = []
    upload_blobfile_pairs = []
    number_of_all_framesets = 0
    # -> Starting the conversion
    tic = time.time()
    logger.info('Frameset calculation finished. '
                'Now starting converting the framesets')
    conversion_processes = ProcessPool(
        max_number_of_conversion_processes, 'convert')
    for(file_blob_pairs, prefix), \
            (fsets, mf_series_uid, mf_series_dir) in results:
        if len(fsets) == 0:
            for file_blob in file_blob_pairs:
                f_query = flaw_query_form.format(
                    file_blob.bucket_name, file_blob.study_uid,
                    file_blob.series_uid, file_blob.instance_uid, 'FRAMESET')
                flaw_queries.append(f_query)
        else:
            mf_study_uid = file_blob_pairs[0].study_uid
            for fset in fsets:
                number_of_all_framesets += 1
                upload_blobfile_pairs.extend(file_blob_pairs)
                mf_instace_uid = generate_uid(
                    prefix="1.3.6.1.4.1.43046.3" + ".1.9.")
                mf_file_path = os.path.join(
                    mf_series_dir, '{}.dcm'.format(mf_instace_uid))
                conversion_processes.queue.put(
                    (
                        conv.ConvertFrameset,
                        (
                            fset,
                            mf_file_path,
                            mf_study_uid,
                            mf_series_uid,
                            mf_instace_uid)
                    )
                )
    conversion_processes.queue.join()
    conversion_processes.kill_them_all()
    toc = time.time()
    conversion_elapsed_time = toc - tic
    conversion_results = conversion_processes.output
    number_of_all_converted_mf = 0
    for args, pr_ch in conversion_results:
        if pr_ch is None:
            fr_sets = args[0]
            for fr in fr_sets.Frames:
                st_id = fr.StudyInstanceUID
                se_id = fr.SeriesInstanceUID
                sop_id = fr.SOPInstanceUID
            f_query = flaw_query_form.format(
                study_series_dict[st_id][se_id][0].bucket_name,
                st_id, se_id, sop_id, 'CONVERSION')
            flaw_queries.append(f_query)
        else:
            number_of_all_converted_mf += 1
            origin_queries.extend(pr_ch.GetQuery(fx_table_name, mf_table_name))
            multiframe_log = []
            VER(pr_ch.child_dicom_file, multiframe_log)
            mf_issues = IssueCollection(
                multiframe_log[1:], mf_table_name,
                pr_ch.child_study_instance_uid,
                pr_ch.child_series_instance_uid,
                pr_ch.child_sop_instance_uid, )
            issue_queries.extend(mf_issues.GetQuery())
            mf_blob_path = '{}/dicom/{}/{}/{}.dcm'.format(
                    mf_gc_info.Bucket.DataObject,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_series_instance_uid)
            upload_blobfile_pairs.append(DicomFileInfo(
                mf_gc_info.Bucket.ProjectID,
                mf_gc_info.Bucket.Dataset,
                mf_blob_path, pr_ch.child_dicom_file,
                pr_ch.child_study_instance_uid,
                pr_ch.child_series_instance_uid,
                pr_ch.child_sop_instance_uid))
    frameset_perf = PerformanceMeasure(
        number_of_all_framesets, frameset_elapsed_time, '(frameset)', False)
    mf_perf = PerformanceMeasure(
        number_of_all_converted_mf, conversion_elapsed_time,
        '(multiframe-inst)')
    logger.info(
        '\tfinished conversion to multi-frame '
        'instances first {} then {}'.format(str(frameset_perf), str(mf_perf)))
    return(issue_queries, origin_queries, upload_blobfile_pairs, flaw_queries,
            frameset_perf, mf_perf)


def organiase_file_blob_infos(file_blob_list: list):
    output = {}
    st_count = 0
    se_count = 0
    inst_count = len(file_blob_list)
    for f in file_blob_list:
        if f.study_uid in output:
            if f.series_uid in output[f.study_uid]:
                output[f.study_uid][f.series_uid].append(f)
            else:
                se_count += 1
                output[f.study_uid][f.series_uid] = [f]
        else:
            se_count += 1
            st_count += 1
            output[f.study_uid] = {f.series_uid: [f]}
    return(output, st_count, se_count, inst_count)


def download_fix_convert_upload_one_sereis(
        inst_infos: list,
        fx_local_study_path: str,
        mf_local_study_path: str,
        in_gc_info, fx_gc_info, mf_gc_info, anatomy: tuple):
    logger = logging.getLogger(__name__)
    try:
        download_fix_convert_upload_one_sereis.counter += 1
    except AttributeError:
        download_fix_convert_upload_one_sereis.counter = 1
    
    if len(inst_infos) == 0:
        logger.debug('The input is empty')
        return([], [], [], [], 0, 0, 0, 0, 0, 0)
    current_pid = os.getpid()
    insert_id = int('1{:05d}{:04d}00000'.format(
        current_pid,download_fix_convert_upload_one_sereis.counter)
        )
    in_table_name = in_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleTableAddress(False)
    single_frames = []
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []

    defective_study_series = []
    downloaded_files_size = 0
    fixed_files_size = 0
    mf_files_size = 0
    upload_files_size = 0
    in_series_dir = os.path.dirname(inst_infos[0].file_path)
    fx_blob_form = '{}/dicom/{{}}/{{}}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject)
    for obj in inst_infos:
        success = download_blob(
            in_gc_info.Bucket.ProjectID,
            obj.bucket_name,
            obj.blob_address,
            obj.file_path)
        logger.debug('Start downloading {}'.format(obj.file_path))
        downloaded_files_size += os.path.getsize(obj.file_path)
        if not success:
            flaw_queries.append(flaw_query_form.format(
                    obj.bucket_name, obj.study_uid,
                    obj.series_uid, obj.instance_uid,
                    'DOWNLOAD')
                )
            rm((in_series_dir,), False)
            return([], [], [], flaw_queries, 0, 0,
                    downloaded_files_size, fixed_files_size,
                    mf_files_size, upload_files_size)
        # I'm using downloaded file uids for fix files
        stuyd_folder = fx_local_study_path.format(obj.study_uid)
        fx_file = '{}/{}/{}.dcm'.format(
            stuyd_folder, obj.series_uid, obj.instance_uid)
        fx_obj = DicomFileInfo(
            fx_gc_info.Bucket.ProjectID, fx_gc_info.Bucket.Dataset,
            '', fx_file, obj.study_uid, obj.series_uid, obj.study_uid)
        logger.debug('Start fixing {}'.format(obj.file_path))
        (fix_q, iss_q, org_q, flaw) = fix_one_instance(
            obj,
            fx_obj,
            in_table_name, fx_table_name, anatomy)
        bgq_db_id = fx_gc_info.BigQuery.GetBigQueryStyleDatasetAddress(False)
        fix_report_table_id = '{}.{}'.format(bgq_db_id, 'FIX_REPORT')
        issue_report_table_id = '{}.{}'.format(bgq_db_id, 'ISSUE')
        orig_report_table_id = '{}.{}'.format(bgq_db_id, 'ORIGINATED_FROM')
        if flaw == '':
            fix_queries.extend(fix_q)
            rows = []
            ids = list(range(insert_id, insert_id + len(fix_q)))
            for q_elem in fix_q:
                rows.append(q_elem[1])
            stream_insert_with_ids(fix_report_table_id, rows, ids)
            rows = []
            ids = list(range(insert_id, insert_id + len(iss_q)))
            for q_elem  in iss_q:
                rows.append(q_elem[1])
            stream_insert_with_ids(issue_report_table_id, rows, ids)
            rows = []
            ids = list(range(insert_id, insert_id + len(org_q)))
            for q_elem  in org_q:
                rows.append(q_elem[1])
            stream_insert_with_ids(issue_report_table_id, rows, ids)
            issue_queries.extend(org_q)
            origin_queries.extend(org_q)
            single_frames.append(fx_obj)
            fx_obj.blob_address = fx_blob_form.format(
                fx_obj.study_uid, fx_obj.series_uid,
                fx_obj.instance_uid)
            logger.debug(
                'Start uploading the fixed file {}'.format(fx_obj.file_path))
            success = upload_blob(
                fx_gc_info.Bucket.ProjectID,
                fx_gc_info.Bucket.Dataset,
                fx_obj.blob_address,
                fx_file)
            fixed_files_size += os.path.getsize(fx_obj.file_path)
            if not success:
                flaw_queries.append(flaw_query_form.format(
                    fx_obj.bucket_name, fx_obj.study_uid,
                    fx_obj.series_uid, fx_obj.instance_uid,
                    'UPLOAD')
                )
            else:
                upload_files_size += os.path.getsize(fx_obj.file_path)
        else:
            flaw_queries.append(flaw)
            defective_study_series.append(
                (fx_obj.study_uid, fx_obj.series_uid))
    # The code is not gonna proceed to conversion if there is any fix issue
    fx_series_dir = os.path.dirname(single_frames[0].file_path)
    if len(flaw_queries) != 0:
        rm((in_series_dir, fx_series_dir), False)
        return([], [], [], flaw_queries, 0, 0,
                downloaded_files_size, fixed_files_size,
                mf_files_size, upload_files_size)
    # Now I want to extract framesets from fixed sereis:
    study_uid = inst_infos[0].study_uid
    study_folder = mf_local_study_path.format(study_uid)
    (fsets, mf_series_uid, mf_series_dir) = frameset_for_one_series(
        single_frames,
        study_folder)
    logger.debug('Start conversion process for {} frameset'.format(len(fsets)))
    number_of_all_converted_mf = 0
    if len(fsets) == 0:
        for file_blob in single_frames:
            f_query = flaw_query_form.format(
                file_blob.bucket_name, file_blob.study_uid,
                file_blob.series_uid, file_blob.instance_uid, 'FRAMESET')
            flaw_queries.append(f_query)
    else:
        mf_study_uid = single_frames[0].study_uid
        char_set = DicomFileInfo.get_chaset_val_from_dataset(single_frames[0])
        for fset in fsets:
            # remove ds from single frome for multi_processing purpose
            for bl_f in single_frames:
                bl_f.dicom_ds = None
            mf_instace_uid = generate_uid(
                prefix="1.3.6.1.4.1.43046.3" + ".1.9."
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
                    inst_infos[0].bucket_name,
                    st_id, se_id, sop_id, 'CONVERSION')
                flaw_queries.append(f_query)
            else:
                mf_files_size += os.path.getsize(pr_ch.child_dicom_file)
                number_of_all_converted_mf += 1
                origin_queries.extend(
                    pr_ch.GetQuery(fx_table_name, mf_table_name))
                multiframe_log = []
                VER(pr_ch.child_dicom_file, multiframe_log, char_set=char_set)
                mf_issues = IssueCollection(
                    multiframe_log[1:], mf_table_name,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_sop_instance_uid, )
                issue_queries.extend(mf_issues.GetQuery())
                mf_blob_path = '{}/dicom/{}/{}/{}.dcm'.format(
                        mf_gc_info.Bucket.DataObject,
                        pr_ch.child_study_instance_uid,
                        pr_ch.child_series_instance_uid,
                        pr_ch.child_sop_instance_uid)
                success = upload_blob(
                    mf_gc_info.Bucket.ProjectID,
                    mf_gc_info.Bucket.Dataset,
                    mf_blob_path, pr_ch.child_dicom_file)
                if not success:
                    flaw_queries.append(flaw_query_form.format(
                        mf_gc_info.Bucket.Dataset, pr_ch.study_uid,
                        pr_ch.series_uid, pr_ch.instance_uid,
                        'UPLOAD')
                    )
                else:
                    upload_files_size += os.path.getsize(pr_ch.child_dicom_file)
    # Now I can remove the series:
    rm((in_series_dir, fx_series_dir, mf_series_dir), False)
    logging.info('fixed = {}, converted = {} orig = {}'.format(len(inst_infos), number_of_all_converted_mf, len(origin_queries)))
    return(fix_queries, issue_queries, origin_queries, flaw_queries,
            len(fsets), number_of_all_converted_mf,
            downloaded_files_size, fixed_files_size,
            mf_files_size, upload_files_size)


def process_series_parallel(in_folder: str, studies_chunk: List[Tuple],
                            in_gc_info, fx_gc_info, mf_gc_info,
                            max_number: int=2 ** 63 - 1) -> ProcessPerformance:
    logger = logging.getLogger(__name__)
    fx_sub_dir = 'FIXED'
    mf_sub_dir = 'MULTIFRAME'
    in_sub_dir = 'ORIGINAL'
    logger.info('Start to process a chunk of {} stud{}'.format(
        len(studies_chunk), 'y' if len(studies_chunk) == 1 else 'ies'
            ))
    max_number_of_instances = max_number
    max_number_of_series = max_number
    blob_address_pattern = 'dicom/{}/{}/{}.dcm'
    input_blob_file_pairs = []
    study_local_folders = []
    for number_of_studies, (study_uid, collection_id, series_dictinary) in\
            enumerate(studies_chunk, 1):
        study_local_folder = os.path.join(in_folder, study_uid)
        study_local_folders.append(study_local_folder)
        for number_of_series, (series_uid, [size, instances]) in\
                enumerate(series_dictinary.items(), 1):
            if number_of_series > max_number_of_series:
                break
            # ------------------------------------
            # create the folder for downloading series:
            series_local_folder = os.path.join(
                study_local_folder, '{}/{}'.format(
                    in_sub_dir, series_uid))
            if not os.path.exists(series_local_folder):
                os.makedirs(series_local_folder)
            fx_series_local_folder = os.path.join(
                study_local_folder, '{}/{}'.format(
                    fx_sub_dir, series_uid))
            if not os.path.exists(fx_series_local_folder):
                os.makedirs(fx_series_local_folder)
            for number_of_inst, instance_uid in enumerate(instances, 1):
                if number_of_inst > max_number_of_instances:
                    break
                blob_address = blob_address_pattern.format(
                    study_uid, series_uid, instance_uid)
                file_path = os.path.join(
                    series_local_folder, '{}.dcm'.format(instance_uid))
                input_blob_file_pairs.append(
                    DicomFileInfo(
                        in_gc_info.Bucket.ProjectID,
                        collection_id,
                        blob_address,
                        file_path,
                        study_uid,
                        series_uid,
                        instance_uid))
    # ----> download, fix, convert, upload series:
    fix_queries = []
    issue_queries = []
    origin_queries = []
    flaw_queries = []
    frameset_number = 0
    multiframe_number = 0
    downloaded_files_size = 0
    fixed_files_size = 0
    mf_files_size = 0
    uploaded_files_size = 0
    study_series_dict, st_count, se_count, inst_count = \
        organiase_file_blob_infos(input_blob_file_pairs)
    proc_num = min(se_count, max_number_of_fix_processes)
    logger.info(
        'Chunk containing {} studies, {} series and, {} instances'.format(
            st_count, se_count, inst_count))
    logger.info('Starting {} = min({}, {}) parallel subprocesses'.format(
        proc_num, se_count, max_number_of_fix_processes))
    jobs = []
    q_sz = 0
    max_q_cap = 4000 * proc_num
    for study_uid, study_contents in study_series_dict.items():
        for series_uid, series_contents in study_contents.items():
            st_anatomy_info = None
            cl_anatomy_info = None
            for cln, cln_an in anatomy_info.items():
                cl_anatomy_info = cln_an[0]
                if study_uid in cln_an[1]:
                    st_anatomy_info = cln_an[1][study_uid]
                    break
            if st_anatomy_info is not None:
                anatomy = get_anatomy_info(st_anatomy_info)
            if anatomy[0] is None and anatomy[1][0] is None:
                anatomy = get_anatomy_info(cl_anatomy_info)
            if q_sz % max_q_cap == 0:
                container = []
                jobs.append(container)
            container.append(
                (
                    download_fix_convert_upload_one_sereis,
                    (
                        series_contents,
                        '{}{}{}'.format(
                            in_folder, '/{}', '/{}'.format(fx_sub_dir)),
                        '{}{}{}'.format(
                            in_folder, '/{}', '/{}'.format(mf_sub_dir)),
                        in_gc_info, fx_gc_info, mf_gc_info, anatomy)
                )
            )
            q_sz += 1
    tic = time.time()
    for ii, job_let in enumerate(jobs, 1):
        logger.info('{}/{} of job bunches'.format(ii, len(jobs)))
        processes = ProcessPool(proc_num, 'd+f+c+u')
        for j in job_let:
            processes.queue.put(j)
        processes.queue.join()
        processes.kill_them_all()
        results = processes.output
        for args, outs in results:
            fq, isq, orq, flq, fs, ms, dl_sz, fx_sz, mf_sz, ul_sz = outs
            fix_queries.extend(fq)
            issue_queries.extend(isq)
            origin_queries.extend(orq)
            flaw_queries.extend(flq)
            frameset_number += fs
            multiframe_number += ms
            downloaded_files_size += dl_sz
            fixed_files_size += fx_sz
            mf_files_size += mf_sz
            uploaded_files_size += mf_sz
    toc = time.time()
    dl_perfs = PerformanceMeasure(downloaded_files_size, toc - tic, 'B')
    fx_perfs = PerformanceMeasure(inst_count, toc - tic, '(inst)', False)
    frset_perfs = PerformanceMeasure(
        frameset_number, toc - tic, '(inst)', False)
    mf_perfs = PerformanceMeasure(
        multiframe_number, toc - tic, '(inst)', False)
    ul_perfs = PerformanceMeasure(uploaded_files_size, toc - tic, 'B')
    fx_perfs_sz = PerformanceMeasure(fixed_files_size, toc - tic, 'B')
    mf_perfs_sz = PerformanceMeasure(mf_files_size, toc - tic, 'B')
    logger.info('download {}'.format(dl_perfs))
    logger.info('fix      {} or {}'.format(fx_perfs, fx_perfs_sz))
    logger.info('convert  {} or {}'.format(mf_perfs, mf_perfs_sz))
    logger.info('upload   {}'.format(ul_perfs))
    # --> Populate big query tables:
    # -------------------------------
    dataset_id = '{}.{}'.format(
        fx_gc_info.BigQuery.ProjectID,
        fx_gc_info.BigQuery.Dataset)
    logger.info('Start running bigquery jobs')
    big_q_processes = ProcessPool(
        max_number_of_bq_processes, 'BQ')
    tic = time.time()
    all_rows = (len(fix_queries) + len(issue_queries) + len(origin_queries) +
                len(flaw_queries))
    global fix_report_tq
    global issue_report_tq
    global org_report_tq
    global defect_report_tq
    if len(fix_queries) != 0:
        BuildQueries1(
            fix_report_tq,
            fix_queries,
            dataset_id, False,
            big_q_processes)
    if len(issue_queries) != 0:
        BuildQueries1(
            issue_report_tq,
            issue_queries,
            dataset_id, False,
            big_q_processes)
    if len(origin_queries) != 0:
        BuildQueries(
            org_report_tq,
            origin_queries,
            dataset_id, False,
            big_q_processes)
        for iq, qqq in enumerate(origin_queries, 1):
            if iq == 1:
                append = False
            else:
                append = True
            ctools.WriteStringToFile(
                './gitexcluded_qqq.txt', '{} -> {}'.format(iq, qqq), append)
    if len(flaw_queries) != 0:
        BuildQueries(
            org_report_tq,
            flaw_queries,
            dataset_id, False,
            big_q_processes)
    big_q_processes.queue.join()
    big_q_processes.kill_them_all()
    toc = time.time()
    big_query_measure = PerformanceMeasure(all_rows, toc - tic, '(row)', False)
    logger.info(
        'Big query tables were populated'
        ' successfully {}'.format(big_query_measure))
    rm(study_local_folders)
    return ProcessPerformance(
        dl_perfs, ul_perfs, fx_perfs, frset_perfs, mf_perfs, big_query_measure)


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



def empty_bucket_contents(proj_id: str, bucket: str,
                          ps_num: int, prefix: str = None):
    logger = logging.getLogger(__name__)
    max_retries = 2
    retries = 0
    tic = time.time()
    def get_blobs_and_list_them(proj_id, bucket, prefix):
        blobs = list_blobs(proj_id, bucket, prefix)
        return list(blobs)
    blob_list = ctools.retry_if_failes(
        get_blobs_and_list_them, (proj_id, bucket, prefix,), wait_in_sec=10,
        give_message=True,
        messaging_intervals=10)
    total_number_of_blobs = len(blob_list)
    if total_number_of_blobs == 0:
        logger.info(
            'The bucket is already empty')
        return []
    logger.info(
        'Started emptying bucket with {} contents'.format(
            total_number_of_blobs))
    ps = ProcessPool(min(ps_num, total_number_of_blobs), 'empty_bucket')
    while retries < max_retries:
        for bl in blob_list:
            if isinstance(bl, str):
                bname = bl
            else:
                bname = bl.name
            ps.queue.put(
                (
                    delete_blob,
                    (proj_id, bucket, bname,)
                )
            )
        ps.queue.join()
        ps.kill_them_all()
        results = ps.output
        not_deleteds = []
        for (pr, buc, bl_n,), suc in results:
            if not suc:
                not_deleteds.append(bl_n)
        if len(not_deleteds) == 0:
            break
        retries += 1
        blob_list = not_deleteds
        logger.info(
            'emptying was not seccessful. going for retry({})'.format(retries))
    nn = len(not_deleteds)
    if nn != 0:
        logger.info(
            "emptying was not successful couldn't delete {} blobs".format(nn))
    else:
        logger.info("emptying was successful")
    toc = time.time()
    perf = PerformanceMeasure(total_number_of_blobs, toc - tic, '(blob)', False)
    logger.info('emptying operation {}'.format(perf))
    return not_deleteds


def delete_bucket_all_or_part(proj_id: str, bucket: str,
                              ps_num: int, prefix: str = None):
    if not exists_bucket(proj_id, bucket):
        return True
    not_deleteds = empty_bucket_contents(proj_id, bucket, ps_num, prefix)
    if len(not_deleteds) > 256 and prefix is None:
        delete_bucket(proj_id, bucket)           
    return len(not_deleteds) == 0


def get_one_series_size(project_id: str, bucket_name: str,
                        study_uid: str, series_uid: str,
                        inst_uids: list = []) -> None:
    logger = logging.getLogger(__name__)
    prefix = 'dicom/{}/{}/'.format(study_uid, series_uid)
    size = float(0)
    # logger.info('getting pp {}'.format(prefix))
    if len(inst_uids) != 0:
        for ins in inst_uids:
            blob_name = prefix + '{}.dcm'.format(ins)
            bl = get_blob(project_id, bucket_name, blob_name)
            if bl is not None:
                size += bl.size
    else:
        max_retries = 30
        retries = 0
        while retries < max_retries:
            try:
                size = float(0)
                blob_list = list_blobs(project_id, bucket_name, prefix)
                for bl in blob_list:
                    size += bl.size
                break
            except BaseException as err:
                retries += 1
                if retries < max_retries:
                    pause_time = 60
                    logger.info("pausing for {} sec ...".format(pause_time))
                    time.sleep(pause_time)
                    logger.info("start retry number {}".format(retries)) 
                else:
                    raise err
    return size


def get_all_series_size(proj_id: str, uids: dict, ps_num: int,
                         partial: bool = False):
    logger = logging.getLogger(__name__)
    # ps_num = MAX_NUMBER_OF_THREADS
    logger.info('start getting the size of {} series on {} processes'.format(
        'part of' if partial else 'all', ps_num
    ))
    tic = time.time()
    ps = ProcessPool(ps_num, 'se_sz')
    global processes_to_monitor
    processes_to_monitor = ps
    series_count = 0
    for st_counter, (st_uid, (bucket_name, se_dict)) in enumerate(uids.items(), 1):
        for se_counter, (se_uid, ins) in enumerate(se_dict.items(), 1):
            if partial:
                inst_uids = ins[1]
                ps.queue.put(
                    (
                        get_one_series_size,
                        (proj_id, bucket_name, st_uid, se_uid, inst_uids,)
                    )
                )
            else:
                ps.queue.put(
                    (
                        get_one_series_size,
                        (proj_id, bucket_name, st_uid, se_uid, [])
                    )
                )
            series_count += 1
    ps.queue.join()
    ps.kill_them_all()
    processes_to_monitor = []
    results = ps.output
    z_count = 0
    for (p, b, st, se, ins), sz in results:
        if sz == 0:
            c_count += 1
        else:
            uids[st][1][se][0] = sz
    toc = time.time()
    perf = PerformanceMeasure(series_count, toc - tic, 'series', False)
    logger.info('Retrieved all series sizes {}'.format(perf))
    return uids


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


def main(number_of_processes: int = None,
         rough_series_count_in_chunk: int=600):
    if number_of_processes is None:
        number_of_processes = MAX_NUMBER_OF_THREADS
    # StudyProcess.initialize_statics()
    global max_number_of_fix_processes
    global max_number_of_up_down_load_processes
    global max_number_of_bq_processes
    global max_number_of_frameset_processes
    global max_number_of_conversion_processes
    max_number_of_fix_processes = number_of_processes
    max_number_of_up_down_load_processes = number_of_processes
    max_number_of_bq_processes = number_of_processes
    max_number_of_frameset_processes = number_of_processes
    max_number_of_conversion_processes = number_of_processes
    home = os.path.expanduser("~")
    pid = os.getpid()
    local_tmp_folder = os.path.join(home, "Tmp-{:05d}".format(pid))
    in_dicoms = DataInfo(
        Datalet('idc-tcia',      # Bucket
                'us',
                '', ''),
        Datalet('idc-dev-etl',      # Dicom Store
                'us-central1',
                'idc_tcia_mvp_wave0',
                'idc_tcia'),
        Datalet('idc-dev-etl',      # Bigquery
                'us-central1',
                'idc_tcia_mvp_wave0',
                'idc_tcia_dicom_metadata'),
        )
    general_dataset_name = 'afshin_results_00_' + in_dicoms.BigQuery.Dataset
    fx_dicoms = DataInfo(
        Datalet('idc-tcia',      # Bucket
                'us',
                general_dataset_name,
                'FIXED'),
        Datalet('idc-tcia',      # Dicom Store
                'us',
                general_dataset_name,
                'FIXED'),
        Datalet('idc-tcia',      # Bigquery
                'us',
                general_dataset_name,
                'FIXED')
        )
    mf_dicoms = DataInfo(
        Datalet('idc-tcia',      # Bucket
                'us',
                general_dataset_name,
                'MULTIFRAME'),
        Datalet('idc-tcia',      # Dicom Store
                'us',
                general_dataset_name,
                'MULTIFRAME'),
        Datalet('idc-tcia',      # Bigquery
                'us',
                general_dataset_name,
                'MULTIFRAME')
        )
    BigQueryInputCollectionInfo = Datalet(
        'idc-dev-etl',      # Bigquery
        'us',
        'idc_tcia_mvp_wave0',
        'idc_tcia_auxilliary_metadata')
    create_all_tables('{}.{}'.format(
        fx_dicoms.BigQuery.ProjectID, fx_dicoms.BigQuery.Dataset),
        fx_dicoms.BigQuery.CloudRegion, True)
    db_dataset_address =\
        fx_dicoms.BigQuery.GetBigQueryStyleDatasetAddress(False)
    global fix_report_tq
    global issue_report_tq
    global org_report_tq
    global defect_report_tq
    fix_report_tq = table_quota(
        10, '{}.{}'.format(
            db_dataset_address, 'FIX_REPORT'), schema_fix)
    issue_report_tq = table_quota(
        10, '{}.{}'.format(
            db_dataset_address, 'ISSUE'), schema_issue)
    org_report_tq = table_quota(
        10, '{}.{}'.format(
            db_dataset_address, 'ORIGINATED_FROM'),
        schema_originated_from)
    defect_report_tq = table_quota(
        10, '{}.{}'.format(
            db_dataset_address, 'DEFECTIVE'),
        schema_originated_from)

    # --> this suffices to remove both issueand multiframes buckets
    success = delete_bucket_all_or_part(
        fx_dicoms.Bucket.ProjectID, fx_dicoms.Bucket.Dataset,
        number_of_processes)
    if not success:
        logger.info(
            "Couldn't delete the bucket successfully."
            " The process is going to be aborted")
        return
    create_bucket(
        fx_dicoms.Bucket.ProjectID,
        fx_dicoms.Bucket.Dataset,
        False)
    create_bucket(
        mf_dicoms.Bucket.ProjectID,
        mf_dicoms.Bucket.Dataset,
        False)
    max_number = 2 ** 63 - 1
    max_number = 50
    if max_number < 2 ** 63 - 1:
        limit_q = 'LIMIT 50000'
    else:
        limit_q = ''
    # with t1 as (select studyinstanceuid, x.CodeValue as CodeValue, x.CodeMeaning as CodeMeaning, x.codingSchemeDesignator as codingSchemeDesignator from `idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_dicom_metadata` CROSS JOIN UNNEST(anatomicregionsequence) as x), t2 as (select src.studyinstanceuid, src.BodyPartExamined from `idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_dicom_metadata` as src group by studyinstanceuid, Bodypartexamined) select t2.Studyinstanceuid, t1.Studyinstanceuid, Bodypartexamined , CodeValue, CodeMeaning, CodingSchemeDesignator from t1 full outer join t2 on t1.studyinstanceuid=t2.studyinstanceuid where not (Bodypartexamined is null and codevalue is null) group by t2.Studyinstanceuid, t1.Studyinstanceuid, Bodypartexamined , CodeValue, CodeMeaning, CodingSchemeDesignator order by t2.studyinstanceuid
    study_query = """
                WITH DICOMS AS (
                SELECT STUDYINSTANCEUID, SERIESINSTANCEUID, SOPINSTANCEUID
                FROM {}
                WHERE
                    SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.2" OR
                    SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.4" OR
                    SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.128"
                    {} )
                    SELECT DICOMS.STUDYINSTANCEUID,
                        DICOMS.SERIESINSTANCEUID,
                        DICOMS.SOPINSTANCEUID,
                        COLLECTION_TABLE.GCS_Bucket,
                    FROM DICOMS JOIN
                        {} AS
                        COLLECTION_TABLE ON
                        COLLECTION_TABLE.SOPINSTANCEUID = DICOMS.SOPINSTANCEUID
    """.format(in_dicoms.BigQuery.GetBigQueryStyleTableAddress(), limit_q,
               BigQueryInputCollectionInfo.GetBigQueryStyleTableAddress())

    global anatomy_info
    anatomy_info = quey_anatomy_from_tables(
        '`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_dicom_metadata`',
        '`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_auxilliary_metadata`')
    uids: dict = {}
    # q_dataset_uid = '{}.{}.{}'.format(
    #     in_dicoms.BigQuery.ProjectID,
    #     in_dicoms.BigQuery.Dataset,
    #     in_dicoms.BigQuery.DataObject
    #     )
    logger = logging.getLogger(__name__)
    max_number_of_studies = max_number
    max_number_of_series = max_number
    max_number_of_intances = max_number
    start_time = time.time()
    studies = query_string_with_result(study_query)
    number_of_all_inst = studies.total_rows
    performance_history = []
    number_of_inst_processed = 1
    whole_performace = None
    number_of_st_processed = 1
    vrtual_mem = psutil.virtual_memory()
    hdd_mem = psutil.disk_usage('/')
    if studies is not None:
        for row in studies:
            stuid = row.STUDYINSTANCEUID
            seuid = row.SERIESINSTANCEUID
            sopuid = row.SOPINSTANCEUID
            cln_id = row.GCS_Bucket
            if stuid in uids:
                if seuid in uids[stuid][1]:
                    if len(uids[stuid][1][seuid][1]) >= max_number_of_intances:
                        continue
                    uids[stuid][1][seuid][1].append(sopuid)
                else:
                    if len(uids[stuid]) >= max_number_of_series:
                        continue
                    uids[stuid][1][seuid] = [0, [sopuid]]
            else:
                if len(uids) >= max_number_of_studies:
                    continue
                uids[stuid] = (cln_id, {seuid: [0, [sopuid]]})
        uids = get_all_series_size(
            in_dicoms.Bucket.ProjectID, uids, number_of_processes,
            max_number < 2 ** 63 - 1)
        number_of_all_studies = min(len(uids), max_number_of_studies)
        max_study_count_in_chunk = 300
        max_series_count_in_chunk = (
            rough_series_count_in_chunk // number_of_processes
            ) * number_of_processes
        max_mem = vrtual_mem.free / 8

        series_chunk_count = 0
        study_chunk = []
        study_uids = []
        chunk_memory = 0
        for number_of_studies, (study_uid, sub_study) in enumerate(uids.items(), 1):
            # if number_of_studies < 3022:
            #     continue
            study_uids.append(study_uid)
            first_half = {}
            second_half = {}
            second_half_sz = 0
            for se_uid, se_v in sub_study[1].items():
                chunk_memory += se_v[0]
                if chunk_memory < max_mem:
                    first_half[se_uid] = se_v
                    series_chunk_count += 1
                else:
                    second_half[se_uid] = se_v
                    second_half_sz += se_v[0]
            chunk_memory -= second_half_sz
            # if series_chunk_count > max_series_count_in_chunk:
            #     diff = series_chunk_count - max_series_count_in_chunk
            #     first_half, second_half = partition_series(sub_study[1], diff)
            # else:
            #     first_half = sub_study[1]
            #     second_half = {}
            study_chunk.append((study_uid, sub_study[0], first_half))
            if number_of_studies == len(uids) or \
                    second_half_sz != 0:
                logger.info(
                    'Bunch of studies with {} series and size of {}B'.format(
                        series_chunk_count,
                        ctools.get_human_readable_string(chunk_memory)
                        ))
                try:
                    perf = process_series_parallel(
                        local_tmp_folder,
                        study_chunk,
                        in_dicoms, fx_dicoms, mf_dicoms,
                        max_number)
                    performance_history.append(perf)
                    number_of_inst_processed += perf.fix.size
                    if whole_performace is None:
                        whole_performace = perf
                    else:
                        whole_performace += perf
                    number_of_st_processed += len(study_chunk)
                except BaseException as err:
                    perf = ProcessPerformance()
                    logger.error(err, exc_info=True)
                progress = float(number_of_inst_processed) /\
                    float(number_of_all_inst)
                time_point = time.time()
                time_elapsed = round(time_point - start_time)
                time_left = round(
                    number_of_all_inst - number_of_inst_processed) * \
                    time_elapsed / float(number_of_inst_processed)
                header = '{}/{})Study = ({}/{}) instances was fix/'\
                    'convert-ed successfully'.format(
                        number_of_st_processed, number_of_all_studies,
                        number_of_inst_processed, number_of_all_inst)
                logger.info(header)
                for st in study_uids:
                    logger.info('\t\t\t{}'.format(st))
                progress_string = ctools.ShowProgress(
                    progress, time_elapsed, time_left, 60,
                    '\t\tInstace progress', False)
                logger.info(progress_string)
                logger.info(
                    'For this chunk of studies with <{}> threads {}'.format(
                        number_of_processes, str(perf))
                )
                logger.info(
                    'For all studies so far with <{}> threads    {}'.format(
                        number_of_processes,
                        str(whole_performace)))
                study_chunk = []
                study_chunk.append((study_uid, sub_study[0], second_half))
                study_uids = []
                series_chunk_count = len(second_half)
                chunk_memory = second_half_sz
    rm(local_tmp_folder)
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
    # Wait unitl populating bigquery stops
    status_logger.kill_timer()
# th = list(range(8, 256, 8))
# th = 88
# th = 35
# chunk = [100]
# for ch in chunk:
#     chunk *= 2
#     main(th, ch)
if __name__ == '__main__':
    status_logger = Periodic(log_status, None, 60)
    status_logger.start()
    try:
        main(33, 1000)
    finally:
        status_logger.kill_timer()
