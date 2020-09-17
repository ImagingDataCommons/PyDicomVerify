import os
import shutil
from StorageBucketStuff import download_blob, upload_blob, exists_bucket,\
    list_blobs, create_bucket,empty_bukcet, delete_bucket
from queue import Queue
import time
import common_tools as ct
import parallelization as pl




def gs_util_d(project_id: str, bucket_name: str, prefix: str, d_folder):
    d_folder = os.path.join(d_folder, prefix)
    if not os._exists(d_folder):
        os.makedirs(d_folder)
    gs_link = 'gs://{}/{}'.format(bucket_name, prefix)
    command = ["gsutil", "-m", "-u", project_id,  "cp", "-r", gs_link, d_folder]
    parent_folder = os.path.dirname(d_folder)
    ct.RunExe(
        command, os.path.join(parent_folder, 'gsutil_err_d.txt'),
        os.path.join(parent_folder, 'gsutil_out_d.txt')
        )


def gs_util_u(project_id: str, bucket_name: str, prefix: str, d_folder):
    d_folder = os.path.join(d_folder, prefix)
    gs_link = 'gs://{}'.format(bucket_name)
    parent_folder = os.path.dirname(d_folder)
    command = [
        "gsutil", "-m", "-u", project_id,
        "cp", "-r", d_folder + '/dicom', gs_link]
    ct.RunExe(
        command, os.path.join(parent_folder, 'gsutil_err_u.txt'),
        os.path.join(parent_folder, 'gsutil_out_u.txt')
        )



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


# def serial_2(project_id: str, bucket_name: str,
#              prefix: str, local_dest_folder: str,
#              u_bucket_name: str):
#     blob_list = list_blobs(project_name, d_bucket_name, prefix=d_folder)
#     d_files = []
#     for i, bl in enumerate(blob_list):
#         # print('----->{}'.format(bl.name))
#         # b_name = os.path.basename(bl.name)
#         d_file = os.path.join(local_dest_folder, bl.name)
#         up_down_(bl.name, d_file, project_name, bucket_name, u_bucket_name)


def parallel_d(number_of_threads: int, project_id: str, bucket_name: str,
           blob_list: list, local_dest_folder: str):
    d_files = []
    q = Queue()
    threads = pl.ThreadPool(number_of_threads, 'download')
    d_files = []
    for i, bl in enumerate(blob_list):
        # print('----->{}'.format(bl.name))
        # b_name = os.path.basename(bl.name)
        d_file = os.path.join(local_dest_folder, bl)
        parent_folder = os.path.dirname(d_file)
        if not os.path.exists(parent_folder):
            os.makedirs(parent_folder)
        d_files.append(d_file)
        threads.queue.put(
            (
                download_blob,
                (project_id, d_bucket_name, bl, d_file,),
            )
        )
    threads.queue.join()
    threads.kill_them_all()
    
    return d_files


def parallel_u(number_of_threads: int, project_id: str, bucket_name: str,
               blob_list: list, local_dest_folder: str):
    q = Queue()
    threads = pl.ThreadPool(number_of_threads, 'download')
    for i, bl in enumerate(blob_list):
        local_file = os.path.join(local_dest_folder, bl)
        threads.queue.put(
            (
                upload_blob,
                (project_id, u_bucket_name, local_file, bl),
            )
        )
    threads.queue.join()
    threads.kill_them_all()



def show_folder_content(folder, d_elapsed_time,
                        u_elapsed_time, heading: str = ''):
    files = ct.Find(folder, cond_function=lambda x: x.endswith('dcm'))
    size = 0
    for i, f in enumerate(files, 1):
        size += os.path.getsize(f)
    size_str = ct.get_human_readable_string(size, True)+'B'
    d_speed = int(size / d_elapsed_time)
    d_speed_str = ct.get_human_readable_string(d_speed, True)+'Bps'
    u_speed = int(size / u_elapsed_time)
    u_speed_str = ct.get_human_readable_string(u_speed, True)+'Bps'
    
    print('{} -> {} ⬆ ({}) ⬇ ({})'.format(
        heading, size_str, u_speed_str, d_speed_str))


def do_the_test(project_id: str, down_bucket: str, up_bucket: str,
                local_tmp_folder: str,
                max_number_of_files: int):
    blob_list = list_blobs(project_id, down_bucket)
    blob_name_list = []
    for i, bl in enumerate(blob_list, 1):
        if i > max_number_of_files:
            break
        blob_name_list.append(bl.name)
    print('{:-^100}'.format('TESTING FOR {} NUMBER OF BLOBS'.format(
        len(blob_name_list))))
    local_d_folder = os.path.join(local_tmp_folder, 'download')
    threads_count = list(range(0, 64, 4))
    threads_count = [1, 4, 8, 16, 32, 64]
    threads_count[0] = 1
    for thread_number in threads_count:
        if os.path.exists(local_tmp_folder):
            shutil.rmtree(local_tmp_folder)
        empty_bukcet(project_id, up_bucket)
        create_bucket(project_id, up_bucket, True)
        tic = time.time()
        parallel_d(
            thread_number, project_id, down_bucket, blob_name_list, local_d_folder)
        toc = time.time()
        d_time = toc - tic
        tic = time.time()
        parallel_u(
            thread_number, project_id, up_bucket, blob_name_list, local_d_folder)
        toc = time.time()
        u_time = toc - tic
        show_folder_content(
            local_d_folder, d_time, u_time,
            'parallel({:03d}thread):'.format(thread_number))
        if os.path.exists(local_tmp_folder):
            shutil.rmtree(local_tmp_folder)
        tic = time.time()
        parallel_d(
            thread_number, project_id, up_bucket, blob_name_list, local_d_folder)
        toc = time.time()
        d_time2 = toc - tic
        tic = time.time()
        parallel_u(
            thread_number, project_id, up_bucket, blob_name_list, local_d_folder)
        toc = time.time()
        u_time2 = toc - tic
        show_folder_content(
            local_d_folder, d_time2, u_time2,
            'parallel({:03d}thread):'.format(thread_number))


    tic = time.time()
    gs_util_d(
        project_id, up_bucket, d_folder, local_d_folder)
    toc = time.time()
    d_time = toc - tic
    tic = time.time()
    gs_util_u(
        project_id, up_bucket, d_folder, local_d_folder)
    toc = time.time()
    u_time = toc - tic
    show_folder_content(local_d_folder, d_time, u_time, 'gs_util')
    


project_name = 'idc-tcia'
d_bucket_name = 'idc-tcia-tcga-esca'
d_folder = 'dicom/1.3.6.1.4.1.14519.5.2.1.6354.4026.221877129534698284985317346754/'
u_bucket_name = 'preformance-test'
home = os.path.expanduser("~")
local_tmp_folder = os.path.join(home, "Tmp")
file_numbers = list(range(0, 300, 20))
file_numbers[0] = 10
for file_number in file_numbers:
    do_the_test(
        project_name, d_bucket_name, u_bucket_name, local_tmp_folder, file_number)
