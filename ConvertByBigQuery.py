import git
import shutil
from pydicom import *
import pydicom.datadict as Dic
import pydicom.dataelem as Elm
import pydicom.sequence as Seq
from pydicom import uid
import re
from condn_cc import *
from dicom_prechecks import *
import os
from numpy import *
from fix_frequent_errors import *
import curses.ascii
from verify import *
import pydicom.charset
import subprocess
import PrivateDicFromDavid
import os
import xlsxwriter
import time
from datetime import timedelta
import common_tools as ctools
import conversion as conv
import json
from datetime import datetime
from BigQueryStuff import create_all_tables,\
                          query_string,\
                          query_string_with_result
                          
from DicomStoreStuff import list_dicom_stores,\
                            create_dicom_store,\
                            create_dataset,\
                            import_dicom_instance,\
                            export_dicom_instance_bigquery,\
                            exists_dicom_store,\
                            exists_dataset
from DicomWebStuff import dicomweb_retrieve_instance,\
                          dicomweb_store_instance,\
                          _BASE_URL

# Logger setup --------------------------------------------------------
import logging
import logging.config
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


class Datalet:

    def __init__(self, project_id: str,
                 cloud_region: str,
                 dataset: str,
                 dataobject: str):
        self.ProjectID = project_id
        self.CloudRegion = cloud_region
        self.Dataset = dataset
        self.DataObject = dataobject


class DataInfo:

    def __init__(self, bucket_datalet: Datalet,
                 dicomstore_datalet: Datalet,
                 bigquery_datalet: Datalet ):
        self.Bucket = bucket_datalet
        self.DicomStore = dicomstore_datalet
        self.BigQuery = bigquery_datalet


class MessageError(Exception):

    def __init__(self, original_msg: str):
        self.original_message = original_msg
        self.message = "Message <{}> doesn't have an appropriate format".format(
            self.original_message
        )
        super().__init__(self.message)


class DicomIssue:
    
    def __init__(self, issue_msg: str) -> None:
        self.message = issue_msg
        regexp = '.*(Error|Warning)([-\s]*)(.*)'
        
        m = re.search(regexp, issue_msg)
        if m is None:
            raise MessageError('The issue is not a right type') 
        self.type = m.group(1)
        self.issue_msg = m.group(3)
        issue_pattern = 'T<([^>]*)>\s(.*)'
        m_issue = re.search(issue_pattern, self.issue_msg)
        if m_issue is not None:
            self.issue_short = m_issue.group(1)
            self.issue = m_issue.group(2)
        else:
            self.issue_short = None
        element_pattern = '(Element|attribute|keyword)[=\s]{,5}<([^>]*)>'
        m = re.search(element_pattern, issue_msg)
        if m is not None:
            self.attribute = m.group(2)
        else:
            self.attribute = None
        if self.attribute is not None:
            self.tag = Dic.tag_for_keyword(self.attribute)
        else:
            ptrn = '\(0x([0-9A-Fa-f]{4})[,\s]*0x([0-9A-Fa-f]{4})\)'
            m =  re.search(ptrn, issue_msg)
            if m is not None:
                self.tag = int(m.group(1) + m.group(2), 16)
            else:
                self.tag = None


        module_pattern = '(Module|Macro)[=\s]{,5}<([^>]*)>'
        m = re.search(module_pattern, issue_msg)
        if m is not None:
            self.module_macro = m.group(2)
        else:
            self.module_macro = None

    def GetQuery(self, TableName: str, SOPInstanceUID: uid) -> str:
        out = '''
            (
                {} , -- DCM_TABLE_NAME
                {} , -- DCM_SOP_INSATANCE_UID
                {} , -- ISSUE_MSG
                {} , -- MESSAGE
                {} , -- TYPE
                {} , -- MODULE_MACRO
                {} , -- KEYWORD
                {}   -- TAG
            )
            '''.format(
                self.GetValue(TableName),
                self.GetValue(str(SOPInstanceUID)),
                self.GetValue(self.issue_msg),
                self.GetValue(self.message),
                self.GetValue(self.type),
                self.GetValue(self.module_macro),
                self.GetValue(self.attribute),
                self.GetValue(self.tag)
            )
        return out

    def GetQuery_OLD(self, TableName: str, SOPInstanceUID: uid) -> str:
        out = '''
            CALL `{{0}}`.ADD_TO_ISSUE(
                {},  -- ISSUE_MSG,
                {},  -- MESSAGE,
                {},  -- TYPE,
                {},  -- MODULE_MACRO,
                {},  -- KEYWORD,
                {},  -- TAG,
                {},  -- TABLE_NAME,
                {},  --SOP_INST_UID
                ID   --ID
            );
            '''.format(
                self.GetValue(self.issue_msg),
                self.GetValue(self.message),
                self.GetValue(self.type),
                self.GetValue(self.module_macro),
                self.GetValue(self.attribute),
                self.GetValue(self.tag),
                self.GetValue(TableName),
                self.GetValue(str(SOPInstanceUID))
            )
        return out

    def GetValue(self, v):
        if v is None:
            return "NULL"
        elif type(v) == str:
            return '"{}"'.format(v)
        else:
            return v


class IssueCollection:

    def __init__(self, issues: list, table_name: str, dcmfile:str) -> None:
        self.table_name = table_name
        try: 
            ds = pydicom.read_file(dcmfile, specific_tags = ['SOPInstanceUID'])
            self.SOPInstanceUID = ds['SOPInstanceUID'].value
        except BaseException:
            self.SOPInstanceUID = None
        self.issues: list = []
        for issue in issues:
            try:
                self.issues.append(DicomIssue(issue))
            except BaseException:
                pass

    def GetQueryHeader(self) -> str:
        header = '''
            INSERT INTO `{0}`.ISSUE
                VALUES {1};
        '''
        return header

    def GetQuery(self) -> list:
        q = []
        for i, f in enumerate(self.issues):
            q.append(f.GetQuery(self.table_name, self.SOPInstanceUID))
        return q  


class DicomFix:
    
    def __init__(self, fix_msg: str) -> None:
        self.message = fix_msg
        git_url = 'https://github.com/afshinmessiah/PyDicomVerify/{}'
        repo = git.Repo(search_parent_directories=True)
        commit = repo.head.object.hexsha
        repo = git.Repo(search_parent_directories=True)
        regexp = '([^-]*)\s-\s(.*):-\>:(.*)\<function(.*)from file:(.*) line_number: (.*)\> \<function(.*)from file:(.*) line_number: (.*)\>'
        
        m = re.search(regexp, fix_msg)
        if m is None:
            raise MessageError("The message is not fix type")
        self.type = m.group(1)
        self.issue = m.group(2)
        issue_pattern = 'T<([^>]*)>\s(.*)'
        m_issue = re.search(issue_pattern, self.issue)
        if m_issue is not None:
            self.issue_short = m_issue.group(1)
            self.issue = m_issue.group(2)
        else:
            self.issue_short = None
        self.fix = m.group(3)
        self.fun1 = m.group(4)
        file1 = m.group(5)
        line1 = m.group(6)
        self.fun2 = m.group(7)
        file2 = m.group(8)
        line2 = m.group(9)
        self.file1_name = os.path.basename(file1) 
        self.file1_link = git_url.format('tree/' + commit) + "/{}#L{}".format(
            self.file1_name, line1)
        self.file2_name = os.path.basename(file2) 
        self.file2_link = git_url.format('tree/' + commit) + "/{}#L{}".format(
            self.file2_name, line2)
        element_pattern = '(Element|attribute|keyword)[=\s]{,5}<([^>]*)>'
        m = re.search(element_pattern, self.issue)
        if m is not None:
            self.attribute = m.group(2)
        else:
            self.attribute = None
        if self.attribute is not None:
            self.tag = Dic.tag_for_keyword(self.attribute)
        else:
            ptrn = '\(0x([0-9A-Fa-f]{4})[,\s]{,2}0x([0-9A-Fa-f]{4})\)'
            m =  re.search(ptrn, self.issue)
            if m is not None:
                self.tag = int(m.group(1) + m.group(2), 16)
            else:
                self.tag = None


        module_pattern = '(Module|Macro)[=\s]{,5}<([^>]*)>'
        m = re.search(module_pattern, self.issue)
        if m is not None:
            self.module_macro = m.group(2)
        else:
            self.module_macro = None

    def GetQuery(self, SOPInstanceUID: uid) -> str:
        out = '''(
                    {}, -- DCM_SOP_INSATANCE_UID 
                    {}, -- SHORT_ISSUE 
                    {}, -- ISSUE 
                    {}, -- FIX 
                    {}, -- TYPE 
                    {}, -- MODULE_MACRO 
                    {}, -- KEYWORD 
                    {}, -- TAG 
                    {}, -- FIX_FUNCTION1 
                    {}, -- FIX_FUNCTION1_LINK 
                    {}, -- FIX_FUNCTION2 
                    {}, -- FIX_FUNCTION2_LINK 
                    {} -- MESSAGE 
            )
            '''.format(
                self.GetValue(str(SOPInstanceUID)),
                self.GetValue(self.issue_short),
                self.GetValue(self.issue),
                self.GetValue(self.fix),
                self.GetValue(self.type),
                self.GetValue(self.module_macro),
                self.GetValue(self.attribute),
                self.GetValue(self.tag),
                self.GetValue(self.fun1),
                self.GetValue(self.file1_link),
                self.GetValue(self.fun2),
                self.GetValue(self.file2_link),
                self.GetValue(self.message),
                )
        return out

    def GetQuery_OLD(self, SOPInstanceUID: uid) -> str:
        out = '''
            CALL `{{0}}`.ADD_TO_FIX(
                {},  --SHORT_ISSUE
                {},  --ISSUE
                {},  --FIX
                {},  --TYPE
                {},  --MODULE_MACRO
                {},  --KEYWORD
                {},   --TAG
                {},  --FIX_FUNCTION1
                {},  --FIX_FUNCTION2
                {},  --MESSAGE
                {},  --SOP_INST_UID
                ID   --ID
            );
            '''.format(
                self.GetValue(self.issue_short),
                self.GetValue(self.issue),
                self.GetValue(self.fix),
                self.GetValue(self.type),
                self.GetValue(self.module_macro),
                self.GetValue(self.attribute),
                self.GetValue(self.tag),
                self.GetValue(self.file1_link),
                self.GetValue(self.file2_link),
                self.GetValue(self.message),
                self.GetValue(str(SOPInstanceUID))
            )
        return out

    def GetValue(self, v):
        if v is None:
            return "NULL"
        elif type(v) == str:
            return '"{}"'.format(v)
        else:
            return v


class FixCollection:

    def __init__(self, fixes: list, dcmfile:str) -> None:
        try: 
            ds = pydicom.read_file(dcmfile, specific_tags = ['SOPInstanceUID'])
            self.SOPInstanceUID = ds['SOPInstanceUID'].value
        except BaseException:
            self.SOPInstanceUID = None
        self.fixes: list = []
        for fix in fixes:
            try:
                self.fixes.append(DicomFix(fix))
            except MessageError:
                pass
    
    def GetQueryHeader(self) -> str:
        header = '''
            INSERT INTO `{0}`.FIX_REPORT
                VALUES {1};
        '''
        return header

    def GetQuery(self) -> str:
        q = []
        for i, f in enumerate(self.fixes):
            q.append(f.GetQuery(self.SOPInstanceUID))
        return q

class FileUIDS:

    def __init__(self, file, vfile, mfile):
        try:
            ds = pydicom.read_file(file, specific_tags = [
                'SOPInstanceUID','SOPClassUID', 'StudyInstanceUID',
                'SeriesInstanceUID'
            ])
            self.SOPInstanceUID = ds['SOPInstanceUID'].value
            self.StudyUID = ds['StudyInstanceUID'].value
            self.SeriesUID = ds['SeriesInstanceUID'].value
            self.SOPClassUID = ds['SOPClassUID'].value
            self.SOPClassTxt =\
                single2multi_frame.SopClassUID2Txt(self.SOPClassUID)
            self.VerificationFilePath = vfile
            self.MetaFilePath = mfile
        except BaseException as err:
            print(err)
            self.SOPInstanceUID = ''
            self.StudyUID = ''
            self.SeriesUID = ''


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
    ctools.RunExe([dcm_verify,'-filename', file], '', '', errlog = log)
    my_code_output = verify(file, False, '')


def FixFile(dicom_file, in_folder,
            fixed_dcm_folder,
            log_fix, log_david_pre, log_david_post):
    # ------------------------------------------------------------------
    deslash = lambda x: x if not x.endswith('/') else x[:-1]
    parent = os.path.dirname(dicom_file)
    file_name = os.path.basename(dicom_file)

    in_folder = deslash(in_folder)
    # ------------------------------------------------------------------
    f_dcm_folder = parent.replace(in_folder, fixed_dcm_folder)
    if not os.path.exists(f_dcm_folder):
        os.makedirs(f_dcm_folder)
    ds = read_file(dicom_file)
    log_mine = []
    VER(dicom_file, log_david_pre)
    fix_frequent_errors.priorfix_RemoveIllegalTags(ds,'All', log_fix)
    #(1)general fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("generalfix_"):
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log_fix)
    #(2)fix with verification:
    fix_Trivials(ds, log_fix)
    #(3)specific fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("fix_"):
            if ffix == "fix_Trivials":
                continue
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log_fix)
    fix_report = PrintLog(log_fix)
    fixed_file = os.path.join(f_dcm_folder, file_name)
    write_file(fixed_file, ds)
    VER(fixed_file, log_david_post)

def BuildQueries(header:str, qs:list, dataset_id: str) -> list:
    out_q = []
    ch_limit = 1024*1024
    row_limit = 1500
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
            print('{} ->'.format(n))
            query_string(out_q[-1])
    out_q.append(header.format(dataset_id, elem_q))
    query_string(out_q[-1])
    return out_q


def FIX_AND_CONVERT(in_folder, out_folder,
                    in_gcloud_info: DataInfo,
                    fx_gcloud_info: DataInfo,
                    mf_gcloud_info: DataInfo,
                    write_in_table: bool=True, prefix=''):
    logger = logging.getLogger(__name__)
    logger.info('\tStarted Fix and Convert for study {}'.format(in_folder))
    dcm_folder = os.path.join(out_folder, "fixed_dicom/")
    mfdcm_folder = os.path.join(out_folder, "multiframe/")
    in_table = '{}.{}.{}'.format(
        in_gcloud_info.BigQuery.ProjectID,
        in_gcloud_info.BigQuery.Dataset,
        in_gcloud_info.BigQuery.DataObject)
    fx_table = '{}.{}.{}'.format(
        fx_gcloud_info.BigQuery.ProjectID,
        fx_gcloud_info.BigQuery.Dataset,
        fx_gcloud_info.BigQuery.DataObject)
    mf_table = '{}.{}.{}'.format(
        mf_gcloud_info.BigQuery.ProjectID,
        mf_gcloud_info.BigQuery.Dataset,
        mf_gcloud_info.BigQuery.DataObject)
    if not os.path.exists(in_folder):
        return
    folder_list = ctools.Find(in_folder, cond_function=ctools.is_dicom, find_parent_folder=True)
    whole_instance_list = ctools.Find(in_folder, cond_function=ctools.is_dicom, find_parent_folder=False)
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    q_fix_string = []
    q_issue_string = []
    q_origin_string = []
    time_interval_for_progress_update = 1
    last_time_point_for_progress_update = 0
    start = time.time()
    number_of_instances = len(whole_instance_list)
    current_instance_number = 0
    for i, folder in enumerate(folder_list, 1):
        in_files = ctools.Find(folder, 1, ctools.is_dicom)
        logger.info('\tStart fixing series({}) out of {}'.format(
            i, len(folder_list)))
        for j, f in enumerate(in_files, 1):
            current_instance_number += 1
            progress = float(current_instance_number) / float(number_of_instances)
            time_point = time.time()
            time_elapsed = round(time_point - start)
            time_left = round(number_of_instances - current_instance_number) *\
                time_elapsed/float(current_instance_number)
            time_elapsed_since_last_show = time_point - \
                last_time_point_for_progress_update
            log_david_post = []
            log_david_pre = []
            log_fixed = []
            FixFile(
                f, in_folder, dcm_folder, log_fixed, 
                log_david_pre, log_david_post)
            fixed_file_path = f.replace(in_folder, dcm_folder)
            dicomweb_store_instance(
                _BASE_URL, 
                fx_gcloud_info.DicomStore.ProjectID,
                fx_gcloud_info.DicomStore.CloudRegion,
                fx_gcloud_info.DicomStore.Dataset,
                fx_gcloud_info.DicomStore.DataObject,
                fixed_file_path
                )
            fixes_all = FixCollection(log_fixed, f)
            q_fix_string.extend(fixes_all.GetQuery())
            pre_issues = IssueCollection(log_david_pre[1:], in_table, f)
            q_issue_string.extend(pre_issues.GetQuery())
            post_issues = IssueCollection(log_david_post[1:], fx_table, 
                f.replace(in_folder, dcm_folder))
            q_issue_string.extend(post_issues.GetQuery())
            fixed_input_ref = conv.ParentChildDicoms(pre_issues.SOPInstanceUID,
                                   post_issues.SOPInstanceUID,
                                   f.replace(in_folder, dcm_folder))
            q_origin_string.extend(fixed_input_ref.GetQuery(in_table, fx_table))    
            if time_elapsed_since_last_show > time_interval_for_progress_update or True:
                last_time_point_for_progress_update = time_point
                header = '\t\t{}/{})Instance {} was fixed successfully'.format(
                j, len(in_files), os.path.basename(f))
                progress_string = ctools.ShowProgress(
                progress, time_elapsed, time_left,60, header, False)
                logger.info(progress_string)
        logger.info('\tEnd fixing series({}) out of {}'.format(
            i, len(folder_list)))
        #  -------------------------------------------------------------
        mf_log:list = []
        single_fixed_folder = folder.replace(in_folder, dcm_folder)
        mf_folder = folder.replace(in_folder, mfdcm_folder)
        if not os.path.exists(mf_folder):
            os.makedirs(mf_folder)
        # try:
        PrntChld = conv.ConvertByHighDicomNew(
            single_fixed_folder, mf_folder, mf_log)
        logger.info(
            '\tSeries {}/{} was successfully converted into {} multiframe files'.
            format(i, len(folder_list), len(PrntChld))
            )
        # except(BaseException) as err:
        #     mf_log.append(str(err))
        #     PrntChld = []
        for pr_ch in PrntChld:
            q_origin_string.extend(pr_ch.GetQuery(in_table, fx_table))
            multiframe_log = []

            VER(pr_ch.child_dicom_file,
                                        multiframe_log)
            mf_issues = IssueCollection(multiframe_log[1:], mf_table, 
                pr_ch.child_dicom_file)
            q_issue_string.extend(mf_issues.GetQuery())
            dicomweb_store_instance(
                _BASE_URL, 
                mf_gcloud_info.DicomStore.ProjectID,
                mf_gcloud_info.DicomStore.CloudRegion,
                mf_gcloud_info.DicomStore.Dataset,
                mf_gcloud_info.DicomStore.DataObject,
                pr_ch.child_dicom_file
                )

    fix_header = fixes_all.GetQueryHeader()
    issue_header = mf_issues.GetQueryHeader()
    origin_header = PrntChld[0].GetQueryHeader()
    file_name = './gitexcluded_qqq.txt'
    dataset_id = '{}.{}'.format(
        fx_gcloud_info.BigQuery.ProjectID,
        fx_gcloud_info.BigQuery.Dataset)
    if write_in_table:
        ctools.WriteStringToFile(
            file_name,
            ctools.StrList2Txt(
                BuildQueries(fix_header, q_fix_string, dataset_id)))
        ctools.WriteStringToFile(
            file_name,
            ctools.StrList2Txt(
                BuildQueries(issue_header, q_issue_string, dataset_id)), True)
        ctools.WriteStringToFile(
            file_name,
            ctools.StrList2Txt(
                BuildQueries(
                    origin_header, q_origin_string, dataset_id)), True)
    logger.info('\tFinished Fix and Convert for study {}'.format(in_folder))

def CreateDicomStore(project_id: str,
                     cloud_region: str,
                     dataset_id: str,
                     dicom_store_id: str):
    if not exists_dataset(project_id, cloud_region, dataset_id):
        create_dataset(project_id, cloud_region, dataset_id)
    if not exists_dicom_store(project_id, 
                       cloud_region, dataset_id, 
                       dicom_store_id):
        create_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id)


home = os.path.expanduser("~")
local_tmp_folder = os.path.join(home,"Tmp")

out_folder = os.path.join(local_tmp_folder,"bgq_output")
in_folder = os.path.join(local_tmp_folder,"bgq_input")
in_dicoms = DataInfo(
    Datalet('idc-dev-etl',      # Bucket
            'us-central1',
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
fx_dicoms = DataInfo(
    Datalet('idc-dev-etl',      # Bucket
            'us-central1',
            '', ''),
    Datalet('idc-tcia',      # Dicom Store
            'us',
            'afshin_results_' + in_dicoms.BigQuery.Dataset,
            'FIXED'),
    Datalet('idc-tcia',      # Bigquery
            'us',
            'afshin_results_' + in_dicoms.BigQuery.Dataset,
            'FIXED')
    )
mf_dicoms = DataInfo(
    Datalet('idc-dev-etl',      # Bucket
            'us-central1',
            '', ''),
    Datalet('idc-tcia',      # Dicom Store
            'us',
            'afshin_results_' + in_dicoms.BigQuery.Dataset,
            'MULTIFRAME'),
    Datalet('idc-tcia',      # Bigquery
            'us',
            'afshin_results_' + in_dicoms.BigQuery.Dataset,
            'MULTIFRAME')
    )

# create_all_tables('{}.{}'.format(
#     fx_dicoms.BigQuery.ProjectID, fx_dicoms.BigQuery.Dataset),
#     fx_dicoms.BigQuery.CloudRegion, True)
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

study_query = 'SELECT STUDYINSTANCEUID, SERIESINSTANCEUID, SOPINSTANCEUID FROM `{0}` ORDER BY STUDYINSTANCEUID, SERIESINSTANCEUID, SOPINSTANCEUID WHERE STUDYINSTANCEUID >= "1.3.6.1.4.1.14519.5.2.1.1188.4001.213420711084714071744561785405"'
uids: dict = {}
q_dataset_uid = '{}.{}.{}'.format(
    in_dicoms.BigQuery.ProjectID,
    in_dicoms.BigQuery.Dataset,
    in_dicoms.BigQuery.DataObject
    )
max_number = 2^63 - 1
# max_number = 3
max_number_of_instances = max_number
max_number_of_series = max_number
max_number_of_studies = max_number
time_interval_for_progress_update = 1
last_time_point_for_progress_update = 0
start = time.time()
analysis_started = False
studies = query_string_with_result(study_query.format(q_dataset_uid))
logger = logging.getLogger(__name__)
if studies is not None:
    for row in studies:
        stuid = row.STUDYINSTANCEUID
        seuid = row.SERIESINSTANCEUID
        sopuid = row.SOPINSTANCEUID
        if stuid in uids:
            if seuid in uids[stuid]:
                uids[stuid][seuid].append(sopuid)
            else:
                uids[stuid][seuid] = [sopuid]
        else:
            uids[stuid] = {seuid: [sopuid]}
    study_count = min(len(uids), max_number_of_studies)
    for number_of_studies, (study_uid, sub_study) in enumerate(uids.items(), 1):
        progress = float(number_of_studies) / float(study_count)
        time_point = time.time()
        time_elapsed = round(time_point - start)
        time_left = round(study_count-number_of_studies) *\
            time_elapsed/float(number_of_studies)
        time_elapsed_since_last_show = time_point - \
            last_time_point_for_progress_update
        # remove the temp folder
        if os.path.exists(local_tmp_folder):
            shutil.rmtree(local_tmp_folder)
        os.makedirs(local_tmp_folder)
        if number_of_studies > max_number_of_studies:
            break
        logger.info('Start fixing study({}) out of {}'.format(
            number_of_studies, study_count))
        for number_of_series, (series_uid, instances) in enumerate(sub_study.items(), 1):
            if number_of_series > max_number_of_series:
                break
            for number_of_instances, instance_uid in enumerate(instances, 1):
                destination_file = os.path.join(
                    in_folder, '{}/{}/{}.dcm'.format(
                        study_uid, series_uid, instance_uid
                    )
                )
                dicomweb_retrieve_instance(
                    _BASE_URL, in_dicoms.DicomStore.ProjectID,
                    in_dicoms.DicomStore.CloudRegion,
                    in_dicoms.DicomStore.Dataset,
                    in_dicoms.DicomStore.DataObject,
                    study_uid, series_uid, instance_uid, destination_file)
                number_of_instances += 1
                if number_of_instances > max_number_of_instances:
                    break
        FIX_AND_CONVERT(os.path.join(
            in_folder, '{}'.format(study_uid)), out_folder,
            in_dicoms, fx_dicoms, mf_dicoms, 'INPUT FIX')
        if time_elapsed_since_last_show > time_interval_for_progress_update:
            header = '{}/{})Study {} was fix/convert-ed successfully'.format(
                number_of_studies, study_count, study_uid)
            last_time_point_for_progress_update = time_point
            progress_string = ctools.ShowProgress(progress, time_elapsed, time_left, 60, header, False)
            logger.info(progress_string)


# study_uids = os.listdir(in_folder)
# for study_uid in study_uids:
#     FIX_AND_CONVERT(os.path.join(
#         in_folder, '{}'.format(study_uid)), out_folder,
#         in_dicoms, fx_dicoms, mf_dicoms, False, 'INPUT FIX')
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