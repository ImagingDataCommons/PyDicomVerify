import os
import shutil
from threading import Thread
from StorageBucketStuff import download_blob, upload_blob, exists_bucket,\
    list_blobs, create_bucket
from queue import Queue
import time
import common_tools as ct
class WorkerThread(Thread):

    def __init__(self, queue: Queue, **kwarg):
        Thread.__init__(self, **kwarg)
        self._queue = queue


    def run(self): 
        while True:
            (function, args) = self._queue.get()
            function(*args)
            self._queue.task_done()
            
def up_down_(blob, file, project_id, d_bucket, u_bucket):
    download_blob(
                    project_id,
                    d_bucket,
                    blob,
                    file)
    upload_blob(project_id, u_bucket_name, file, blob)

def gs_util_cp(
    project_id: str, d_bucket_name: str,
    u_bucket_name: str, prefix: str, d_folder):
    d_folder = os.path.join(d_folder,prefix)
    if not os._exists(d_folder):
        os.makedirs(d_folder)
    gs_link = 'gs://{}/{}'.format(d_bucket_name, prefix)
    command = ["gsutil", "-m", "-u", project_id,  "cp", "-r", gs_link, d_folder]
    parent_folder = os.path.dirname(d_folder)
    ct.RunExe(
        command, os.path.join(parent_folder, 'gsutil_err_d.txt'),
        os.path.join(parent_folder, 'gsutil_out_d.txt')
        )
    gs_link = 'gs://{}'.format(u_bucket_name)

    command = ["gsutil", "-m", "-u", project_id,
        "cp", "-r", d_folder + '/dicom', gs_link]
    ct.RunExe(
        command, os.path.join(parent_folder, 'gsutil_err_u.txt'),
        os.path.join(parent_folder, 'gsutil_out_u.txt')
        )

    # pp = 'gs://idc-tcia-tcga-kich/dicom/1.3.6.1.4.1.14519.5.2.1.1357.4011.125120931083013189922694218456/1.3.6.1.4.1.14519.5.2.1.1357.4011.213846823699400886279698296072/1.3.6.1.4.1.14519.5.2.1.1357.4011.103363562259738014669855138321.dcm'

def serial_1(project_id: str, bucket_name: str,
           prefix: str, local_dest_folder: str,
           u_bucket_name: str):
    blob_list = list_blobs(project_name, d_bucket_name, prefix=d_folder)
    d_files = []
    for i, bl in enumerate(blob_list):
        # print('----->{}'.format(bl.name))
        # b_name = os.path.basename(bl.name)
        d_file = os.path.join(local_dest_folder, bl.name)
        download_blob(
                    project_id,
                    bucket_name,
                    bl.name,
                    d_file)
        d_files.append((d_file, bl.name,))
    for i, f in enumerate(d_files, 1):
        upload_blob(project_id, u_bucket_name, f[0], f[1])


def serial_2(project_id: str, bucket_name: str,
           prefix: str, local_dest_folder: str,
           u_bucket_name: str):
    blob_list = list_blobs(project_name, d_bucket_name, prefix=d_folder)
    d_files = []
    for i, bl in enumerate(blob_list):
        # print('----->{}'.format(bl.name))
        # b_name = os.path.basename(bl.name)
        d_file = os.path.join(local_dest_folder, bl.name)
        up_down_(bl.name, d_file, project_name, bucket_name, u_bucket_name)


def parallel(number_of_threads: int, project_id: str, bucket_name: str,
           prefix: str, local_dest_folder: str,
           u_bucket_name: str):
    blob_list = list_blobs(project_name, d_bucket_name, prefix=d_folder)
    d_files = []
    q = Queue()
    for i in range(number_of_threads):
        t = WorkerThread(q)
        t.daemon = True
        t.start()
    for i, bl in enumerate(blob_list):
        # print('----->{}'.format(bl.name))
        # b_name = os.path.basename(bl.name)
        d_file = os.path.join(local_dest_folder, bl.name)
        parent_folder = os.path.dirname(d_file)
        if not os.path.exists(parent_folder):
            os.makedirs(parent_folder)
        d_file = os.path.join(local_dest_folder, bl.name)
        q.put(
            (up_down_,
            (bl.name, d_file, project_name, bucket_name, u_bucket_name),)
        )
    q.join()


def get_human_readable_string(input: int, binary: bool=True) -> str:
    input_suffix = ['', 'K', 'M', 'G', 'T']
    if binary:
        divisor = 1024
    else:
        divisor = 1000
    bin_ = []
    while input % divisor > 0:
        bin_.append(input % divisor)
        input = (input // divisor)
    # bin_.append(input)
    suff = input_suffix[len(bin_)-1]
    input_str = '{:03.2f} {}'.format(bin_[-1]+float(bin_[-2]) / divisor, suff)
    return input_str



def show_folder_content(folder, elapsed_time, heading:str = ''):
    files = ct.Find(folder, cond_function=lambda x: x.endswith('dcm'))
    size_suffix = ['B', 'KB', 'MB', 'GB', 'TB']
    size = 0
    for i, f in enumerate(files, 1):
        size += os.path.getsize(f)
    size_str = get_human_readable_string(size, True)+'B'
    speed = int(size / elapsed_time)
    speed_str = get_human_readable_string(speed, True)+'Bps'
    
    print('{}) -> {}({})'.format(heading, size_str, speed_str))

project_name = 'idc-tcia'
d_bucket_name = 'idc-tcia-tcga-kich'
d_folder = 'dicom/1.3.6.1.4.1.14519.5.2.1.1357.4011.125120931083013189922694218456/1.3.6.1.4.1.14519.5.2.1.1357.4011.213846823699400886279698296072/'
u_bucket_name = 'preformance-test'

create_bucket(project_name, u_bucket_name, False)
home = os.path.expanduser("~")
local_tmp_folder = os.path.join(home,"Tmp")


local_d_folder = os.path.join(local_tmp_folder, 'download')
if os.path.exists(local_tmp_folder):
    shutil.rmtree(local_tmp_folder)
tt = {}
tic = time.time()
serial_1(project_name, d_bucket_name, d_folder,
       local_d_folder, u_bucket_name)
toc = time.time()
tt['serila_1'] = toc - tic
show_folder_content(local_d_folder, toc - tic, 'serial_1')
if os.path.exists(local_tmp_folder):
    shutil.rmtree(local_tmp_folder)
tic = time.time()
serial_2(project_name, d_bucket_name, d_folder,
       local_d_folder, u_bucket_name)
toc = time.time()
tt['serila_2'] = toc - tic
show_folder_content(local_d_folder, toc - tic, 'serial_2')
if os.path.exists(local_tmp_folder):
    shutil.rmtree(local_tmp_folder)
for thread_number in range(4, 34):
    tic = time.time()
    parallel(thread_number, project_name, d_bucket_name, d_folder,
        local_d_folder, u_bucket_name)
    toc = time.time()
    tt['prallel'] = toc - tic
    show_folder_content(local_d_folder, toc - tic, 'parallel with: {}'.format(thread_number))
if os.path.exists(local_tmp_folder):
    shutil.rmtree(local_tmp_folder)
tic = time.time()
gs_util_cp(project_name, d_bucket_name, u_bucket_name, d_folder, local_d_folder)
toc = time.time()
tt['gs_util'] = toc - tic
show_folder_content(local_d_folder, toc - tic, 'gs_util')





