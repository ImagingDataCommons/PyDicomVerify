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
from BigQueryStuff import create_all_tables, query_string
PROJECT_NAME = 'idc-tcia'
dataset = 'afshin_test00'


    
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
        regexp = '([^-]*)\s-\s(.*):-\>:(.*)\<function(.*)from file:(.*)\> \<function(.*)from file:(.*)\>'
        
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
        self.fun2 = m.group(6)
        file2 = m.group(7)
        self.file1_name = os.path.basename(file1) 
        self.file1_link = file1.replace(
            '/Users/afshin/Documents/work/VerifyDicom',
            git_url.format('tree/' + commit))
        self.file2_name = os.path.basename(file2) 
        self.file2_link = file2.replace(
            '/Users/afshin/Documents/work/VerifyDicom',
            git_url.format('tree/' + commit))
        element_pattern = '(Element|attribute|keyword)[=\s]{,5}<([^>]*)>'
        m = re.search(element_pattern, fix_msg)
        if m is not None:
            self.attribute = m.group(2)
        else:
            self.attribute = None
        if self.attribute is not None:
            self.tag = Dic.tag_for_keyword(self.attribute)
        else:
            ptrn = '\(0x([0-9A-Fa-f]{4})[,\s]0x([0-9A-Fa-f]{4})\)'
            m =  re.search(ptrn, fix_msg)
            if m is not None:
                self.tag = int(m.group(1) + m.group(2), 16)
            else:
                self.tag = None


        module_pattern = '(Module|Macro)[=\s]{,5}<([^>]*)>'
        m = re.search(module_pattern, fix_msg)
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
                    {}, -- FIX_FUNCTION2 
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
                self.GetValue(self.file1_link),
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
            INSERT INTO `{0}`.FIX
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


def VER(file:str, out_folder:str, log:list, write_meta=True):
    file_name = os.path.basename(file)
    if file_name.endswith('.dcm'):
        file_name = file_name[:-4]
    meta_file = os.path.join(out_folder, file_name +'.xml')
    if write_meta:
        toxml_exe_file =\
        "/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/bin/dcm2xml"
        if not os.path.exists(toxml_exe_file):
            toxml_exe_file = shutil.which('dcm2xml')
            if toxml_exe_file is None:
                print('ERROR: Please install dcm2xml in system path')
                assert(False)
        ctools.RunExe([toxml_exe_file, file, meta_file],'', '',
            env_vars = {"DYLD_LIBRARY_PATH":"/Users/afshin/"
            "Documents/softwares/dcmtk/3.6.5/bin/lib/"})
    else:
        meta_file = ''
    # print('{:=^120}'.format("DAVID'S"))
    dcm_verify = "/Users/afshin/Documents/softwares"\
        "/dicom3tools/exe_20200430/dciodvfy"
    if not os.path.exists(dcm_verify):
        dcm_verify = shutil.which('dciodvfy')
        if dcm_verify is None:
            print("Error: install dciodvfy into system path")
            assert(False)
    vfy_file = os.path.join(out_folder, file_name + "_vfy.txt")
    ctools.RunExe([dcm_verify,'-filename', file], vfy_file, '', errlog = log)
    # print('{:=^120}'.format("MY CODE"))
    my_code_output = verify(file, False, '')
    ctools.WriteStringToFile(vfy_file, '{:=^120}\n'.format("MY CODE"), True)
    ctools.WriteStringToFile(vfy_file, my_code_output, True)
    return(vfy_file, meta_file)
# == == == == == == == == == == == == == == == == == == == == == == == == == 


def FixFile(dicom_file, in_folder,
            fixed_dcm_folder, fixed_report_folder,
            pre_vfy_folder, post_vfy_folder,
            log_fix, log_david_pre, log_david_post):
    # ------------------------------------------------------------------
    deslash = lambda x: x if not x.endswith('/') else x[:-1]
    parent = os.path.dirname(dicom_file)
    file_name = os.path.basename(dicom_file)
    fixed_dcm_folder = deslash(fixed_dcm_folder)
    fixed_report_folder = deslash(fixed_report_folder)
    pre_vfy_folder = deslash(pre_vfy_folder)
    post_vfy_folder = deslash(post_vfy_folder)
    in_folder = deslash(in_folder)
    # ------------------------------------------------------------------
    f_dcm_folder = parent.replace(in_folder, fixed_dcm_folder)
    f_rpt_folder = parent.replace(in_folder, fixed_report_folder)
    f_pre_vfy_folder = parent.replace(in_folder, pre_vfy_folder)
    f_post_vfy_folder = parent.replace(in_folder, post_vfy_folder)
    if not os.path.exists(f_dcm_folder):
        os.makedirs(f_dcm_folder)
    if not os.path.exists(f_rpt_folder):
        os.makedirs(f_rpt_folder)
    if not os.path.exists(f_pre_vfy_folder):
        os.makedirs(f_pre_vfy_folder)
    if not os.path.exists(f_post_vfy_folder):
        os.makedirs(f_post_vfy_folder)
    ds = read_file(dicom_file)
    log_mine = []
    (v_file_pre, m_file_pre) = VER(dicom_file, f_pre_vfy_folder, log_david_pre)
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
    ctools.WriteStringToFile(os.path.join(f_rpt_folder,
                             file_name +'_fix_report.txt'),
                             fix_report)
    (v_file_post, m_file_post) = VER(fixed_file,
                                     f_post_vfy_folder,
                                     log_david_post)
    return(v_file_pre, m_file_pre, v_file_post, m_file_post)

def BuildQueries(header:str, qs:list, dataset_id: str) -> list:
    out_q = []
    ch_limit = 1024*1024
    row_limit = 2000
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
    return out_q

        


def FIX_AND_CONVERT(in_folder, out_folder, prefix =''):
    dcm_folder = os.path.join(out_folder, "fixed_dicom/")
    mfdcm_folder = os.path.join(out_folder, "multiframe/")
    mfvfy_folder = os.path.join(out_folder, "mf_vfy/")
    fix_folder = os.path.join(out_folder, "fix_report/")
    pre_vfy_folder = os.path.join(out_folder, "pre-fix_vfy_report/")
    post_vfy_folder = os.path.join(out_folder, "post-fix_vfy_report/")
    fix_report_file_name = '/TCIA_fix_report_total'
    pre_fix_error_file_name = '/TCIA_pre-fix_verification_error'
    post_fix_error_file_name = '/TCIA_post-fix_verification_error'
    pre_fix_warning_file_name = '/TCIA_pre-fix_verification_warning'
    post_fix_warning_file_name = '/TCIA_post-fix_verification_warning'
    input_table = 'InputTable'
    fixed_table = 'FixedTable'
    mf_table = 'MultiFrameTable'
    dataset_id = '{}.{}'.format(PROJECT_NAME, dataset)
    fix_rep = {}
    pre_fix_error_statistics = {}
    post_fix_error_statistics = {}
    pre_fix_warning_statistics = {}
    post_fix_warning_statistics = {}
    if not os.path.exists(in_folder):
        return(pre_fix_error_statistics, post_fix_error_statistics,
            pre_fix_warning_statistics, post_fix_warning_statistics)
    folder_list = ctools.Find(in_folder, cond_function=ctools.is_dicom, find_parent_folder=True)
    start = time.time()
    repo = git.Repo(search_parent_directories=True)
    print(repo.active_branch)
    sha = repo.head.object.hexsha
    print(sha)
    time_interval_for_progress_update = 1
    time_interval_record_data = 1800
    last_time_point_for_progress_update = 0
    last_time_point_record_data = 0
    analysis_started = False
    q_fix_string = []
    q_issue_string = []
    q_origin_string = []
    for i, folder in enumerate(folder_list, 1):
        progress = float(i) / float(len(folder_list))
        time_point = time.time()
        time_elapsed = round(time_point - start)
        time_left = round(float(len(folder_list)-i) * time_elapsed/float(i))
        time_elapsed_since_last_show = (time_point -
            last_time_point_for_progress_update)
        time_elapsed_since_last_record = (time_point -
            last_time_point_record_data)

        in_files = ctools.Find(in_folder, 1, ctools.is_dicom)
        for f in in_files:
            log_david_post = []
            log_david_pre = []
            log_fixed = []
            (v_pre, m_pre, v_post, m_post) = FixFile(
                f, in_folder, dcm_folder,
                fix_folder, pre_vfy_folder,
                post_vfy_folder, log_fixed,
                log_david_pre, log_david_post)
            fixed_file_path = f.replace(in_folder, dcm_folder)
            fixes_all = FixCollection(log_fixed, f)
            q_fix_string.extend(fixes_all.GetQuery())
                
            #query_string(fixes_all.GetQuery().format(dataset_id))
            pre_issues = IssueCollection(log_david_pre[1:], input_table, f)
            q_issue_string.extend(pre_issues.GetQuery())
            #query_string(pre_issues.GetQuery().format(dataset_id))
            post_issues = IssueCollection(log_david_post[1:], fixed_table, 
                f.replace(in_folder, dcm_folder))
            q_issue_string.extend(post_issues.GetQuery())
            #query_string(post_issues.GetQuery().format(dataset_id))
            fixed_input_ref = conv.ParentChildDicoms(pre_issues.SOPInstanceUID,
                                   post_issues.SOPInstanceUID,
                                   f.replace(in_folder, dcm_folder))
            q_origin_string.extend(fixed_input_ref.GetQuery(input_table, fixed_table))
            #query_string(
                # fixed_input_ref.GetQuery(input_table, fixed_table).format(
                #     dataset_id
                # )
            # )
        #  -------------------------------------------------------------
        
        mf_log:list = []
        single_fixed_folder = folder.replace(in_folder, dcm_folder)
        mf_folder = folder.replace(in_folder, mfdcm_folder)
        if not os.path.exists(mf_folder):
            os.makedirs(mf_folder)
        # try:
        PrntChld = conv.ConvertByHighDicomNew(
            single_fixed_folder, mf_folder, mf_log)
        # except(BaseException) as err:
        #     mf_log.append(str(err))
        #     PrntChld = []
        for pr_ch in PrntChld:
            #query_string(pr_ch.GetQuery(fixed_table, mf_table).format(
                # dataset_id))
            q_origin_string.extend(pr_ch.GetQuery(input_table, fixed_table))
            multiframe_log = []
            (v_file_post, m_file_post) = VER(pr_ch.child_dicom_file,
                                        mfvfy_folder,
                                        multiframe_log)
            mf_issues = IssueCollection(multiframe_log[1:], mf_table, 
                pr_ch.child_dicom_file)
            q_issue_string.extend(mf_issues.GetQuery())
            
            #query_string(mf_issues.GetQuery().format(dataset_id))
        if time_elapsed_since_last_show > time_interval_for_progress_update:
            last_time_point_for_progress_update = time_point
            ctools.ShowProgress(progress, time_elapsed, time_left, 80, prefix)
            if i == len(folder_list):
                print('\n')
    fix_header = fixes_all.GetQueryHeader()
    issue_header = mf_issues.GetQueryHeader()
    origin_header = PrntChld[0].GetQueryHeader()
    file_name = './gitexcluded_qqq.txt'
    ctools.WriteStringToFile(file_name, ctools.StrList2Txt(BuildQueries(fix_header, q_fix_string, dataset_id)))
    ctools.WriteStringToFile(file_name, ctools.StrList2Txt(BuildQueries(issue_header, q_issue_string, dataset_id)), True)
    ctools.WriteStringToFile(file_name, ctools.StrList2Txt(BuildQueries(origin_header, q_origin_string, dataset_id)), True)
    return(
        pre_fix_error_statistics, 
        post_fix_error_statistics,
        pre_fix_warning_statistics, 
        post_fix_warning_statistics
        )

create_all_tables('{}.{}'.format(PROJECT_NAME, dataset), True)
small = 'TCGA-UCEC/TCGA-D1-A16G/07-11-1992-NMPETCT trunk-82660/'\
    '1005-TRANSAXIALTORSO 3DFDGIR CTAC-37181/'
# small = ''
local_dropbox_folder = "/Users/afshin/Dropbox (Partners HealthCare)/"
if not os.path.exists(local_dropbox_folder):
    local_dropbox_folder = "."
out_folder = os.path.join(local_dropbox_folder,"bgq_output")
in_folder = os.path.join(local_dropbox_folder,"IDC-MF_DICOM/data/"+small)
if len(sys.argv) > 1:
    in_folder = sys.argv[1]
if os.path.exists(out_folder):
    shutil.rmtree(out_folder)
slash = lambda x: x if x.endswith('/') else x+'/'
in_folder = slash(in_folder)
out_folder = slash(out_folder)
# ---------------------------------------------------------------
highdicom_folder = os.path.join(out_folder, "hd/files")
pixelmed_folder = os.path.join(out_folder, "pm/files")
inputresult_folder = os.path.join(out_folder,"in")
input_stats = FIX_AND_CONVERT(in_folder, inputresult_folder, 'INPUT FIX')
# fixed_folder = os.path.join(inputresult_folder, 'fixed_dicom/')
# conversion_log = []
# single2multi_frame.Convert(fixed_folder, pixelmed_folder, highdicom_folder,
#      conversion_log)
# ctools.WriteStringToFile(os.path.join(highdicom_folder,'highdicom_log.txt'),
# ctools.StrList2Txt(conversion_log))
# hd_stats = FIX(highdicom_folder, os.path.dirname(highdicom_folder), 'FIXING HD')
# pm_stats = FIX(pixelmed_folder, os.path.dirname(pixelmed_folder), 'FIXING PM')
