import subprocess
import pydicom
import re, os, numpy
from datetime import timedelta
import inspect, logging
def Find(address, max_depth=0, cond_function = os.path.isfile, 
sort_key=None, reverse_sort=False,
find_parent_folder = False)->list:
    #rood depth is max_depth = 1
    approved_list = []
    RecursiveFind(address, approved_list, 0, max_depth, 
            cond_function, find_parent_folder)
    if sort_key is not None:
        approved_list.sort(key=sort_key,reverse=reverse_sort)
    return approved_list

def RecursiveFind(address, approvedlist, current_depth:int, max_depth=0,
cond_function = os.path.isfile, find_parent_folder = False):
    filelist = os.listdir(address)
    for i in range(0, len(filelist)):
        filelist[i] = os.path.join(address, filelist[i])

    for filename in filelist:
        if os.path.isdir(filename) and (max_depth<=0 or current_depth<max_depth):
            RecursiveFind(filename, approvedlist, current_depth+1, max_depth, 
            cond_function, find_parent_folder)
    
    for filename in filelist:
        if cond_function(filename):
            if find_parent_folder:
                approvedlist.append(address)
                break
            else:
                approvedlist.append(filename)
def RunExe(arg_list, stderr_file, stdout_file,outlog=None,errlog=None, env_vars=None, log=[]):
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
    log.append(out_text)

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
        WriteStringToFile(stderr_file, _error.decode("ascii"))
        # print( _error.decode("ascii"))
    _output = proc.stdout
    if len(stdout_file) != 0:
        WriteStringToFile(stdout_file, _output.decode("ascii"))
    if outlog is not None:
        outlog.extend(re.split("\n",  _output.decode("ascii")))
    if errlog is not None:
        errlog.extend(re.split("\n",  _error.decode("ascii")))
    return proc.returncode
def StrList2Txt(strlist)->str:
    out = ''
    if type(strlist)==list:
        for s in strlist:
            out +='{}\n'.format(s)
    return out

def WriteStringToFile(file_name, content, append = False):
    folder = os.path.dirname(file_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    if append:
        text_file = open(file_name, "a")
    else:
        text_file = open(file_name, "w")
    n = text_file.write(content)
    text_file.close()
def Txt2StrList(filename):
    File_object = open(filename, "r")
    try:
        Content = File_object.read()
    except:
        print("Couldn't read the file")
        Content = ""
    File_object.close()
    return Content
def GetVectorDistance(vec1, vec2):
    dist = 0
    for e1, e2 in zip(vec1, vec2):
        d = e1 - e2
        dist += d ** 2
    return numpy.sqrt(dist)

def is_dicom(filename: str) -> bool:
    is_dicom = True
    if not os.path.isfile(filename):
        return False
    import pydicom.filebase
    with pydicom.filebase.DicomFile(filename, 'rb') as fp:
        try:
            pydicom.filereader.read_preamble(fp, False)  
        except pydicom.errors.InvalidDicomError:
            is_dicom = False
    return is_dicom
def ShowProgress(progress, time_elapsed=None, time_left=None,
                 length=120,prefix='' , Print: bool=True) -> str:
    t_e = ''
    if time_elapsed is not None:
        t_e = 'time elapsed: {}'.format(str(timedelta(seconds = time_elapsed)))
    
    t_l = ''
    if time_left is not None:   
        t_l = 'estimated time left:{}'.format(str(timedelta(seconds = time_left)))
    prog_str = '{:.2%}'.format(progress)
    ll = int(progress*length)
    rr = length - ll
    form = '{{:|>{}}}{{:.<{}}}'.format(ll, rr)
    progress_bar = form.format(prog_str, '')
    out_string = '{} {} ({}) {}        '.format(prefix,t_e, progress_bar, t_l)
    if Print:
        print(out_string, end='\r', flush=True)
    return out_string


def GetFunctionLugger(indent: str = '    '):
    depth = len(inspect.stack())-2
    f_name = inspect.stack()[1][3]
    if len(f_name) > 32:
        f_name = f_name[0:32]
    else:
        f_name = "{: <32}".format(f_name)
    indent = indent*(depth)
    logger = logging.getLogger(f_name)
    return (logger, indent)