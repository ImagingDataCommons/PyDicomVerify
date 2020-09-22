import shutil
import pydicom
import re
import os
import fix_frequent_errors
import pydicom.charset
import time
from queue import Queue
from datetime import timedelta
import common_tools as ctools
import conversion as conv
import json
from datetime import datetime
from typing import List, Tuple
import logging
import logging.config
from DicomStoreStuff import (
    create_dataset, exists_dataset, exists_dicom_store, create_dicom_store,
    import_dicom_bucket, export_dicom_instance_bigquery)
from parallelization import (StudyThread,
                             ThreadPool, MAX_NUMBER_OF_THREADS)
from BigQueryStuff import (
    create_all_tables,
    query_string,
    query_string_with_result)
from StorageBucketStuff import (
    download_blob,
    upload_blob,
    create_bucket,
    )
from dicom_fix_issue_info import (
    FixCollection,
    IssueCollection,
    Datalet,
    DataInfo,
    DicomFileInfo,
    PerformanceMeasure, ProcessPerformance
    )
# ---------------- Global Vars --------------------------:
max_number_of_threads = os.cpu_count() + 1
max_number_of_study_threads = 1
max_number_of_series_threads = 4
max_number_of_instance_threads = MAX_NUMBER_OF_THREADS
max_number_of_up_down_load_threads = MAX_NUMBER_OF_THREADS 
max_number_of_bq_threads = MAX_NUMBER_OF_THREADS 
flaw_query_form = '''(
        "{}",-- COLLECTION_NAME
        "{}",-- STUDY_INSTANCE_UID
        "{}",-- SERIES_INSTANCE_UID
        "{}",-- SOP_INSTANCE_UID
        "{}"-- FLAW
            )
            '''
# Logger setup --------------------------------------------------------
with open('log_config.json') as json_file:
    d = json.load(json_file)
dt_string = datetime.now().strftime("[%d-%m-%Y][%H-%M-%S]")
file_name = './Logs/log{}.log'.format(dt_string)
folder = os.path.dirname(file_name)
if not os.path.exists(folder):
    os.makedirs(folder)
d["handlers"]['file']['filename'] = file_name
with open('log_config.json', 'w') as json_file:
    json.dump(d, json_file, indent=4)
logging.config.dictConfig(d)
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.CRITICAL)
# -----------------------------------------------------------------------


def VER(file: str, log: list):
    file_name = os.path.basename(file)
    if file_name.endswith('.dcm'):
        file_name = file_name[:-4]
    dcm_verify = "/Users/afshin/Documents/softwares"\
        "/dicom3tools/exe_20200430/dciodvfy"
    if not os.path.exists(dcm_verify):
        dcm_verify = shutil.which('dciodvfy')
        if dcm_verify is None:
            print("Error: install dciodvfy into system path")
            assert(False)
    ctools.RunExe([dcm_verify, '-filename', file], '', '', errlog=log)
    # my_code_output = verify(file, False, '')


def FixFile(dicom_file: str, dicom_fixed_file: str,
            log_fix: list, log_david_pre: list, log_david_post: list):
    ds = pydicom.read_file(dicom_file)
    # log_mine = []
    VER(dicom_file, log_david_pre)
    fix_frequent_errors.priorfix_RemoveIllegalTags(ds, 'All', log_fix)
    # (1)general fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("generalfix_"):
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log_fix)
    # (2)fix with verification:
    fix_frequent_errors.fix_Trivials(ds, log_fix)
    # (3)specific fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("fix_"):
            if ffix == "fix_Trivials":
                continue
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log_fix)
    # fix_report = PrintLog(log_fix)
    pydicom.write_file(dicom_fixed_file, ds)
    VER(dicom_fixed_file, log_david_post)
    return (
        ds.StudyInstanceUID,
        ds.SeriesInstanceUID,
        ds.SOPInstanceUID,
    )


def BuildQueries(header: str, qs: list, dataset_id: str,
                 return_: bool = True) -> list:
    logger = logging.getLogger(__name__)
    m = re.search('\.(.*)\n', header)
    if m is not None:
        table_name = m.group(1)
    else:
        table_name = ''
    out_q = []
    ch_limit = 1024*1000
    row_limit = 1000
    elem_q = ''
    n = 0
    rn = 0
    for q in qs:
        rn += 1
        if len(elem_q) + len(q) + len(header) < ch_limit and rn < row_limit:
            elem_q = q if elem_q == '' else '{},{}'.format(q, elem_q)
        else:
            n += 1
            out_q.append(header.format(dataset_id, elem_q))
            elem_q = ''
            rn = 0
            # print('{} ->'.format(n))
            logger.info("running query for '{}".format(table_name))
            query_string(out_q[-1])
    out_q.append(header.format(dataset_id, elem_q))
    logger.info("running query for '{}".format(table_name))
    query_string(out_q[-1])
    if return_:
        return out_q
    else:
        return []


def BuildQueries_parallel(header: str, qs: list, dataset_id: str,
                 return_: bool = True, threads: ThreadPool = None) -> list:
    # logger = logging.getLogger(__name__)
    m = re.search("\.(.*)\n", header)
    if m is not None:
        table_name = m.group(1)
    else:
        table_name = ''
    out_q = []
    ch_limit = 1024*1000
    row_limit = 1000
    elem_q = ''
    n = 0
    rn = 0
    for q in qs:
        rn += 1
        if len(elem_q) + len(q) + len(header) < ch_limit and rn < row_limit:
            elem_q = q if elem_q == '' else '{},{}'.format(q, elem_q)
        else:
            n += 1
            out_q.append(header.format(dataset_id, elem_q))
            elem_q = ''
            rn = 0
            if threads is None:
                query_string(out_q[-1], table_name)
            else:
                logger.info('putting in queue')
                threads.queue.put(
                    (
                        query_string,
                        (out_q[-1], table_name)
                    )
                )
    out_q.append(header.format(dataset_id, elem_q))
    if threads is None:
        query_string(out_q[-1], table_name)
    else:
        logger.info('putting in queue')
        threads.queue.put(
                    (
                        query_string,
                        (out_q[-1], table_name)
                    )
                )
    if return_:
        return out_q
    else:
        return []


def CreateDicomStore(project_id: str,
                     cloud_region: str,
                     dataset_id: str,
                     dicom_store_id: str):
    if not exists_dataset(project_id, cloud_region, dataset_id):
        create_dataset(project_id, cloud_region, dataset_id)
    if not exists_dicom_store(project_id, cloud_region, dataset_id,
                              dicom_store_id):
        create_dicom_store(
            project_id, cloud_region, dataset_id, dicom_store_id)


def fix_one_instance(inst_info: DicomFileInfo,
                     fx_inst_info: DicomFileInfo,
                     input_table_name: str,
                     fixed_table_name: str) -> tuple:
    logger = logging.getLogger(__name__)
    fix_log = []
    pre_fix_issues = []
    post_fix_issues = []
    try:
        (fx_inst_info.study_uid, fx_inst_info.sereies_uid,
            fx_inst_info.instance_uid) = FixFile(
            inst_info.file_path, fx_inst_info.file_path, fix_log,
            pre_fix_issues,
            post_fix_issues)
        fx_success = True
    except BaseException as err:
        logger.error(err, exc_info=True)
    if not fx_success:
        return ([], [], [], flaw_query_form.format(
            inst_info.bucket_name, inst_info.study_uid,
            inst_info.series_uid, inst_info.instance_uid, 'FIX'))
    fixes_all = FixCollection(
        fix_log, fx_inst_info.study_uid,
        fx_inst_info.series_uid, fx_inst_info.instance_uid)
    fix_queries = fixes_all.GetQuery()
    pre_issues = IssueCollection(
        pre_fix_issues[1:],
        input_table_name,
        inst_info.study_uid,
        inst_info.series_uid,
        inst_info.instance_uid)
    issue_queries = pre_issues.GetQuery()
    post_issues = IssueCollection(
        post_fix_issues[1:],
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
        fixed_table_name
    )
    return (fix_queries, issue_queries, origin_queries, '')


def process_one_series(inst_infos: List[DicomFileInfo],
                       fx_series_dir: str,
                       mf_series_dir: str,
                       in_gc_info, fx_gc_info, mf_gc_info) -> tuple:
    logger = logging.getLogger(__name__)
    logger.info('\tStart fixing series({}) containing {} instances'.format(
            inst_infos[0].series_uid, len(inst_infos)))
    tic = time.time()
    # Create necessarry folders:
    if not os.path.exists(fx_series_dir):
        os.makedirs(fx_series_dir)
    if not os.path.exists(mf_series_dir):
        os.makedirs(mf_series_dir)
    # Get table neames for populating bigquery tables:
    in_table_name = in_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    # Fix process
    single_frames = []
    fix_threads = ThreadPool(
        min(len(inst_infos), max_number_of_instance_threads), 'instance')
    for obj in inst_infos:
        fx_file = os.path.join(
            fx_series_dir, '{}.dcm'.format(obj.instance_uid))
        fx_obj = DicomFileInfo(
            fx_gc_info.Bucket.ProjectID, fx_gc_info.Bucket.Dataset,
            '', fx_file, '', '', '')
        fix_threads.queue.put(
            (
                fix_one_instance,
                (
                    obj,
                    fx_obj,
                    in_table_name, fx_table_name
                )
            )
        )
    # wait for all fix threads to finish
    fix_threads.queue.join()
    fix_threads.kill_them_all()
    toc = time.time()
    t_e = '{}'.format(str(timedelta(seconds=toc - tic)))
    # Log some information
    speed_str = ctools.get_human_readable_string(
        len(inst_infos) / (toc - tic)
        )
    logger.info(
        'finished fixing series<{}>: {} '
        'instances in {} sec ({}inst/sec)'.format(
            inst_infos[0].series_uid, len(inst_infos), t_e, speed_str))
    # collect outputs
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    blob_file_pair = []
    fx_blob_form = '{}/dicom/{{}}/{{}}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject)
    success = True
    for args, (fix_q, iss_q, org_q, flaw) in fix_threads.output:
        success = success and (flaw == '')
        flaw_queries.append(flaw)
        fix_queries.extend(fix_q)
        issue_queries.extend(iss_q)
        origin_queries.extend(org_q)
        fx_file_info = args[1]
        fx_file_info.blob_address = fx_blob_form.format(
            fx_file_info.study_uid, fx_file_info.series_uid,
            fx_file_info.instance_uid)
        blob_file_pair.append(fx_file_info)
        single_frames.append(fx_file_info.file_path)
    if not success:
        logger.info(
            'series <{}> encountered a problem while fi'
            'xing so the conversion is going to be aborted',)
        return ([], [], [], [], flaw_queries)
    # Now I want to convert the fix series:
    tic = time.time()
    mf_log = []
    PrntChld = conv.ConvertByHighDicomNew(
            single_frames, mf_series_dir, mf_log)
    for pr_ch in PrntChld:
        origin_queries.extend(pr_ch.GetQuery(in_table_name, fx_table_name))
        multiframe_log = []
        VER(pr_ch.child_dicom_file, multiframe_log)
        mf_issues = IssueCollection(
            multiframe_log[1:], mf_table_name,
            pr_ch.child_study_instance_uid,
            pr_ch.child_series_instance_uid,
            pr_ch.child_sop_instance_uid,)
        issue_queries.extend(mf_issues.GetQuery())
        mf_blob_path = '{}/dicom/{}/{}/{}.dcm'.format(
                mf_gc_info.Bucket.DataObject,
                pr_ch.child_study_instance_uid,
                pr_ch.child_series_instance_uid,
                pr_ch.child_series_instance_uid
            )
        blob_file_pair.append(DicomFileInfo(
            mf_gc_info.Bucket.ProjectID,
            mf_gc_info.Bucket.Dataset,
            mf_blob_path, pr_ch.child_dicom_file,
            pr_ch.child_study_instance_uid,
            pr_ch.child_series_instance_uid,
            pr_ch.child_sop_instance_uid
        ))
    toc = time.time()
    # Now I'm logging the conversion process:
    speed_str = ctools.get_human_readable_string(
        len(inst_infos) / (toc - tic))
    t_e = '{}'.format(str(timedelta(seconds=toc - tic)))
    logger.info(
        '\tfinished conversion to MF series<{}>: {} '
        'instances in {} sec ({}inst/sec)'.format(
            inst_infos[0].series_uid, len(PrntChld),  t_e, speed_str))
    return (fix_queries, issue_queries, origin_queries, blob_file_pair, [])


def down_up_load_files_form_google_cloud(blob_file_pairs: List[DicomFileInfo],
                                         download: bool = True):
    if download:
        prifix = 'dn-load'
        function = download_blob
    else:
        prifix = 'up-load'
        function = upload_blob
    load_threads = ThreadPool(
        min(max_number_of_up_down_load_threads, len(blob_file_pairs)), prifix)
    blob_dict = {}
    for obj in blob_file_pairs:
        blob_dict[obj.blob_address] = obj
        load_threads.queue.put(
            (
                function,
                (
                    obj.project_id,
                    obj.bucket_name,
                    obj.blob_address,
                    obj.file_path
                )
            )
        )
    load_threads.queue.join()
    load_threads.kill_them_all()
    results = []
    for (poj, buck, b, f), (success) in load_threads.output:
        results.append((blob_dict[b], success,))
    return results


def download_bunch_of_studies(blob_file_pairs: List[DicomFileInfo]) -> tuple:
    logger = logging.getLogger(__name__)
    tic = time.time()
    results = down_up_load_files_form_google_cloud(blob_file_pairs)
    toc = time.time()
    # Measrure the download_size:
    # ----------------------------------
    download_elapsed_time = toc - tic
    th_count = min(MAX_NUMBER_OF_THREADS, len(results))
    size_measure = ThreadPool(th_count, "size")
    for bl, success in results:
        if success:
            size_measure.queue.put(
                (
                    lambda x: os.path.getsize(x),
                    (bl.file_path,)
                )
            )
    size_measure.queue.join()
    size_measure.kill_them_all()
    downloaded_size = 0
    for arg, sz in size_measure.output:
        downloaded_size += sz
    logger.info(
        'Study <{}>, {}B in size was downlaoded in {} ({}B\sec)'.format(
            study_uid, ctools.get_human_readable_string(downloaded_size),
            timedelta(seconds=download_elapsed_time),
            ctools.get_human_readable_string(
                downloaded_size / download_elapsed_time)
            )
        )
    # Prepare the output
    # ----------------------------------
    defected_series = []
    flaw_queries = []
    study_series_dict = {}
    for bl, success in results:
        if not success:
            flaw_queries.append(flaw_query_form.format(
                bl.bucket_name, bl.study_uid, bl.series_uid,
                bl.instance_uid, 'DOWNLOAD')
            )
            defected_series.append((bl.study_uid, bl.series_uid,))
        else:
            if bl.study_uid in study_series_dict:
                if bl.series_uid in study_series_dict[bl.study_uid]:
                    study_series_dict[bl.study_uid][bl.series_uid].append(
                        bl)
                else:
                    study_series_dict[
                        bl.study_uid][bl.series_uid] = [bl]
            else:
                study_series_dict[
                    bl.study_uid] = {bl.series_uid: [bl]}
    # I'm going to remove all incomplete series that couldn't download:
    for st_uid, se_uid in defected_series:
        del study_series_dict[st_uid][se_uid]
    return (study_series_dict, flaw_queries,
            PerformanceMeasure(downloaded_size, download_elapsed_time,))


def upload_bunch_of_studies(blob_file_pairs: List[DicomFileInfo]) -> list:
    logger = logging.getLogger(__name__)
    tic = time.time()
    results = down_up_load_files_form_google_cloud(
        blob_file_pairs, False)
    toc = time.time()
    # Measrure the upload_size:
    # ----------------------------------
    upload_elapsed_time = toc - tic
    th_count = min(MAX_NUMBER_OF_THREADS, len(results))
    size_measure = ThreadPool(th_count, "size")
    for blob_info, success in results:
        if success:
            size_measure.queue.put(
                (
                    lambda x: os.path.getsize(x),
                    (blob_info.file_path,)
                )
            )
    size_measure.queue.join()
    size_measure.kill_them_all()
    uploaded_size = 0
    for arg, sz in size_measure.output:
        uploaded_size += sz 
    logger.info(
        'Study <{}>, {}B in size was uplaoded in {} ({}B\sec)'.format(
            study_uid, ctools.get_human_readable_string(uploaded_size),
            timedelta(seconds=upload_elapsed_time),
            ctools.get_human_readable_string(
                uploaded_size / upload_elapsed_time)
            )
        )
    # Prepare the output
    # ----------------------------------
    flaw_queries = []
    for blob_file_info, success in results:
        if not success:
            flaw_queries.append(flaw_query_form.format(
                blob_file_info.bucket_name, blob_file_info.study_uid,
                blob_file_info.series_uid, blob_file_info.instance_uid,
                'UPLOAD')
            )
    return (flaw_queries,
            PerformanceMeasure(uploaded_size, upload_elapsed_time))


def process_bunche_of_studies(in_folder: str, studies_chunk: List[Tuple],
                              in_gc_info, fx_gc_info, mf_gc_info,
                              max_number: int = 2**63 - 1) -> int:
    logger = logging.getLogger(__name__)
    number_of_inst_in_study = 0
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
        study_local_folder = os.path.join(
                in_folder, study_uid)
        study_local_folders.append(study_local_folder)
        for number_of_series, (series_uid, instances) in\
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
            for number_of_inst, instance_uid in enumerate(instances, 1):
                if number_of_inst > max_number_of_instances:
                    break
                blob_address = blob_address_pattern.format(
                    study_uid, series_uid, instance_uid
                )
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
                        instance_uid
                    ))
    # --> Starting download
    # -------------------------------
    downloaded_files, defected_queries, download_measure =\
        download_bunch_of_studies(
            input_blob_file_pairs)
    # --> Fix and convert all  downloaded files
    # -------------------------------
    tic = time.time()
    series_threads = ThreadPool(
        min(max_number_of_series_threads, len(downloaded_files)), 'fix')
    for study_uid, downloaded_series in downloaded_files.items():    
        for series_uid, instance_info in downloaded_series.items():
            fx_series_folder = os.path.join(
                    study_local_folder,
                    '{}/{}'.format(fx_sub_dir, series_uid))
            mf_series_folder = os.path.join(
                    study_local_folder,
                    '{}/{}'.format(mf_sub_dir, series_uid))
            series_threads.queue.put(
                (
                    process_one_series,
                    (
                        instance_info,
                        fx_series_folder,
                        mf_series_folder,
                        in_gc_info, fx_gc_info, mf_gc_info
                    )
                )
            )
            number_of_inst_in_study += len(instance_info)
    series_threads.queue.join()
    series_threads.kill_them_all()
    toc = time.time()
    process_measure = PerformanceMeasure(number_of_inst_in_study, toc - tic)
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    blob_file_pairs = []
    for args, (fix_q, iss_q, org_q, bl_f_pairs, flaw_q) in\
            series_threads.output:
        fix_queries.extend(fix_q)
        issue_queries.extend(iss_q)
        origin_queries.extend(org_q)
        flaw_queries.extend(flaw_q)
        blob_file_pairs.extend(bl_f_pairs)
    # --> Multithread uploading the data
    # -------------------------------
    upload_flawed_queries, upload_measure = upload_bunch_of_studies(
        blob_file_pairs)
    flaw_queries.extend(upload_flawed_queries)
    # --> Populate big query tables:
    # -------------------------------
    dataset_id = '{}.{}'.format(
        fx_gc_info.BigQuery.ProjectID,
        fx_gc_info.BigQuery.Dataset)
    big_q_threads = ThreadPool(max_number_of_bq_threads, 'BQ')
    tic = time.time()
    all_rows = (len(fix_queries) + len(issue_queries) + len(origin_queries) +
                len(flaw_queries))
    if len(fix_queries) != 0:
        BuildQueries_parallel(
            FixCollection.GetQueryHeader(),
            fix_queries,
            dataset_id, False,
            big_q_threads
            )
    if len(issue_queries) != 0:
        BuildQueries_parallel(
            IssueCollection.GetQueryHeader(),
            issue_queries,
            dataset_id, False,
            big_q_threads
            )
    if len(origin_queries) != 0:
        BuildQueries_parallel(
            conv.ParentChildDicoms.GetQueryHeader(),
            origin_queries,
            dataset_id, False,
            big_q_threads
            )
    if len(flaw_queries) != 0:
        BuildQueries_parallel(
            "INSERT INTO `{0}`.DEFECTED VALUES {1};",
            flaw_queries,
            dataset_id, False,
            big_q_threads
            )
    big_q_threads.queue.join()
    big_q_threads.kill_them_all()
    toc = time.time()
    elapsed_time = timedelta(seconds=toc - tic)
    big_query_measure = PerformanceMeasure(all_rows, toc - tic)
    logger.info(
        'Big query tables were populated'
        ' successfully. Time elapse: {}'.format(elapsed_time))
    rm(study_local_folders)
    return ProcessPerformance(
                download_measure, upload_measure,
                process_measure, big_query_measure)


def rm(folders):
    # print(folders)
    if type(folders) == str:
        folders = (folders,)
    for a in folders:
        if os.path.exists(a):
            logging.info(' XXX -> REMOVING FOLDER {}'.format(a))
            shutil.rmtree(a)
        else:
            logging.info("FOLDER {} DOESN'T EXIST TO BE ROMOVED".format(a))


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
general_dataset_name = 'afshin_results_02_' + in_dicoms.BigQuery.Dataset
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
CreateDicomStore(
    fx_dicoms.DicomStore.ProjectID,
    fx_dicoms.DicomStore.CloudRegion,
    fx_dicoms.DicomStore.Dataset,
    fx_dicoms.DicomStore.DataObject)
CreateDicomStore(
    mf_dicoms.DicomStore.ProjectID,
    mf_dicoms.DicomStore.CloudRegion,
    mf_dicoms.DicomStore.Dataset,
    mf_dicoms.DicomStore.DataObject)
create_bucket(
    fx_dicoms.Bucket.ProjectID,
    fx_dicoms.Bucket.Dataset,
    False)
create_bucket(
    mf_dicoms.Bucket.ProjectID,
    mf_dicoms.Bucket.Dataset,
    False)
max_number = 2**63 - 1
# max_number = 3
if max_number < 2**63 - 1:
    limit_q = 'LIMIT 50000'
else:
    limit_q = ''
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
""".format(in_dicoms.BigQuery.GetBigQueryStyleAddress(), limit_q,
           BigQueryInputCollectionInfo.GetBigQueryStyleAddress())
uids: dict = {}
q_dataset_uid = '{}.{}.{}'.format(
    in_dicoms.BigQuery.ProjectID,
    in_dicoms.BigQuery.Dataset,
    in_dicoms.BigQuery.DataObject
    )
logger = logging.getLogger(__name__)
max_number_of_studies = max_number
time_interval_for_progress_update = 1
last_time_point_for_progress_update = 0
start = time.time()
analysis_started = False
studies = query_string_with_result(study_query)
number_of_all_inst = studies.total_rows
number_of_inst_processed = 1
logger.info('Starting {} active threads'.format(max_number_of_threads))
q = Queue()
for ii in range(max_number_of_study_threads):
    t = StudyThread(q, name='afn_th{:02d}'.format(ii))
    t.daemon = True
    t.start()
if studies is not None:
    for row in studies:
        stuid = row.STUDYINSTANCEUID
        seuid = row.SERIESINSTANCEUID
        sopuid = row.SOPINSTANCEUID
        cln_id = row.GCS_Bucket
        if stuid in uids:
            if seuid in uids[stuid][1]:
                uids[stuid][1][seuid].append(sopuid)
            else:
                uids[stuid][1][seuid] = [sopuid]
        else:
            uids[stuid] = (cln_id, {seuid: [sopuid]})
    StudyThread.number_of_all_studies = min(len(uids), max_number_of_studies)
    StudyThread.number_of_all_instances = number_of_all_inst
    study_chunk_count = 10
    study_chunk = []
    for number_of_studies, (study_uid, sub_study) in enumerate(uids.items(), 1):
        if number_of_studies > max_number_of_studies:
            break
        study_chunk.append((study_uid, sub_study[0], sub_study[1]))
        if number_of_studies % study_chunk_count == 0 or\
                number_of_studies == len(uids) or \
                number_of_studies == max_number_of_studies:
            q.put(
                (
                    process_bunche_of_studies,
                    (
                        local_tmp_folder,
                        study_chunk,
                        in_dicoms, fx_dicoms, mf_dicoms,
                        max_number
                    )
                )
            )
            study_chunk = []
q.join()  # waiting for all tasks to be done
rm(local_tmp_folder)
import_dicom_bucket(
    fx_dicoms.DicomStore.ProjectID,
    fx_dicoms.DicomStore.CloudRegion,
    fx_dicoms.DicomStore.Dataset,
    fx_dicoms.DicomStore.DataObject,
    fx_dicoms.Bucket.ProjectID,
    fx_dicoms.Bucket.Dataset,
    fx_dicoms.Bucket.DataObject
    )
import_dicom_bucket(
    mf_dicoms.DicomStore.ProjectID,
    mf_dicoms.DicomStore.CloudRegion,
    mf_dicoms.DicomStore.Dataset,
    mf_dicoms.DicomStore.DataObject,
    mf_dicoms.Bucket.ProjectID,
    mf_dicoms.Bucket.Dataset,
    mf_dicoms.Bucket.DataObject
    )
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
