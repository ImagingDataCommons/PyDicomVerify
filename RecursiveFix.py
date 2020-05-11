import git
import shutil
from pydicom import *
import pydicom.datadict as Dic
import pydicom.dataelem as Elm
import pydicom.sequence as Seq
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
import single2multi_frame
class FileUIDS:
    StudyUID:pydicom.uid.UID
    SeriesUID:pydicom.uid.UID
    SOPInstanceUID:pydicom.uid.UID
    def __init__(self, file):
        try:
            ds = pydicom.read_file(file, specific_tags=[
                'SOPInstanceUID', 'StudyInstanceUID', 'SeriesInstanceUID'
            ])
            self.SOPInstanceUID = ds['SOPInstanceUID'].value
            self.StudyUID = ds['StudyInstanceUID'].value
            self.SeriesUID = ds['SeriesInstanceUID'].value
            
        except BaseException as err:
            print(err)
            self.SOPInstanceUID = ''
            self.StudyUID = ''
            self.SeriesUID = ''

class ErrStatistics:
    SampleTargetFile:str
    ErrorDirs:set
    ErrorFiles:dict
    Count:int
    def __init__(self):
        self.SampleTargetFile = ''
        self.ErrorDirs = set()
        self.ErrorFiles = {}
        self.Count = 0
# import condn_cc
def VER(file:str, out_folder:str,log:list):
    file_name = os.path.basename(file)
    toxml_exe_file = "/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/bin/dcm2xml"
    ctools.RunExe([toxml_exe_file, file, os.path.join(out_folder,'xml.xml')],
    os.path.join(out_folder,'err_xml.txt'),os.path.join(out_folder,'out_xml.txt'),
            env_vars={"DYLD_LIBRARY_PATH":"/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/lib/"})
    # print('{:=^120}'.format("DAVID'S"))
    dcm_verify = "/Users/afshin/Documents/softwares/dicom3tools/exe_20200430/dciodvfy"
    out = os.path.join(out_folder, file_name + "_err.txt")
    ctools.RunExe([dcm_verify,'-filename', file], out, '', errlog=log)
    # print('{:=^120}'.format("MY CODE"))
    my_code_output = verify(file, False, '')
    ctools.WriteStringToFile(out, '{:=^120}\n'.format("MY CODE"), True)
    ctools.WriteStringToFile(out, my_code_output, True)

# =========================================================================
def FixFile(dicom_file, in_folder,
fixed_dcm_folder, fixed_report_folder, pre_vfy_folder, post_vfy_folder, 
log_fix, log_david_pre,log_david_post):

#------------------------------------------------------------------
    deslash = lambda x: x if not x.endswith('/') else x[:-1]
    parent = os.path.dirname(dicom_file)
    file_name=os.path.basename(dicom_file)
    fixed_dcm_folder= deslash(fixed_dcm_folder)
    fixed_report_folder= deslash(fixed_report_folder)
    pre_vfy_folder= deslash(pre_vfy_folder)
    post_vfy_folder= deslash(post_vfy_folder)
    in_folder= deslash(in_folder)
#------------------------------------------------------------------
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
    

    fix_it = True
    ds = read_file(dicom_file)
    

    log_mine = []
    VER(dicom_file, f_pre_vfy_folder, log_david_pre)
    if fix_it:
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
        ctools.WriteStringToFile(os.path.join(f_rpt_folder, file_name+'_fix_report.txt'),fix_report)
        VER(fixed_file, f_post_vfy_folder, log_david_post)


    

def AddLogToStatistics(filename:str ,log:list, stat:dict, regexp = ''):
    folder = os.path.dirname(filename)
    folder = FileFromDropbox(folder)
    for i in log:
        if regexp != '':
            if re.match(regexp,i) is None:
                continue

        if i in stat:
            
            stat[i].ErrorDirs.add(folder)
            stat[i].Count += 1
            if filename not in stat[i].ErrorFiles:
                stat[i].ErrorFiles[filename] = FileUIDS(filename)
        else:
            stat_let = ErrStatistics()
            stat_let.ErrorDirs = {folder}
            stat_let.ErrorFiles [filename] = FileUIDS(filename)
            stat_let.Count = 1
            stat[i] = stat_let

def WriteReportStatisticsToFile(stat:dict, filename:str):
    to_string = ''
    c = 0
    for k,v in sorted(stat.items(),key=lambda x:x[1].Count, reverse=True):
        c += 1
        msg = '\n\t\t\t{}: {}'
        to_string += "({}) {} cases in {} folders : {}".format(
            c, v.Count, len(v.ErrorDirs), k
        )
        top = list(v.ErrorFiles.items())[0]
        to_string += msg.format('FILE',top[0])
        to_string += msg.format('SOP',top[1].SOPInstanceUID)
        to_string += msg.format('STUDY',top[1].StudyUID)
        to_string += msg.format('SERIES',top[1].SeriesUID)
    ctools.WriteStringToFile(filename, to_string)
def WriteFixReportToWorksheet(seq_, excel_file):
    fs = ['N','FREQ(FILES)','FREQ(FOLDER)','ERROR TYPE','ERROR',
     "FIX APPROACH", 'CURRENT FUN', 'CURRENT FUN FILE', 'LAST FUN',
      'LAST FUN FILE']
    fs_1 = ["DCM FILE" , 'SOP UID', 'STUDY UID', 'SERIES UID']
    workbook = xlsxwriter.Workbook(excel_file)
    home_sheet = "general"
    worksheet = workbook.add_worksheet(name = home_sheet)
    col = 0
    git_url = 'https://github.com/afshinmessiah/PyDicomVerify/{}'
    repo = git.Repo(search_parent_directories=True)
    worksheet.write_string(0, 0,"GIT BRANCH")
    branch = str(repo.active_branch)
    worksheet.write_url(1, 0, git_url.format('tree/'+branch), string=branch)
    worksheet.write_string(0, 1,'HEAD HASH')
    commit = repo.head.object.hexsha
    worksheet.write_url(1, 1, git_url.format('tree/'+commit), string=commit)
    row_offset = 2
    for value, idx in zip(fs, range(0, len(fs))):
        worksheet.write_string(row_offset, idx, value)
    r = 1 + row_offset
    
    for err, obj in sorted(seq_.items(), key=lambda x:x[1].Count, reverse=True):
        regexp = '(.*{})-(.*):-\>:(.*)\<function(.*)from file:(.*)\> \<function(.*)from file:(.*)\>'
        
        m = re.search(regexp.format('Fix\s'), err)
        if m is None:
            m = re.search(regexp.format('Error\s'), err)

        
        e_type = m.group(1)
        err = m.group(2)
        fix = m.group(3)
        fun1 = m.group(4)
        file1 = m.group(5)
        fun2 = m.group(6)
        file2 = m.group(7)

        file1_name = os.path.basename(file1) 
        file1_link = file1.replace('/Users/afshin/Documents/work/VerifyDicom',git_url.format('tree/'+commit))
        file2_name = os.path.basename(file2) 
        file2_link = file2.replace('/Users/afshin/Documents/work/VerifyDicom',git_url.format('tree/'+commit))
        
        

        worksheet.write_url(r,fs.index('N'), 'internal:{}!A1'.format(r - row_offset), string=str(r-row_offset))
        worksheet.write_number(r, fs.index('FREQ(FILES)'), obj.Count)
        worksheet.write_number(r, fs.index('FREQ(FOLDER)'), len(obj.ErrorDirs))
        worksheet.write_string(r, fs.index('ERROR TYPE'), e_type)
        worksheet.write_string(r, fs.index('ERROR'), err)
        worksheet.write_string(r, fs.index('FIX APPROACH'), fix)
        worksheet.write_string(r, fs.index('CURRENT FUN'), fun1)
        worksheet.write_url(r, fs.index('CURRENT FUN FILE'), file1_link,string=file1_name)
        worksheet.write_string(r, fs.index('LAST FUN'), fun2)
        worksheet.write_url(r, fs.index('LAST FUN FILE'), file2_link,string=file2_name)

        worksheet1 = workbook.add_worksheet(name = "{}".format(r-row_offset))
        worksheet1.write_url(0,0 , 'internal:{}!A2'.format(home_sheet), 
        string="back to {} sheet".format(home_sheet))
        
        for header, idx in zip(fs_1, range(0, len(fs_1))):
            worksheet1.write_string(1, idx, header)
        secondary_row = 2
        for f, fuids in obj.ErrorFiles.items():
            f = FileFromDropbox(f)
            worksheet1.write_string(secondary_row, fs_1.index('DCM FILE'),f)
            worksheet1.write(secondary_row, fs_1.index('SOP UID'), fuids.SOPInstanceUID)
            worksheet1.write(secondary_row, fs_1.index('STUDY UID'), fuids.StudyUID)
            worksheet1.write(secondary_row, fs_1.index('SERIES UID'), fuids.SeriesUID)
            secondary_row += 1
        
        worksheet1.write(secondary_row, 0, 'FOLDERS LIST')
        secondary_row +=1
        for idx, d in enumerate(obj.ErrorDirs, 1):
            worksheet1.write(idx+secondary_row-1, 0, d)
        r += 1

    workbook.close()
def FileFromDropbox(f)->str:
    if f.find(local_dropbox_folder) != -1:
        f=f.replace(local_dropbox_folder,'.')
    return f
        

def WriteVryReportToWorksheet(seq_, excel_file):
    fs = ['N','FREQ(FILES)','FREQ(FOLDER)','ERROR']
    fs_1 = ["DCM FILE" , 'SOP UID', 'STUDY UID', 'SERIES UID']
    workbook = xlsxwriter.Workbook(excel_file)
    home_sheet = "general"
    worksheet = workbook.add_worksheet(name = home_sheet)
    col = 0
    git_url = 'https://github.com/afshinmessiah/PyDicomVerify/{}'
    repo = git.Repo(search_parent_directories=True)
    worksheet.write_string(0, 0,"GIT BRANCH")
    branch = str(repo.active_branch)
    worksheet.write_url(1, 0, git_url.format('tree/'+branch), string=branch)
    worksheet.write_string(0, 1,'HEAD HASH')
    commit = repo.head.object.hexsha
    worksheet.write_url(1, 1, git_url.format('commit/'+commit), string=commit)
    row_offset = 2
    for value, idx in zip(fs, range(0, len(fs))):
        worksheet.write_string(row_offset, idx, value)
    r = 1 + row_offset
    
    for err, obj in sorted(seq_.items(), key=lambda x:x[1].Count, reverse=True):
        


        worksheet.write_url(r,fs.index('N'), 'internal:{}!A1'.format(r - row_offset), string=str(r-row_offset))
        worksheet.write_number(r, fs.index('FREQ(FILES)'), obj.Count)
        worksheet.write_number(r, fs.index('FREQ(FOLDER)'), len(obj.ErrorDirs))
        worksheet.write_string(r, fs.index('ERROR'), err)
        worksheet1 = workbook.add_worksheet(name = "{}".format(r-row_offset))
        worksheet1.write_url(0,0 , 'internal:{}!A2'.format(home_sheet), 
        string="back to {} sheet".format(home_sheet))
        
        for header, idx in zip(fs_1, range(0, len(fs_1))):
            worksheet1.write_string(1, idx, header)
        secondary_row = 2
        for f, fuids in obj.ErrorFiles.items():
            f = FileFromDropbox(f)

            worksheet1.write(secondary_row, fs_1.index('DCM FILE'), f)
            worksheet1.write(secondary_row, fs_1.index('SOP UID'), fuids.SOPInstanceUID)
            worksheet1.write(secondary_row, fs_1.index('STUDY UID'), fuids.StudyUID)
            worksheet1.write(secondary_row, fs_1.index('SERIES UID'), fuids.SeriesUID)
            secondary_row += 1
        
        worksheet1.write(secondary_row, 0, 'FOLDERS LIST')
        secondary_row +=1
        for idx, d in enumerate(obj.ErrorDirs, 1):
            worksheet1.write(idx+secondary_row-1, 0, d)
        r += 1

    workbook.close()
def FIX(in_folder, out_folder, prefix=''):

    dcm_folder = os.path.join(out_folder , "fixed_dicom/")
    fix_folder = os.path.join(out_folder , "fix_report/")
    pre_vfy_folder = os.path.join(out_folder , "beforefix_vfy_report/")
    post_vfy_folder = os.path.join(out_folder , "afterfix_vfy_report/")
    fix_report_file_name = '/TCIA_fix_report_total'
    pre_fix_report_file_name = '/TCIA_pre-fix_verification_report'
    post_fix_report_file_name = '/TCIA_post-fix_verification_report'
    fix_rep = {}
    pre_fix_error_statistics = {}
    post_fix_error_statistics = {}
    pre_fix_warning_statistics = {}
    post_fix_warning_statistics = {}
    file_list = ctools.Find(in_folder,cond_function=ctools.is_dicom,)
    start = time.time()
    repo = git.Repo(search_parent_directories=True)
    print(repo.active_branch)
    sha = repo.head.object.hexsha
    print(sha)
    time_interval_for_progress_update = .5
    time_interval_record_data = 30
    last_time_point_for_progress_update = 0
    last_time_point_record_data = 0
    for i, f in enumerate(file_list,1):
        progress = float(i) / float(len(file_list))
        time_point = time.time()
        time_elapsed = round(time_point - start)
        time_left = round(float(len(file_list)-i)* time_elapsed/float(i))
        time_elapsed_since_last_show = time_point - last_time_point_for_progress_update
        time_elapsed_since_last_record = time_point - last_time_point_record_data
        log_david_post = []
        log_david_pre = []
        log_fixed = []
        FixFile(f, in_folder, dcm_folder, fix_folder, pre_vfy_folder,
        post_vfy_folder,log_fixed, log_david_pre, log_david_post)
        fixed_file_path = f.replace(in_folder,dcm_folder)
        AddLogToStatistics(f, log_fixed, fix_rep, '.*:\-\>:.*')
        AddLogToStatistics(fixed_file_path, log_david_post, post_fix_error_statistics,'Error.*')
        AddLogToStatistics(f, log_david_pre, pre_fix_error_statistics,'Error.*')
        AddLogToStatistics(fixed_file_path, log_david_post, post_fix_warning_statistics,'Warning.*')
        AddLogToStatistics(f, log_david_pre, pre_fix_warning_statistics,'Warning.*')
        if time_elapsed_since_last_show > time_interval_for_progress_update:
            last_time_point_for_progress_update = time_point
            ctools.ShowProgress(progress,time_elapsed, time_left, 80, prefix)
            if i == len(file_list):
                print('\n')
        if time_elapsed_since_last_record > time_interval_record_data:
            last_time_point_record_data = time_point
            WriteFixReportToWorksheet(fix_rep, out_folder + fix_report_file_name+".xlsx")
            WriteVryReportToWorksheet(post_fix_error_statistics, out_folder+ post_fix_report_file_name+".xlsx")
            WriteVryReportToWorksheet(pre_fix_error_statistics, out_folder+ pre_fix_report_file_name+".xlsx")

            # WriteReportStatisticsToFile(fix_rep, out_folder + fix_report_file_name+".txt")
            # WriteReportStatisticsToFile(post_fix_error_statistics, out_folder+ post_fix_report_file_name+".txt")
            # WriteReportStatisticsToFile(pre_fix_error_statistics, out_folder+ pre_fix_report_file_name+".txt")
                # WriteFixReportToWorksheet(vfy_rep, out_folder + "/stat_vfy.xlsx")
    return (pre_fix_error_statistics,post_fix_error_statistics, pre_fix_warning_statistics, post_fix_warning_statistics)
def SubtractDictionaries(d1, d2):
    out = {}
    for k, v in d1.items():
        if k not in d2:
            out[k] = v
    return out
def WriteMultiFrameOnlyReportOnWorksheet(sf_statistics, mf_statistics, filename):
    only = SubtractDictionaries(mf_statistics, sf_statistics )
    WriteVryReportToWorksheet(only, filename)



        
                
    



        

small = 'TCGA-UCEC/TCGA-D1-A16G/07-11-1992-NMPETCT trunk-82660/1005-TRANSAXIALTORSO 3DFDGIR CTAC-37181/'
small = ''
local_dropbox_folder = "/Users/afshin/Dropbox (Partners HealthCare)/"
out_folder = os.path.join(local_dropbox_folder,"fix_output00")
in_folder = os.path.join(local_dropbox_folder,"IDC-MF_DICOM/data/"+small)
if os.path.exists(out_folder):
    shutil.rmtree(out_folder)

#---------------------------------------------------------------
highdicom_folder = os.path.join(out_folder, "hd/files")
pixelmed_folder = os.path.join(out_folder, "pm/files")
inputresult_folder = os.path.join(out_folder,"in")
input_stats = FIX(in_folder, inputresult_folder, 'INPUT FIX')
fixed_folder = os.path.join(inputresult_folder, 'fixed_dicom/')
conversion_log = []
single2multi_frame.Convert(fixed_folder,pixelmed_folder, highdicom_folder, 
     conversion_log)
ctools.WriteStringToFile(os.path.join(highdicom_folder,'highdicom_log.txt'),
ctools.StrList2Txt(conversion_log))

hd_stats = FIX(highdicom_folder,os.path.dirname(highdicom_folder), 'FIXING HD')
pm_stats = FIX(pixelmed_folder, os.path.dirname(pixelmed_folder), 'FIXING PM')

WriteMultiFrameOnlyReportOnWorksheet(input_stats[1], hd_stats[1],
 os.path.join(out_folder,'hd_mfonly_post_fix_error.xlsx'))
WriteMultiFrameOnlyReportOnWorksheet(input_stats[1], pm_stats[1],
 os.path.join(out_folder,'pm_mfonly_post_fix_error.xlsx'))
WriteMultiFrameOnlyReportOnWorksheet(input_stats[3], hd_stats[3],
 os.path.join(out_folder,'hd_mfonly_post_fix_warning.xlsx'))
WriteMultiFrameOnlyReportOnWorksheet(input_stats[3], pm_stats[3],
 os.path.join(out_folder,'pm_mfonly_post_fix_warning.xlsx'))

