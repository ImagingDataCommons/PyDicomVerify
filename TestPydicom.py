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


# import condn_cc
def run_exe(arg_list, stderr_file, stdout_file, env_vars=None):
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
    print(out_text)

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
        print( _error.decode("ascii"))
    _output = proc.stdout
    if len(stdout_file) != 0:
        write_str_to_text(stdout_file, _output.decode("ascii"))

    return proc.returncode
def VER(file:str, out_folder:str):
    toxml_exe_file = "/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/bin/dcm2xml"
    run_exe([toxml_exe_file, file, os.path.join(out_folder,'xml.xml')],os.path.join(out_folder,'err_xml.txt'),os.path.join(out_folder,'out_xml.txt'),
            {"DYLD_LIBRARY_PATH":"/Users/afshin/Documents/softwares/dcmtk/3.6.5/bin/lib/"})
    print('{:=^120}'.format("DAVID'S"))
    dcm_verify = "/Users/afshin/Documents/softwares/dicom3tools/exe_20200430/dciodvfy"
    out = os.path.join(out_folder, "devids.txt")
    run_exe([dcm_verify,'-filename', file], out, '')
    print('{:=^120}'.format("MY CODE"))
    log = verify(file, False, '')
    print(log)
    write_str_to_text(out, '{:=^120}\n'.format("MY CODE"), True)
    write_str_to_text(out, log, True)

# =========================================================================
def write_str_to_text(file_name, content, append = False):
    if append:
        text_file = open(file_name, "a")
    else:
        text_file = open(file_name, "w")
    n = text_file.write(content)
    text_file.close()
out_folder = "/Users/afshin/Documents/work/dicom_xmls"
dicom_file = '/Users/afshin/Dropbox (Partners HealthCare)/IDC-MF_DICOM/out_00/hd/fixed_dicom//TCGA-UCEC/TCGA-D1-A0ZU/08-22-1987-MRI - PELVIS-71997/411-lava arc-03407/MR_00_.dcm'
if not os.path.exists(out_folder):
    os.makedirs(out_folder)
if os.path.isdir(dicom_file):
    files = os.listdir(dicom_file)
    for f in files:
        if f.endswith(".dcm"):
            dicom_file = os.path.join(dicom_file,f)
            break
fix_it = True
ds = read_file(dicom_file)

log = []
if fix_it:
    #(1)general fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("generalfix_"):
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log)

    #(2)fix with verification:
    fix_Trivials(ds, log)

    #(3)specific fixes:
    for ffix in dir(fix_frequent_errors):
        if ffix.startswith("fix_"):
            if ffix == "fix_Trivials":
                continue
            item = getattr(fix_frequent_errors, ffix)
            if callable(item):
                item(ds, log)

    PrintLog(log)

    fixed_file = os.path.join(out_folder, 'fixed.dcm')

    write_file(fixed_file, ds)
    VER(fixed_file, out_folder)

else:
    VER(dicom_file, out_folder)






