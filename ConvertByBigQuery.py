import shutil
from pydicom.uid import generate_uid
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
from highdicom.legacy.sop import FrameSetCollection
from DicomStoreStuff import (
    create_dataset, exists_dataset, exists_dicom_store, create_dicom_store,
    import_dicom_bucket, export_dicom_instance_bigquery)
from parallelization import (ProcessPool, MAX_NUMBER_OF_THREADS,
                             install_mp_handler)
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
max_number_of_study_processes = 1
max_number_of_fix_processes = MAX_NUMBER_OF_THREADS
max_number_of_up_down_load_processes = MAX_NUMBER_OF_THREADS
max_number_of_bq_processes = MAX_NUMBER_OF_THREADS
max_number_of_frameset_processes = MAX_NUMBER_OF_THREADS
max_number_of_conversion_processes = MAX_NUMBER_OF_THREADS

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
    logger_config_dict = json.load(json_file)
dt_string = datetime.now().strftime("[%d-%m-%Y][%H-%M-%S]")
file_name = './Logs/log{}.log'.format(dt_string)
folder = os.path.dirname(file_name)
if not os.path.exists(folder):
    os.makedirs(folder)
logger_config_dict["handlers"]['file']['filename'] = file_name
with open('log_config.json', 'w') as json_file:
    json.dump(logger_config_dict, json_file, indent=4)
logging.config.dictConfig(logger_config_dict)
install_mp_handler()
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
    return ds


def BuildQueries(header: str, qs: list, dataset_id: str,
                 return_: bool = True, processes: ProcessPool = None) -> list:
    logger = logging.getLogger(__name__)
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
            if processes is None:
                query_string(out_q[-1], table_name)
            else:
                logger.info('putting in queue')
                processes.queue.put(
                    (
                        query_string,
                        (out_q[-1], table_name)
                    )
                )
    out_q.append(header.format(dataset_id, elem_q))
    if processes is None:
        query_string(out_q[-1], table_name)
    else:
        logger.info('putting in queue')
        processes.queue.put(
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
        fx_ds = FixFile(
            inst_info.file_path, fx_inst_info.file_path, fix_log,
            pre_fix_issues,
            post_fix_issues)
        fx_inst_info.study_uid = fx_ds.StudyInstanceUID
        fx_inst_info.sereies_uid = fx_ds.SeriesInstanceUID
        fx_inst_info.instance_uid = fx_ds.SOPInstanceUID
        # as a trick to workaround pickling problem
        fx_inst_info.dicom_ds = {'dataset': fx_ds}
    except BaseException as err:
        logger.error(err, exc_info=True)
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


def frameset_for_one_series(file_blob_pairs: List[DicomFileInfo],
                            series_folder_prifix: str):
    logger = logging.getLogger(__name__)
    # All frames set created out of one series must have the same series
    #   instance uid. So I have to create on sereies instance uid and a
    #   destination folder for future multiframe images
    # ------------------------------------------------
    multi_frame_series_uid = generate_uid()
    multi_frame_series_folder = os.path.join(
        series_folder_prifix,
        multi_frame_series_uid)
    if not os.path.exists(multi_frame_series_folder):
        os.makedirs(multi_frame_series_folder)
    ds_list = []
    for f_bl in file_blob_pairs:
        ds_list.append(f_bl.dicom_ds['dataset'])
    try:
        fs_collection = FrameSetCollection(ds_list)
        fs = fs_collection.FrameSets
    except BaseException as err:
        logger.error(err, exc_info=True)
        fs = []
    return (fs, multi_frame_series_uid, multi_frame_series_folder)


def extract_convert_framesets_for_bunch_of_studies(
        study_series_dict,
        mf_local_study_path: str,
        fx_gc_info, mf_gc_info) -> tuple:
    # Now I want to extract framesets from fixed sereis:
    logger = logging.getLogger(__name__)
    logger.info('Start finding the framesets')
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleAddress(False)
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
                        study_folder
                    )
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
    for (file_blob_pairs, prefix),\
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
                mf_instace_uid = generate_uid()
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
                            mf_instace_uid
                        )
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
                pr_ch.child_sop_instance_uid,)
            issue_queries.extend(mf_issues.GetQuery())
            mf_blob_path = '{}/dicom/{}/{}/{}.dcm'.format(
                    mf_gc_info.Bucket.DataObject,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_series_instance_uid
                )
            upload_blobfile_pairs.append(DicomFileInfo(
                mf_gc_info.Bucket.ProjectID,
                mf_gc_info.Bucket.Dataset,
                mf_blob_path, pr_ch.child_dicom_file,
                pr_ch.child_study_instance_uid,
                pr_ch.child_series_instance_uid,
                pr_ch.child_sop_instance_uid
            ))
    frameset_perf = PerformanceMeasure(
        number_of_all_framesets, frameset_elapsed_time, '(frameset)')
    mf_perf = PerformanceMeasure(
        number_of_all_converted_mf, conversion_elapsed_time,
        '(multiframe-inst)')
    logger.info(
        '\tfinished conversion to multi-frame '
        'instances first {} then {}'.format(str(frameset_perf), str(mf_perf)))
    return (issue_queries, origin_queries, upload_blobfile_pairs, flaw_queries,
            frameset_perf, mf_perf)


def fix_bunch_of_studies(inst_infos: List[DicomFileInfo],
                         fx_local_study_path: str,
                         in_gc_info, fx_gc_info) -> tuple:
    logger = logging.getLogger(__name__)
    logger.info(
        "\tStart fixing bunch of studies containing {} instances".format(
         len(inst_infos))
         )
    tic = time.time()

    # Get table neames for populating bigquery tables:
    in_table_name = in_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    # Fix process
    single_frames = []
    fix_processes = ProcessPool(
        min(len(inst_infos), max_number_of_fix_processes),
        'instance')
    for obj in inst_infos:
        # I'm using downloaded file uids for fix files
        stuyd_folder = fx_local_study_path.format(obj.study_uid)
        fx_file = '{}/{}/{}.dcm'.format(
            stuyd_folder, obj.series_uid, obj.instance_uid)
        fx_obj = DicomFileInfo(
            fx_gc_info.Bucket.ProjectID, fx_gc_info.Bucket.Dataset,
            '', fx_file, obj.study_uid, obj.series_uid, obj.study_uid)
        fix_processes.queue.put(
            (
                fix_one_instance,
                (
                    obj,
                    fx_obj,
                    in_table_name, fx_table_name
                )
            )
        )
    # wait for all fix processes to finish
    fix_processes.queue.join()
    fix_processes.kill_them_all()
    toc = time.time()
    t_e = '{}'.format(str(timedelta(seconds=toc - tic)))
    performance = PerformanceMeasure(len(inst_infos), toc - tic)
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
    study_series_dict = {}
    defected_study_series = []
    fx_blob_form = '{}/dicom/{{}}/{{}}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject)
    for args, (fix_q, iss_q, org_q, flaw) in fix_processes.output:
        fx_file_info = args[1]
        if flaw == '':
            fix_queries.extend(fix_q)
            issue_queries.extend(iss_q)
            origin_queries.extend(org_q)
            fx_file_info.blob_address = fx_blob_form.format(
                fx_file_info.study_uid, fx_file_info.series_uid,
                fx_file_info.instance_uid)
            # All instances must be organized for conversion process and flawed 
            # series to be removed
            single_frames.append(fx_file_info)
        else:
            flaw_queries.append(flaw)
            defected_study_series.append(
                (fx_file_info.study_uid, fx_file_info.series_uid))
    study_series_dict, st_count, se_count, inst_count =\
        organiase_file_blob_infos(single_frames)
    for study, series in defected_study_series:
        logger.info(
            'series \n-\t\t<{}>.<{}>\-\t\t encountered a problem while fi'
            'xing so the conversion is going to be aborted'.format(
                study, series))
        if study in study_series_dict:
            if series in study_series_dict[study]:
                del study_series_dict[study][series]
    return (fix_queries, issue_queries,
            origin_queries, study_series_dict, flaw_queries, performance)


def down_up_load_files_form_google_cloud(blob_file_pairs: List[DicomFileInfo],
                                         download: bool = True):
    if download:
        prifix = 'dn-load'
        function = download_blob
    else:
        prifix = 'up-load'
        function = upload_blob
    load_processes = ProcessPool(
        min(max_number_of_up_down_load_processes, len(blob_file_pairs)),
        prifix)
    blob_dict = {}
    for obj in blob_file_pairs:
        blob_dict[obj.blob_address] = obj
        load_processes.queue.put(
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
    load_processes.queue.join()
    load_processes.kill_them_all()
    results = []
    for (poj, buck, b, f), (success) in load_processes.output:
        results.append((blob_dict[b], success,))
    return results


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
    return (output, st_count, se_count, inst_count)


def download_bunch_of_studies(blob_file_pairs: List[DicomFileInfo]) -> tuple:
    logger = logging.getLogger(__name__)
    tic = time.time()
    results = down_up_load_files_form_google_cloud(blob_file_pairs)
    toc = time.time()
    # Measrure the download_size:
    # ----------------------------------
    download_elapsed_time = toc - tic
    pr_count = min(max_number_of_up_down_load_processes, len(results))
    size_measure = ProcessPool(pr_count, "size")
    for bl, success in results:
        if success:
            size_measure.queue.put(
                (
                    os.path.getsize,
                    (bl.file_path,)
                )
            )
    size_measure.queue.join()
    size_measure.kill_them_all()
    downloaded_size = 0
    for arg, sz in size_measure.output:
        downloaded_size += sz
    # Prepare the output
    # ----------------------------------
    # defected_series = []
    # flaw_queries = []
    # study_series_dict = {}
    # for bl, success in results:
    #     if not success:
    #         flaw_queries.append(flaw_query_form.format(
    #             bl.bucket_name, bl.study_uid, bl.series_uid,
    #             bl.instance_uid, 'DOWNLOAD')
    #         )
    #         defected_series.append((bl.study_uid, bl.series_uid,))
    #     else:
    #         if bl.study_uid in study_series_dict:
    #             if bl.series_uid in study_series_dict[bl.study_uid]:
    #                 study_series_dict[bl.study_uid][bl.series_uid].append(
    #                     bl)
    #             else:
    #                 study_series_dict[
    #                     bl.study_uid][bl.series_uid] = [bl]
    #         else:
    #             study_series_dict[
    #                 bl.study_uid] = {bl.series_uid: [bl]}
    # # I'm going to remove all incomplete series that couldn't download:
    # for st_uid, se_uid in defected_series:
    #     del study_series_dict[st_uid][se_uid]
    # return (study_series_dict, flaw_queries,
    #         PerformanceMeasure(downloaded_size, download_elapsed_time,))
    defected_series = []
    downloaded_blobs = []
    flaw_queries = []
    for bl, success in results:
        if not success:
            flaw_queries.append(flaw_query_form.format(
                bl.bucket_name, bl.study_uid, bl.series_uid,
                bl.instance_uid, 'DOWNLOAD')
            )
            defected_series.append((bl.study_uid, bl.series_uid,))
        else:
            downloaded_blobs.append(bl)
    return (downloaded_blobs, flaw_queries,
            PerformanceMeasure(downloaded_size, download_elapsed_time,))


def fix_conver_one_series(inst_infos: List[DicomFileInfo],
                          fx_local_study_path: str,
                          mf_local_study_path: str,
                          in_gc_info, fx_gc_info, mf_gc_info) -> tuple:
    in_table_name = in_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    single_frames = []
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    defected_study_series = []
    upload_blobfile_pairs = []
    fx_blob_form = '{}/dicom/{{}}/{{}}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject)
    for obj in inst_infos:
        # I'm using downloaded file uids for fix files
        stuyd_folder = fx_local_study_path.format(obj.study_uid)
        fx_file = '{}/{}/{}.dcm'.format(
            stuyd_folder, obj.series_uid, obj.instance_uid)
        fx_obj = DicomFileInfo(
            fx_gc_info.Bucket.ProjectID, fx_gc_info.Bucket.Dataset,
            '', fx_file, obj.study_uid, obj.series_uid, obj.study_uid)
        (fix_q, iss_q, org_q, flaw) = fix_one_instance(
            obj,
            fx_obj,
            in_table_name, fx_table_name
        )
        if flaw == '':
            fix_queries.extend(fix_q)
            issue_queries.extend(iss_q)
            origin_queries.extend(org_q)
            single_frames.append(fx_obj)
            fx_obj.blob_address = fx_blob_form.format(
                fx_obj.study_uid, fx_obj.series_uid,
                fx_obj.instance_uid)
        else:
            flaw_queries.append(flaw)
            defected_study_series.append(
                (fx_obj.study_uid, fx_obj.series_uid))
    # The code is not gonna proceed to conversion if there is any fix issue
    if len(flaw_queries) != 0:
        return ([], [], [], [], flaw_queries, 0, 0)
    # Now I want to extract framesets from fixed sereis:
    study_uid = inst_infos[0].study_uid
    study_folder = mf_local_study_path.format(study_uid)
    (fsets, mf_series_uid, mf_series_dir) = frameset_for_one_series(
        single_frames,
        study_folder
    )
    number_of_all_converted_mf = 0
    if len(fsets) == 0:
        for file_blob in single_frames:
            f_query = flaw_query_form.format(
                file_blob.bucket_name, file_blob.study_uid,
                file_blob.series_uid, file_blob.instance_uid, 'FRAMESET')
            flaw_queries.append(f_query)
    else:
        mf_study_uid = single_frames[0].study_uid
        for fset in fsets:
            # remove ds from single frome for multi_processing purpose
            for bl_f in single_frames:
                bl_f.dicom_ds = None
            upload_blobfile_pairs.extend(single_frames)
            mf_instace_uid = generate_uid()
            mf_file_path = os.path.join(
                mf_series_dir, '{}.dcm'.format(mf_instace_uid))
            pr_ch = conv.ConvertFrameset(
                fset,
                mf_file_path,
                mf_study_uid,
                mf_series_uid,
                mf_instace_uid
            )
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
                number_of_all_converted_mf += 1
                origin_queries.extend(
                    pr_ch.GetQuery(fx_table_name, mf_table_name))
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
                upload_blobfile_pairs.append(DicomFileInfo(
                    mf_gc_info.Bucket.ProjectID,
                    mf_gc_info.Bucket.Dataset,
                    mf_blob_path, pr_ch.child_dicom_file,
                    pr_ch.child_study_instance_uid,
                    pr_ch.child_series_instance_uid,
                    pr_ch.child_sop_instance_uid
                ))

    return (fix_queries, issue_queries, origin_queries,
            upload_blobfile_pairs, flaw_queries,
            len(fsets), number_of_all_converted_mf)


def fix_convert_bunch_of_studies(inst_infos: List[DicomFileInfo],
                                 fx_local_study_path: str,
                                 mf_local_study_path: str,
                                 in_gc_info, fx_gc_info, mf_gc_info):
    logger = logging.getLogger(__name__)
    logger.info(
        "\tStart (fix+convert)ing bunch of studies containing {} instances".format(
         len(inst_infos))
         )
    study_series_dict, st_count, se_count, inst_count =\
        organiase_file_blob_infos(inst_infos)
    tic = time.time()
    number_of_processes = min(max_number_of_fix_processes, se_count)
    processes = ProcessPool(number_of_processes, 'fx+conv')
    for stuy_uid, study_content in study_series_dict.items():
        for sreies_uid, curretn_file_blobs in study_content.items():
            processes.queue.put(
                (
                    fix_conver_one_series,
                    (
                        curretn_file_blobs, fx_local_study_path,
                        mf_local_study_path,
                        in_gc_info, fx_gc_info, mf_gc_info)
                )
            )
    processes.queue.join()
    processes.kill_them_all()
    toc = time.time()
    results = processes.output
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    upload_blobfile_pairs = []
    framesets_in_bunch = 0
    mfs_in_bunch = 0
    for args, outs in results:
        (
            fx_qr, iss_qr, orig_qr,
            blobfile_pairs, flaw_qr,
            number_of_framesets,
            number_of_all_converted_mf
        ) = outs
        fix_queries.extend(fx_qr)
        issue_queries.extend(iss_qr)
        origin_queries.extend(orig_qr)
        flaw_queries.extend(flaw_qr)
        upload_blobfile_pairs.extend(blobfile_pairs)
        framesets_in_bunch += number_of_framesets
        mfs_in_bunch += number_of_all_converted_mf
    fx_perf = PerformanceMeasure(inst_count, toc - tic, '(inst)')
    frameset_perf = PerformanceMeasure(
        framesets_in_bunch, toc - tic, '(frameset)')
    mf_perf = PerformanceMeasure(mfs_in_bunch, toc - tic, '(mf)')
    logger.info("\tFinished (fix+convert)ing bunch of studies:")
    logger.info("\t\t\tFixes                 -> {}".format(fx_perf))
    logger.info("\t\t\tFrmeset extraction    -> {}".format(frameset_perf))
    logger.info("\t\t\tMultiframe conversion -> {}".format(mf_perf))
    return (fix_queries, issue_queries, origin_queries, flaw_queries,
            upload_blobfile_pairs, fx_perf, frameset_perf, mf_perf)


def download_fix_convert_upload_one_sereis(
        inst_infos: list,
        fx_local_study_path: str,
        mf_local_study_path: str,
        in_gc_info, fx_gc_info, mf_gc_info):
    if len(inst_infos) <= 1:
        return ([], [], [], [], 0, 0, 0, 0, 0, 0)
    in_table_name = in_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    fx_table_name = fx_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    mf_table_name = mf_gc_info.BigQuery.GetBigQueryStyleAddress(False)
    single_frames = []
    issue_queries = []
    fix_queries = []
    origin_queries = []
    flaw_queries = []
    defected_study_series = []
    downloaded_files_size = 0
    fixed_files_size = 0
    mf_files_size = 0
    upload_files_size = 0

    fx_blob_form = '{}/dicom/{{}}/{{}}/{{}}.dcm'.format(
        fx_gc_info.Bucket.DataObject)
    for obj in inst_infos:
        success = download_blob(
            in_gc_info.Bucket.ProjectID,
            obj.bucket_name,
            obj.blob_address,
            obj.file_path
        )
        downloaded_files_size += os.path.getsize(obj.file_path)
        if not success:
            flaw_queries.append(flaw_query_form.format(
                    obj.bucket_name, obj.study_uid,
                    obj.series_uid, obj.instance_uid,
                    'DOWNLOAD')
                )
            return ([], [], [], flaw_queries, 0, 0,
                    downloaded_files_size, fixed_files_size,
                    mf_files_size, upload_files_size)
        # I'm using downloaded file uids for fix files
        stuyd_folder = fx_local_study_path.format(obj.study_uid)
        fx_file = '{}/{}/{}.dcm'.format(
            stuyd_folder, obj.series_uid, obj.instance_uid)
        fx_obj = DicomFileInfo(
            fx_gc_info.Bucket.ProjectID, fx_gc_info.Bucket.Dataset,
            '', fx_file, obj.study_uid, obj.series_uid, obj.study_uid)
        (fix_q, iss_q, org_q, flaw) = fix_one_instance(
            obj,
            fx_obj,
            in_table_name, fx_table_name
        )
        if flaw == '':
            fix_queries.extend(fix_q)
            issue_queries.extend(iss_q)
            origin_queries.extend(org_q)
            single_frames.append(fx_obj)
            fx_obj.blob_address = fx_blob_form.format(
                fx_obj.study_uid, fx_obj.series_uid,
                fx_obj.instance_uid)
            success = upload_blob(
                fx_gc_info.Bucket.ProjectID,
                fx_gc_info.Bucket.Dataset,
                fx_obj.blob_address,
                fx_file
            )
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
            defected_study_series.append(
                (fx_obj.study_uid, fx_obj.series_uid))
    # The code is not gonna proceed to conversion if there is any fix issue
    if len(flaw_queries) != 0:
        return ([], [], [], flaw_queries, 0, 0,
                downloaded_files_size, fixed_files_size,
                mf_files_size, upload_files_size)
    # Now I want to extract framesets from fixed sereis:
    study_uid = inst_infos[0].study_uid
    study_folder = mf_local_study_path.format(study_uid)
    (fsets, mf_series_uid, mf_series_dir) = frameset_for_one_series(
        single_frames,
        study_folder
    )
    fx_series_dir = os.path.dirname(single_frames[0].file_path)
    in_series_dir = os.path.dirname(inst_infos[0].file_path)
    number_of_all_converted_mf = 0
    if len(fsets) == 0:
        for file_blob in single_frames:
            f_query = flaw_query_form.format(
                file_blob.bucket_name, file_blob.study_uid,
                file_blob.series_uid, file_blob.instance_uid, 'FRAMESET')
            flaw_queries.append(f_query)
    else:
        mf_study_uid = single_frames[0].study_uid
        for fset in fsets:
            # remove ds from single frome for multi_processing purpose
            for bl_f in single_frames:
                bl_f.dicom_ds = None
            mf_instace_uid = generate_uid()
            mf_file_path = os.path.join(
                mf_series_dir, '{}.dcm'.format(mf_instace_uid))
            pr_ch = conv.ConvertFrameset(
                fset,
                mf_file_path,
                mf_study_uid,
                mf_series_uid,
                mf_instace_uid
            )
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
    return (fix_queries, issue_queries, origin_queries, flaw_queries,
            len(fsets), number_of_all_converted_mf,
            downloaded_files_size, fixed_files_size,
            mf_files_size, upload_files_size)


def process_series_parallel(in_folder: str, studies_chunk: List[Tuple],
                            in_gc_info, fx_gc_info, mf_gc_info,
                            max_number: int = 2**63 - 1) -> ProcessPerformance:
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
            fx_series_local_folder = os.path.join(
                study_local_folder, '{}/{}'.format(
                    fx_sub_dir, series_uid))
            if not os.path.exists(fx_series_local_folder):
                os.makedirs(fx_series_local_folder)
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
    study_series_dict, st_count, se_count, inst_count =\
        organiase_file_blob_infos(input_blob_file_pairs)
    proc_num = min(se_count, max_number_of_fix_processes)
    logger.info('starting {} = min({}, {}) parallel subprocesses'.format(
        proc_num, se_count, max_number_of_fix_processes
    ))
    tic = time.time()
    processes = ProcessPool(proc_num, 'd+f+c+u')
    for study_uid, study_contents in study_series_dict.items():
        for series_uid, series_contents in study_contents.items():
            processes.queue.put(
                (
                    download_fix_convert_upload_one_sereis,
                    (
                        series_contents,
                        '{}{}{}'.format(
                            in_folder, '/{}', '/{}'.format(fx_sub_dir)),
                        '{}{}{}'.format(
                            in_folder, '/{}', '/{}'.format(mf_sub_dir)),
                        in_gc_info, fx_gc_info, mf_gc_info
                    )
                )
            )
    processes.queue.join()
    processes.kill_them_all()
    toc = time.time()
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
    dl_perfs = PerformanceMeasure(downloaded_files_size, toc - tic, 'B')
    fx_perfs = PerformanceMeasure(inst_count, toc - tic, '(inst)')
    frset_perfs = PerformanceMeasure(frameset_number, toc - tic, '(inst)')
    mf_perfs = PerformanceMeasure(multiframe_number, toc - tic, '(inst)')
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
    big_q_processes = ProcessPool(
        max_number_of_bq_processes, 'BQ')
    tic = time.time()
    all_rows = (len(fix_queries) + len(issue_queries) + len(origin_queries) +
                len(flaw_queries))
    if len(fix_queries) != 0:
        BuildQueries(
            FixCollection.GetQueryHeader(),
            fix_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(issue_queries) != 0:
        BuildQueries(
            IssueCollection.GetQueryHeader(),
            issue_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(origin_queries) != 0:
        BuildQueries(
            conv.ParentChildDicoms.GetQueryHeader(),
            origin_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(flaw_queries) != 0:
        BuildQueries(
            "INSERT INTO `{0}`.DEFECTED VALUES {1};",
            flaw_queries,
            dataset_id, False,
            big_q_processes
            )
    big_q_processes.queue.join()
    big_q_processes.kill_them_all()
    toc = time.time()
    big_query_measure = PerformanceMeasure(all_rows, toc - tic, '(row)')
    logger.info(
        'Big query tables were populated'
        ' successfully {}'.format(big_query_measure))
    rm(study_local_folders)
    return ProcessPerformance(
        dl_perfs, fx_perfs, frset_perfs, mf_perfs, ul_perfs, big_query_measure)


def upload_bunch_of_studies(blob_file_pairs: List[DicomFileInfo]) -> list:
    tic = time.time()
    results = down_up_load_files_form_google_cloud(
        blob_file_pairs, False)
    toc = time.time()
    # Measrure the upload_size:
    # ----------------------------------
    upload_elapsed_time = toc - tic
    pr_count = min(MAX_NUMBER_OF_THREADS, len(results))
    size_measure = ProcessPool(pr_count, "size")
    for blob_info, success in results:
        if success:
            size_measure.queue.put(
                (
                    os.path.getsize,
                    (blob_info.file_path)
                )
            )
    size_measure.queue.join()
    size_measure.kill_them_all()
    uploaded_size = 0
    for arg, sz in size_measure.output:
        uploaded_size += sz 
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
            fx_series_local_folder = os.path.join(
                study_local_folder, '{}/{}'.format(
                    fx_sub_dir, series_uid))
            if not os.path.exists(fx_series_local_folder):
                os.makedirs(fx_series_local_folder)
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
    # fx_result = fix_bunch_of_studies(
    #         downloaded_files,
    #         '{}{}{}'.format(
    #             in_folder, '/{}', '/{}'.format(fx_sub_dir)),
    #         in_gc_info, fx_gc_info
    #         )
    # (
    #     fix_queries, issue_queries, origin_queries,
    #     study_series_dict, flaw_queries,
    #     fix_performace) = fx_result
    # mf_result = extract_convert_framesets_for_bunch_of_studies(
    #         study_series_dict,
    #         '{}{}{}'.format(
    #             in_folder, '/{}', '/{}'.format(mf_sub_dir)),
    #         fx_gc_info, mf_gc_info) 
    # (
    #     issue_queries, origin_queries, upload_blobfile_pairs, flaw_queries,
    #     frameset_perf, mf_perf
    # ) = mf_result
    fx_mf_results = fix_convert_bunch_of_studies(
        downloaded_files,
        '{}{}{}'.format(
            in_folder, '/{}', '/{}'.format(fx_sub_dir)),
        '{}{}{}'.format(
            in_folder, '/{}', '/{}'.format(mf_sub_dir)),
        in_gc_info, fx_gc_info, mf_gc_info)
    (
        fix_queries, issue_queries, origin_queries, flaw_queries,
        upload_blobfile_pairs, fix_perf, frameset_perf, mf_perf

    ) = fx_mf_results

    # --> Multiprocess uploading the data
    # -------------------------------
    upload_flawed_queries, upload_measure = upload_bunch_of_studies(
        upload_blobfile_pairs)
    flaw_queries.extend(upload_flawed_queries)
    # --> Populate big query tables:
    # -------------------------------
    dataset_id = '{}.{}'.format(
        fx_gc_info.BigQuery.ProjectID,
        fx_gc_info.BigQuery.Dataset)
    big_q_processes = ProcessPool(
        max_number_of_bq_processes, 'BQ')
    tic = time.time()
    all_rows = (len(fix_queries) + len(issue_queries) + len(origin_queries) +
                len(flaw_queries))
    if len(fix_queries) != 0:
        BuildQueries(
            FixCollection.GetQueryHeader(),
            fix_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(issue_queries) != 0:
        BuildQueries(
            IssueCollection.GetQueryHeader(),
            issue_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(origin_queries) != 0:
        BuildQueries(
            conv.ParentChildDicoms.GetQueryHeader(),
            origin_queries,
            dataset_id, False,
            big_q_processes
            )
    if len(flaw_queries) != 0:
        BuildQueries(
            "INSERT INTO `{0}`.DEFECTED VALUES {1};",
            flaw_queries,
            dataset_id, False,
            big_q_processes
            )
    big_q_processes.queue.join()
    big_q_processes.kill_them_all()
    toc = time.time()
    elapsed_time = timedelta(seconds=toc - tic)
    big_query_measure = PerformanceMeasure(all_rows, toc - tic)
    logger.info(
        'Big query tables were populated'
        ' successfully. Time elapse: {}'.format(elapsed_time))
    rm(study_local_folders)
    return ProcessPerformance(
                download_measure, upload_measure, fix_perf,
                frameset_perf, mf_perf,
                big_query_measure)


def rm(folders, log: bool = True):
    # print(folders)
    if type(folders) == str:
        folders = (folders,)
    for a in folders:
        if os.path.exists(a):
            if log:
                logging.info(' XXX -> REMOVING FOLDER {}'.format(a))
            shutil.rmtree(a)
        else:
            if log:
                logging.info("FOLDER {} DOESN'T EXIST TO BE ROMOVED".format(a))


def main(number_of_processes: int = None):
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
    general_dataset_name = 'afshin_results_03_' + in_dicoms.BigQuery.Dataset
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
    # max_number = 10
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
    # q_dataset_uid = '{}.{}.{}'.format(
    #     in_dicoms.BigQuery.ProjectID,
    #     in_dicoms.BigQuery.Dataset,
    #     in_dicoms.BigQuery.DataObject
    #     )
    logger = logging.getLogger(__name__)
    max_number_of_studies = max_number
    start_time = time.time()
    studies = query_string_with_result(study_query)
    number_of_all_inst = studies.total_rows
    performance_history = []
    number_of_inst_processed = 1
    whole_performace = None
    number_of_st_processed = 1

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
        number_of_all_studies = min(len(uids), max_number_of_studies)
        study_chunk_count = 100
        study_chunk = []
        study_uids = []
        for number_of_studies, (study_uid, sub_study) in enumerate(uids.items(), 1):
            if number_of_studies > max_number_of_studies:
                break
            study_chunk.append((study_uid, sub_study[0], sub_study[1]))
            study_uids.append(study_uid)
            if number_of_studies % study_chunk_count == 0 or\
                    number_of_studies == len(uids) or \
                    number_of_studies == max_number_of_studies:
                try:
                    perf = process_series_parallel(
                        local_tmp_folder,
                        study_chunk,
                        in_dicoms, fx_dicoms, mf_dicoms,
                        max_number
                    )
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
                    number_of_all_inst - number_of_inst_processed
                    ) * time_elapsed / float(number_of_inst_processed)
                header = '{}/{})Study = ({}/{}) instances was fix/'\
                    'convert-ed successfully'.format(
                        number_of_st_processed, number_of_all_studies,
                        number_of_inst_processed, number_of_all_inst
                    )
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
                study_uids = []
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

th = list(range(0, 64, 4))
th = [64]
for nt in th:
    main(nt + 1)
