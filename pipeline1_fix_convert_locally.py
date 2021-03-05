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
ref_info = None
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
        query_string(out_q[-1], '', project)
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


def organize_file_blob_infos(file_blob_list: list):
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

    defective_study_series = []
    fixed_files_size = 0
    mf_files_size = 0
    in_local_series_path = os.path.dirname(original_files[0])
    
    if not os.path.exists(fx_local_series_path):
        os.makedirs(fx_local_series_path)
    if not os.path.exists(mf_local_study_path):
        os.makedirs(mf_local_study_path)

    
    for obj in original_files:
        
        fx_file_path = obj.replace(in_local_series_path, fx_local_series_path)
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
            # rows, ids, insert_id = get_rows_and_insert_ids(fix_q, insert_id)
            # success = stream_insert_with_ids_with_ids(fix_report_table_id, rows, schema_fix)
            # if not success:
            fix_queries.extend(fix_q)
            # rows, ids, insert_id = get_rows_and_insert_ids(iss_q, insert_id)
            # success = stream_insert_with_ids_with_ids(issue_report_table_id, rows, schema_issue)
            # if not success:
            issue_queries.extend(iss_q)
            # rows, ids, insert_id = get_rows_and_insert_ids(org_q, insert_id)
            # success = stream_insert_with_ids_with_ids(orig_report_table_id, rows, schema_originated_from)
            # if not success:
            origin_queries.extend(org_q)
            single_frames.append(fx_file_path)
            logger.debug(
                'Start uploading the fixed file {}'.format(obj))
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
        mf_local_study_path)
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
                    in_collection_name,
                    st_id, se_id, sop_id, 'CONVERSION')
                flaw_queries.append(f_query)
            else:
                mf_files_size += os.path.getsize(pr_ch.child_dicom_file)
                number_of_all_converted_mf += 1
                org_q = pr_ch.GetQuery(fx_table_name, mf_table_name)
                # rows, ids, insert_id = get_rows_and_insert_ids(org_q, insert_id)
                # success = stream_insert_with_ids_with_ids(
                #     orig_report_table_id, rows, schema_originated_from)
                # if not success:
                origin_queries.extend(org_q)
                multiframe_log = []
                VER(pr_ch.child_dicom_file, multiframe_log, char_set=char_set)
                mf_issues = IssueCollection(
                    multiframe_log, mf_table_name,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_sop_instance_uid, )
                q_iss = mf_issues.GetQuery()
                # rows, ids, insert_id = get_rows_and_insert_ids(
                #     q_iss, insert_id)
                # success = stream_insert_with_ids_with_ids(
                #     issue_report_table_id, rows, schema_issue)
                # if not success:
                issue_queries.extend(q_iss)
    # Now I can remove the series:
    # rm((in_series_dir, fx_series_dir, mf_series_dir), False)
    logging.info('fixed = {}, converted = {} orig = {}'.format(
        len(in_local_series_path),
        number_of_all_converted_mf,
        len(origin_queries)))
    return(fix_queries, issue_queries, origin_queries, flaw_queries,
            len(fsets), number_of_all_converted_mf)


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
        organize_file_blob_infos(input_blob_file_pairs)
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
                    fix_convert_one_sereis,
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
    fix_queries = []
    issue_queries = []
    origin_queries = []
    flaw_queries = []
    frameset_number = 0
    multiframe_number = 0
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
        max_number_of_bq_processes, 'BQSTREAM')
    tic = time.time()
    all_rows = (len(fix_queries) + len(issue_queries) + len(origin_queries) +
                len(flaw_queries))
    global fix_report_tq
    global issue_report_tq
    global org_report_tq
    global defect_report_tq
    global ref_info
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
        BuildQueries1(
            org_report_tq,
            origin_queries,
            dataset_id, False,
            big_q_processes)

    if len(flaw_queries) != 0:
        BuildQueries(
            org_report_tq,
            flaw_queries,
            dataset_id, False,
            big_q_processes)
    
    toc = time.time()
    big_query_measure = PerformanceMeasure(all_rows, toc - tic, '(row)', False)
    logger.info(
        'Big query tables were populated'
        ' successfully {}'.format(big_query_measure))
    # rm(study_local_folders)
    return ProcessPerformance(
        dl_perfs, ul_perfs, fx_perfs, frset_perfs, mf_perfs, big_query_measure)



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
    fx_dicoms, mf_dicoms = create_datainfos(dataset_name)
    create_all_tables('{}.{}'.format(
        fx_dicoms.BigQuery.ProjectID, fx_dicoms.BigQuery.Dataset),
        fx_dicoms.BigQuery.CloudRegion, True, 
        project_id=fx_dicoms.BigQuery.ProjectID)
    create_bucket(
        fx_dicoms.Bucket.ProjectID,
        fx_dicoms.Bucket.Dataset,
        False)
    create_bucket(
        mf_dicoms.Bucket.ProjectID,
        mf_dicoms.Bucket.Dataset,
        False)


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


def main(dataset_name):
    series_paths = [
        '/workspaces/Tmp/in/1.3.6.1.4.1.14519.5.2.1.1357.4011.599277854519315291094834984976/1.3.6.1.4.1.14519.5.2.1.1357.4011.335385811943069724469579113670',
        '/workspaces/Tmp/in/1.3.6.1.4.1.14519.5.2.1.3023.4017.246199836259881483055596634768/1.3.6.1.4.1.14519.5.2.1.3023.4017.720525569168415113913096578859',
        '/workspaces/Tmp/in/1.3.6.1.4.1.14519.5.2.1.7695.1700.171220893861098819813996410099/1.3.6.1.4.1.14519.5.2.1.7695.1700.641077247274927806246916358599',
    ]
    fx_dicoms, mf_dicoms = create_datainfos(dataset_name)

    home = os.path.expanduser("~")
    pid = os.getpid()
    local_tmp_folder = os.path.join(home, "Tmp-{:05d}".format(pid))

    # dataset_name = 'afshin_terra_00_' + in_dicoms.BigQuery.Dataset

    
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
    create_bucket_tables(dataset_name)

    fix_queries = []
    issue_queries = []
    origin_queries = []
    flaw_queries = []
    frameset_number = 0
    multiframe_number = 0
    
    input_table_name = 'canceridc-data.idc_views.dicom_all'
    
    fx_local_series_path = '/Users/afshin/Documents/work/Tmp/fx'
    mf_local_study_path = '/Users/afshin/Documents/work/Tmp/mf'
    if os.path.exists(fx_local_series_path):
        rm(fx_local_series_path)
    if os.path.exists(mf_local_study_path):
        rm(mf_local_study_path)
    for in_local_series_path in series_paths:
        files = [os.path.join(in_local_series_path, i) for i in os.listdir(
            in_local_series_path) if i.endswith('.dcm')]
        outs = fix_convert_one_sereis(
            files,
            fx_local_series_path,
            mf_local_study_path,
            fx_dicoms, mf_dicoms, {}, input_table_name)
        fq, isq, orq, flq, fs, ms = outs
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
    ctools.RunExe([
        'gsutil', 'cp', '-r', fx_local_series_path, 
        'gs://{}/{}'.format(fx_dicoms.Bucket.Dataset,
        fx_dicoms.Bucket.DataObject) ],
        log_std_out=True, log_std_err=True)
    ctools.RunExe([
        'gsutil', 'cp', '-r', mf_local_study_path, 
        'gs://{}/{}'.format(mf_dicoms.Bucket.Dataset,
            mf_dicoms.Bucket.DataObject) ],
        log_std_out=True, log_std_err=True)
    
    # Wait unitl populating bigquery stops
    create_dicomstores(dataset_name)
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
        main('afshin_terra_test00')
    finally:
        status_logger.kill_timer()
