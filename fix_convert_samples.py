import logging
import logging.config
import os
import pydicom
import shutil
import common.common_tools as ctools
import common.parallelization as pl
import conversion as convtool
from query_anatomy import (
    # FUNCTIONS
    query_anatomy_from_tables,
)
from gcloud.bigquery_tools import (
    # FUNCTIONS
    query_string_with_result,
)
from gcloud.storage_tools import (
    # FUNCTIONS
    download_blob,
    list_blobs,
)
from multiprocessing import (
    # SUBMODULES
    freeze_support,
)
from pydicom.charset import (
    # VARIABLES
    python_encoding,
)
from rightdicom.dcmfix.fix_all import (
    # FUNCTIONS
    fix_dicom,
)
from rightdicom.dcmfix.study_dependent_patches import (
    # FUNCTIONS
    add_anatomy,
)
from rightdicom.dcmvfy.verify import (
    # FUNCTIONS
    verify_dicom,
)
from local_fix_vfy import (
    fix_file_verify_write,
    verify_with_dciodvfy_and_pyvfy)
from query_reference import QueryReferencedStudySequence
from dicom_fix_issue_info import (
    # CLASSES
    DicomFileInfo
)
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': './Logs/sampling_log.log',  # Default is stderr
            "mode": "w",
        },
    },
    'loggers': {
        'xxx': {  # root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    'root': {  # root logger
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': False
        }
}
logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger(__name__)
log.debug("Logging is configured.")
anatomic_attribs = ["ImageLaterality" ,
"BodyPartExamined",
"FrameAnatomySequence",
"AnatomicRegionSequence",]

def download_parallel(project_id: str, bucket_name: str, st_uid: str,
                      se_uid: str, destination_dir: str,
                      process_number: int=pl.MAX_NUMBER_OF_THREADS):
    logger = logging.getLogger(__name__)
    prefix = 'dicom/{}/'.format(st_uid)
    if se_uid != '':
        prefix = '{}{}/'.format(prefix, se_uid)
    bl_names = []
    bl_lists = list_blobs(project_id, bucket_name, prefix)
    for bl in bl_lists:
        bl_names.append(bl.name)
        print(bl.name)
    logger.info('Number of blobs to be downloaded {}'.format(len(bl_names)))
    if len(bl_names) == 0:
        return
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.makedirs(destination_dir)
    ps = pl.ProcessPool(min(len(bl_names), process_number), 'down')
    for i, bl_name in enumerate(bl_names, 1):
        if i > 30:
            break
        file_name = '{:05d}.dcm'.format(i)
        ps.queue.put(
            (
                download_blob,
                (project_id, bucket_name, bl_name, os.path.join(
                    destination_dir, file_name)
                )
            ))
    ps.queue.join()
    ps.kill_them_all()


def GetSeries(keyword: str, value: str):
    if isinstance(value, str):
        value = '"{}"'.format(value)
    study_query = """
                WITH DICOMS AS (
                SELECT STUDYINSTANCEUID, SERIESINSTANCEUID, SOPINSTANCEUID
                FROM {}
                WHERE
                    (SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.2" OR
                    SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.4" OR
                    SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.128") AND
                    {} = {}
                    )
                    SELECT DICOMS.STUDYINSTANCEUID,
                        DICOMS.SERIESINSTANCEUID,
                        DICOMS.SOPINSTANCEUID,
                        COLLECTION_TABLE.GCS_Bucket,
                    FROM DICOMS JOIN
                        {} AS
                        COLLECTION_TABLE ON
                        COLLECTION_TABLE.SOPINSTANCEUID = DICOMS.SOPINSTANCEUID
    """.format(
        '`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_dicom_metadata`',
        keyword, value,
        '`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_auxilliary_metadata`')
    
    studies = query_string_with_result(study_query, project_name='idc-dev-etl')
    stuid = None
    seuid = None
    sopuid = None
    cln_id = None
    if studies is not None:
        for row in studies:
            stuid = row.STUDYINSTANCEUID
            seuid = row.SERIESINSTANCEUID
            sopuid = row.SOPINSTANCEUID
            cln_id = row.GCS_Bucket
            break
    return (stuid, seuid, sopuid, cln_id)


def fix_convert_series(attribute:str , value):
    project_id = 'idc-tcia'
    in_folders = ['../Tmp/in']
    out_folders = '../Tmp/out'
    out_folders = os.path.realpath(out_folders)
    study_uid, series_uid, instance_uid, bucket_name = GetSeries(
        attribute, value)
    # bucket_name = 'idc-tcia-tcga-blca'
    # study_uid = '1.3.6.1.4.1.14519.5.2.1.6354.4016.292170230498352399648594035286'
    # series_uid = '1.3.6.1.4.1.14519.5.2.1.6354.4016.316228581410299389630475076825'
    # instance_uid = '1.3.6.1.4.1.14519.5.2.1.6354.4016.161670751003027974162100121182'
    in_folders[0] = '{}/{}/{}'.format(in_folders[0], study_uid, series_uid)
    log = []
    log_ver = []
    fix_: bool = True
    download_ : bool = False
    ref_info = QueryReferencedStudySequence(
            'canceridc-data.idc_views.dicom_all')
    anatomy_info = query_anatomy_from_tables(
        'canceridc-data.idc_views.dicom_all')
    empty_anatomy = (None, (None, None, None))
    anatomy = empty_anatomy if study_uid not in anatomy_info else\
        anatomy_info[study_uid]
    for i in range(0, len(in_folders)):
        in_folder = os.path.realpath(in_folders[i])
        if download_:
            download_parallel(
                project_id, bucket_name, study_uid, series_uid, in_folder, 16)
        out_folder = os.path.join(out_folders, str(i + 1))
        if os.path.exists(out_folder):
            shutil.rmtree(out_folder)
        os.makedirs(out_folder)
        fix_folder = os.path.join(out_folder, 'fixed')
        if not os.path.exists(fix_folder):
            os.makedirs(fix_folder)
        in_files = ctools.Find(
            in_folder, max_depth = 1, cond_function=ctools.is_dicom)
        if fix_:
            for i, ff in enumerate(in_files):
                fx_log = []
                base = os.path.basename(ff)
                base_wo_ext = base[:-4] if base.endswith('.dcm') else base
                if i % 10 == 0:
                    print('{}/{}) {}'.format(i, len(in_files), base))
                if i == 0:
                    fix_output = fix_file_verify_write(
                        ff, os.path.join(fix_folder, base),
                        anatomy,
                        ref_info,
                        os.path.join(out_folder, base_wo_ext +"_fixrpt.txt"),
                        os.path.join(out_folder, 'pre' + base_wo_ext +"_vfy.txt"),
                        os.path.join(out_folder, 'post' + base_wo_ext +"_vfy.txt"),
                        )
                    char_set = DicomFileInfo.get_charset_val_from_dataset(
                        fix_output[0])
                else:
                    fix_output = fix_file_verify_write(
                        ff, os.path.join(fix_folder, base),
                        anatomy,
                        ref_info
                        )

                (
                    fx_ds, fix_report, pre_rawlog,
                    pre_orglog, pre_pylog,
                    post_rawlog, post_orglog, post_pylog
                ) = fix_output
                # ds = FixFile(ff, os.path.join(fix_folder, base), fx_log, [], [])

                # try:
                fx_files = ctools.Find(fix_folder, max_depth=1,
                                                cond_function=ctools.is_dicom)
                
        else:
            fx_files = in_files
            fix_folder = in_folder
        print('before coversion')
        SOPClassList = convtool.ConvertByHighDicomNew(fix_folder, out_folder)
        for n, f in enumerate(SOPClassList, 0):
            output_file_pattern = "hd{:03d}.dcm"
            new_name = os.path.join(out_folder, output_file_pattern.format(n))
            os.rename(f.child_dicom_file, new_name)
        files = ctools.Find(out_folder, 1, lambda x: x.endswith('.dcm'))
        print(fx_files[0])
        for f in files:
            f_name = os.path.basename(f)
            if f_name.endswith('.dcm'):
                f_name = f_name[: -4]
            verify_with_dciodvfy_and_pyvfy(
                f, char_set,
                os.path.join(out_folder, f_name + '_vfy.txt'))

if __name__ == '__main__':
    freeze_support()
    sopuids = [
        '1.3.6.1.4.1.14519.5.2.1.8421.4010.516731121903255199504736458533', 
    ]
    for i, uid in enumerate(sopuids, 1):
        print('{}/{}) {}'.format(i, len(sopuids), uid))
        fix_convert_series('SOPINSTANCEUID', uid)