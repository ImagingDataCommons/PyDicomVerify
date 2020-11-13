import logging
import numpy
import inspect
import os
import pydicom
import pydicom.filebase
import re
import subprocess
import traceback
import time
from datetime import (
    # CLASSES
    timedelta,
)


def Find(address, max_depth = 0, cond_function = os.path.isfile,
         sort_key = None, reverse_sort = False,
         find_parent_folder=False) -> list:
    # rood depth is max_depth = 1
    approved_list = []
    RecursiveFind(address, approved_list, 1, max_depth,
            cond_function, find_parent_folder)
    if sort_key is not None:
        approved_list.sort(key = sort_key, reverse=reverse_sort)
    return approved_list


def RecursiveFind(address, approvedlist, current_depth:int, max_depth = 0,
                  cond_function = os.path.isfile, find_parent_folder=False):
    filelist = os.listdir(address)
    for i in range(0, len(filelist)):
        filelist[i] = os.path.join(address, filelist[i])
    for filename in filelist:
        if os.path.isdir(filename) and(
            max_depth <= 0 or current_depth < max_depth):
            RecursiveFind(filename, approvedlist, current_depth + 1, max_depth,
            cond_function, find_parent_folder)
    for filename in filelist:
        if cond_function(filename):
            if find_parent_folder:
                approvedlist.append(address)
                break
            else:
                approvedlist.append(filename)


def RunExe(arg_list, stderr_file, stdout_file, outlog=None,
           errlog=None, env_vars=None, log=[],
           char_encoding: str = 'ascii'):
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
    proc = subprocess.run(
        arg_list, shell = False, stdout = subprocess.PIPE,
        stderr = subprocess.PIPE, env=curr_env)
    _error = proc.stderr
    if len(stderr_file) != 0:
        WriteStringToFile(
            stderr_file, _error.decode(char_encoding, 'backslashreplace'))
    _output = proc.stdout
    if len(stdout_file) != 0:
        WriteStringToFile(
            stdout_file, _output.decode(char_encoding, 'backslashreplace'))
    if outlog is not None:
        outlog.extend(
            re.split("\n",  _output.decode(char_encoding, 'backslashreplace')))
    if errlog is not None:
        errlog.extend(
            re.split("\n",  _error.decode(char_encoding, 'backslashreplace')))
    return proc.returncode


def StrList2Txt(strlist) -> str:
    out = ''
    if type(strlist) == list:
        for s in strlist:
            out +='{}\n'.format(s)
    return out


def WriteStringToFile(file_name, content, append=False):
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
    with pydicom.filebase.DicomFile(filename, 'rb') as fp:
        try:
            pydicom.filereader.read_preamble(fp, False)
        except pydicom.errors.InvalidDicomError:
            is_dicom = False
    return is_dicom


def ShowProgress(progress, time_elapsed = None, time_left = None,
                 length = 120, prefix = '', Print: bool=True) -> str:
    t_e = ''
    if time_elapsed is not None:
        t_e = 'time elapsed: {}'.format(str(timedelta(seconds=time_elapsed)))
    t_l = ''
    if time_left is not None:
        t_l = 'estimated time left:{}'.format(str(timedelta(seconds=time_left)))
    prog_str = '{:.2%}'.format(progress)
    ll = int(progress * length)
    rr = length - ll
    form = '{{:|>{}}}{{:.<{}}}'.format(ll, rr)
    progress_bar = form.format(prog_str, '')
    out_string = '{} {} ({}) {}        '.format(prefix, t_e, progress_bar, t_l)
    if Print:
        print(out_string, end ='\r', flush = True)
    return out_string


class IndentAdapter(logging.LoggerAdapter):

    @staticmethod
    def indent():
        indentation_level = len(traceback.extract_stack())
        return indentation_level-4  # Remove logging infrastructure frames

    def process(self, msg, kwargs):
        ind_str = '{{: <{}}}'.format(self.indent() * 4)
        return '{i} {m}'.format(
            i = ind_str.format(self.indent()), m=msg), kwargs


def get_human_readable_string(input_: float, binary: bool = True) -> str:
    input_suffix = ['f', 'p', 'n', 'µ', 'm', ' ', 'K', 'M', 'G', 'T', 'P', 'E']
    # 1024^5 = 1125899906842624
    if binary:
        input_ *= 1125899906842624
    else:
        input_ *= 1e15
    if input_ < 1:
        return '{:6.2e} {}'.format(input_, input_suffix[0])
    if not isinstance(input_, int):
        input_ = int(input_)
    if binary:
        divisor = 1024
    else:
        divisor = 1000
    bin_ = []
    value = input_
    while value // divisor > 0:
        bin_.append(value % divisor)
        value = (value // divisor)
    bin_.append(value)
    suff = input_suffix[len(bin_)-1]
    if len(bin_) > 1:
        input_str = '{:06.2f} {}'.format(
            bin_[-1] + float(bin_[-2]) / divisor, suff)
    else:
        input_str = '{:06.2f} {}'.format(
            bin_[-1], suff)
    return input_str


def dict2str(input_, indent=1, indent_char='\t'):
    if indent <= 1:
        output = '{{\n{}\n}}'
    else:
        ind = indent_char * (indent - 1)
        if len(input_) == 0:
            return '{}'
        else:     
            output = '{2}\n{1}\n{0}{3}'.format(ind, '{}', '{{', '}}')
    content = ''
    indents = indent_char * indent
    line_ = '{}{{}}: {{}}'.format(indents)
    for i, (key, val) in enumerate(input_.items(), 1):
        if isinstance(val, dict):
            element = line_.format(key, dict2str(val, indent + 1))
        else:
            element = line_.format(key, val)
        if i != 1:
            content += '\n' + element
        else:
            content += element

    return output.format(content)


def retry_if_failes(function, args, max_retries: int = 30,
                    wait_in_sec: int = None,
                    give_message: bool = True, messaging_intervals: int = 10):
    logger = logging.getLogger(__name__)
    retries = 0
    while retries < max_retries:
        try:
            if args is not None:
                logger.debug("Start running {}({})".format(function, args))
                output = function(*args)
            else:
                output = function()
            break
        except BaseException as err:
            retries += 1
            if retries < max_retries:
                if wait_in_sec is not None and wait_in_sec > 0:
                    logger.info(
                        'waiting for {} seconds to call {} ...'.format(
                            wait_in_sec, function.__name__))
                    time.sleep(wait_in_sec)
                if give_message and retries % messaging_intervals == 0:
                    arg_msg = str(err + '\n\t')
                    arg_msg += 'Retyining number {} after {} seconds\n\t ->'\
                               ' Function {} list of arguments:'.format(
                                    retries, wait_in_sec, function.__name__)
                    arg_labels = inspect.getfullargspec(function)
                    if arg_labels is not None:
                        for arg_l, arg in zip(arg_labels[0], args):
                            if isinstance(arg, tuple) or isinstance(arg, list):
                                if len(arg) > 0:
                                    arg = arg[0]
                            if isinstance(arg, str):
                                arg_msg += ('\n\t\t\t{} = "{}"'.format(arg_l, arg))
                            else:
                                if isinstance(arg, dict):
                                    arg = dict2str(arg)
                                arg_msg += ('\n\t\t\t{} = {}'.format(arg_l, arg))
                    else:
                        arg_msg += "No argumnets()"
                    logger.info(arg_msg)
            else:
                raise err
    return output
