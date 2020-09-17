import git
import pydicom.datadict as Dic
from pydicom import uid
import re
import os

git_url = 'https://github.com/afshinmessiah/PyDicomVerify/{}'
repo = git.Repo(search_parent_directories=True)
commit = repo.head.object.hexsha


class Datalet:

    def __init__(self, project_id: str,
                 cloud_region: str,
                 dataset: str,
                 dataobject: str):
        self.ProjectID = project_id
        self.CloudRegion = cloud_region
        self.Dataset = dataset
        self.DataObject = dataobject

    def GetBigQueryStyleAddress(self, quoted: bool = True) -> str:
        output = '{}.{}.{}'.format(
            self.ProjectID,
            self.Dataset,
            self.DataObject
        )
        if quoted:
            output = '`{}`'.format(output)
        return output


class DataInfo:

    def __init__(self, bucket_datalet: Datalet,
                 dicomstore_datalet: Datalet,
                 bigquery_datalet: Datalet):
        self.Bucket = bucket_datalet
        self.DicomStore = dicomstore_datalet
        self.BigQuery = bigquery_datalet


class MessageError(Exception):

    def __init__(self, original_msg: str):
        self.original_message = original_msg
        self.message = \
            "Message <{}> doesn't have an appropriate format".format(
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
            ptrn = "\(0x([0-9A-Fa-f]{4})[,\s]*0x([0-9A-Fa-f]{4})\)"
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

    def __init__(self, issues: list, table_name: str,
                 study_uid: str,
                 series_uid: str,
                 sop_uid: str
                 ) -> None:
        self.table_name = table_name
        self.StudyInstanceUID = study_uid
        self.SeriesInstanceUID = series_uid
        self.SOPInstanceUID = sop_uid
        self.issues: list = []
        for issue in issues:
            try:
                self.issues.append(DicomIssue(issue))
            except BaseException:
                pass

    @staticmethod
    def GetQueryHeader() -> str:
        header = '''
            INSERT INTO `{0}`.ISSUE
                VALUES {1}
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

    def __init__(self, fixes: list,
                 study_uid: str,
                 series_uid: str,
                 sop_uid: str
                 ) -> None:
        self.StudyInstanceUID = study_uid
        self.SeriesInstanceUID = series_uid
        self.SOPInstanceUID = sop_uid
        self.fixes: list = []
        for fix in fixes:
            try:
                self.fixes.append(DicomFix(fix))
            except MessageError:
                pass

    @staticmethod
    def GetQueryHeader() -> str:
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
# class FileUIDS:
#     def __init__(self, file, vfile, mfile):
#         try:
#             ds = pydicom.read_file(file, specific_tags = [
#                 'SOPInstanceUID','SOPClassUID', 'StudyInstanceUID',
#                 'SeriesInstanceUID'
#             ])
#             self.SOPInstanceUID = ds['SOPInstanceUID'].value
#             self.StudyUID = ds['StudyInstanceUID'].value
#             self.SeriesUID = ds['SeriesInstanceUID'].value
#             self.SOPClassUID = ds['SOPClassUID'].value
#             self.SOPClassTxt =\
#                 single2multi_frame.SopClassUID2Txt(self.SOPClassUID)
#             self.VerificationFilePath = vfile
#             self.MetaFilePath = mfile
#         except BaseException as err:
#             print(err)
#             self.SOPInstanceUID = ''
#             self.StudyUID = ''
#             self.SeriesUID = ''
