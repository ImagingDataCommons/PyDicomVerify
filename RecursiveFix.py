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
def run_exe(arg_list, stderr_file, stdout_file,log:list, env_vars=None):
    # print(str(arg_list))
    out_text = ""
    for a in arg_list:
        has_ws = False
        for ch in a:
            if ch.isspace():
                has_ws = True
                break
        if has_ws:
            out_text += "\"{}\" ".format(a)
        else:
            out_text += "{} ".format(a)
    # print(out_text)

    curr_env = os.environ.copy()
    if env_vars is not None:
        if type(env_vars) == dict:
            for key, v in env_vars.items():
                if key in curr_env:
                    curr_env[key] += ":{}".format(v)
                else:
                    curr_env[key] = v

    proc = subprocess.run(arg_list, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=curr_env)
    _error = proc.stderr
    if len(stderr_file) != 0:
        write_str_to_text(stderr_file, _error.decode("ascii"))
        # print( _error.decode("ascii"))
    _output = proc.stdout
    if len(stdout_file) != 0:
        write_str_to_text(stdout_file, _output.decode("ascii"))
    log.extend(re.split("\n",  _error.decode("ascii")))
    return proc.returncode
def VER(file:str, out_folder:str,log:list):
    file_name = os.path.basename(file)
    toxml_exe_file = "/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/bin/dcm2xml"
    run_exe([toxml_exe_file, file, os.path.join(out_folder,'xml.xml')],os.path.join(out_folder,'err_xml.txt'),os.path.join(out_folder,'out_xml.txt'),[],
            {"DYLD_LIBRARY_PATH":"/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/lib/"})
    # print('{:=^120}'.format("DAVID'S"))
    dcm_verify = "/Users/afshin/Documents/softwares/dicom3tools/dicom3tools_macexe_1.00.snapshot.20191225051647/dciodvfy"
    out = os.path.join(out_folder, file_name + "_err.txt")
    run_exe([dcm_verify,'-filename', file], out, '',log)
    # print('{:=^120}'.format("MY CODE"))
    my_code_output = verify(file, False, '')
    write_str_to_text(out, '{:=^120}\n'.format("MY CODE"), True)
    write_str_to_text(out, my_code_output, True)

# =========================================================================
def write_str_to_text(file_name, content, append = False):
    if append:
        text_file = open(file_name, "a")
    else:
        text_file = open(file_name, "w")
    n = text_file.write(content)
    text_file.close()
def GetFileString(filename):
    File_object = open(filename, "r")
    try:
        Content = File_object.read()
    except:
        print("Couldn't read the file")
        Content = ""
    File_object.close()
    return Content
def fix_file(dicom_file, in_folder,
fixed_dcm_folder, fix_report_folder, final_vfy_folder,
log_fix, log_david):
    parent = os.path.dirname(dicom_file)
    file_name=os.path.basename(dicom_file)
    f_dcm_folder = parent.replace(in_folder, fixed_dcm_folder)
    f_rpt_folder = parent.replace(in_folder, fix_report_folder)
    f_vfy_folder = parent.replace(in_folder, final_vfy_folder)
    if not os.path.exists(f_dcm_folder):
        os.makedirs(f_dcm_folder)  
    if not os.path.exists(f_rpt_folder):
        os.makedirs(f_rpt_folder)  
    if not os.path.exists(f_vfy_folder):
        os.makedirs(f_vfy_folder)  
    

    fix_it = True
    ds = read_file(dicom_file)

    log_mine = []
    if fix_it:
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

        PrintLog(log_fix)
        fixed_file = os.path.join(f_dcm_folder, file_name)

        write_file(fixed_file, ds)
        VER(fixed_file, f_vfy_folder, log_david)

    else:
        VER(dicom_file, f_vfy_folder, log_david)

def AddLogToStatistics(filename:str ,log:list, stat:dict, regexp = ''):
    folder = os.path.dirname(filename)
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
def recursive_file_find(address, approvedlist):
    filelist = os.listdir(address)
    for filename in filelist:
        fullpath = os.path.join(address, filename);

        if os.path.isdir(fullpath):
            recursive_file_find(fullpath, approvedlist)
            continue;
        filename_size = len(filename);
        if filename.find(".dcm", filename_size - 5) != -1:
            approvedlist.append(fullpath)
def write_stat_report(stat:dict, filename:str):
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
    write_str_to_text(filename, to_string)
def write_fix_stat_worksheet(seq_, excel_file):
    fs = ['N','FREQ(FILES)','FREQ(FOLDER)','ERROR TYPE','ERROR',
     "FIX APPROACH", 'CURRENT FUN', 'CURRENT FUN FILE', 'LAST FUN',
      'LAST FUN FILE']
    fs_1 = ["DCM FILE" , 'SOP UID', 'STUDY UID', 'SERIES UID']
    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet(name = "general")
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

        worksheet.write_url(r,fs.index('N'), 'internal:{}!A1'.format(r - row_offset), string=str(r-row_offset))
        worksheet.write_number(r, fs.index('FREQ(FILES)'), obj.Count)
        worksheet.write_number(r, fs.index('FREQ(FOLDER)'), len(obj.ErrorDirs))
        worksheet.write_string(r, fs.index('ERROR TYPE'), e_type)
        worksheet.write_string(r, fs.index('ERROR'), err)
        worksheet.write_string(r, fs.index('FIX APPROACH'), fix)
        worksheet.write_string(r, fs.index('CURRENT FUN'), fun1)
        worksheet.write_string(r, fs.index('CURRENT FUN FILE'), file1)
        worksheet.write_string(r, fs.index('LAST FUN'), fun2)
        worksheet.write_string(r, fs.index('LAST FUN FILE'), file2)
        worksheet1 = workbook.add_worksheet(name = "{}".format(r-row_offset))
        
        for header, idx in zip(fs_1, range(0, len(fs_1))):
            worksheet1.write_string(0, idx, header)
        secondary_row = 1
        for f, fuids in obj.ErrorFiles.items():
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
def write_vfy_stat_worksheet(seq_, excel_file):
    fs = ['N','FREQ(FILES)','FREQ(FOLDER)','ERROR']
    fs_1 = ["DCM FILE" , 'SOP UID', 'STUDY UID', 'SERIES UID']
    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet(name = "general")
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
        


        worksheet.write_url(r,fs.index('N'), 'internal:{}!A2'.format(r - row_offset), string=str(r-row_offset))
        worksheet.write_number(r, fs.index('FREQ(FILES)'), obj.Count)
        worksheet.write_number(r, fs.index('FREQ(FOLDER)'), len(obj.ErrorDirs))
        worksheet.write_string(r, fs.index('ERROR'), err)
        worksheet1 = workbook.add_worksheet(name = "{}".format(r-row_offset))
        
        for header, idx in zip(fs_1, range(0, len(fs_1))):
            worksheet1.write_string(0, idx, header)
        secondary_row = 1
        for f, fuids in obj.ErrorFiles.items():
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
        



out_folder = "/Users/afshin/Documents/work/dicom_fix01"
if os.path.exists(out_folder):
    shutil.rmtree(out_folder)
dcm_folder = os.path.join(out_folder , "dcm/")
fix_folder = os.path.join(out_folder , "fix/")
vfy_folder = os.path.join(out_folder , "vfy/")
in_folder = '/Users/afshin/Dropbox (Partners HealthCare)/IDC-MF_DICOM/data/'
dicom_file = "/Users/afshin/Dropbox (Partners HealthCare)/./IDC-MF_DICOM/data/TCGA-UCEC/TCGA-D1-A169/12-01-1992-NMPETCT trunk-32478/1007-MIPTORSO 3DFDGIR CTAC-95040/000027.dcm"

fix_rep = {}
vfy_rep = {}
file_list = []
recursive_file_find(in_folder, file_list)
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
    log_david = []
    log_fixed = []
    fix_file(f, in_folder, dcm_folder, fix_folder,
    vfy_folder,log_fixed, log_david)
    if time_elapsed_since_last_show > time_interval_for_progress_update:
        last_time_point_for_progress_update = time_point
        t_e = str(timedelta(seconds = time_elapsed))
        t_l = str(timedelta(seconds = time_left))
        prog_str = '{:.2%}'.format(progress)
        ll = int(progress*100)
        rr = 100 - ll
        form = '{{:|>{}}}{{:.<{}}}'.format(ll,rr)
        progress_bar = form.format(prog_str, '')
        print('time elapsed: {} ({}) estimated time left:{}\t\t\t'.format(t_e, progress_bar, t_l),end='\r', flush=True)
    if time_elapsed_since_last_record > time_interval_record_data:
        last_time_point_record_data = time_point
        AddLogToStatistics(f, log_fixed, fix_rep, '.*:\-\>:.*')
        write_stat_report(fix_rep, out_folder + "/stat_fix.txt")
        write_fix_stat_worksheet(fix_rep, out_folder + "/stat_fix.xlsx")
        AddLogToStatistics(f, log_david, vfy_rep,'Error.*')
        write_stat_report(vfy_rep, out_folder + "/stat_vfy.txt")
        write_vfy_stat_worksheet(vfy_rep, out_folder + "/stat_vfy.xlsx")
            # write_fix_stat_worksheet(vfy_rep, out_folder + "/stat_vfy.xlsx")


    
            

