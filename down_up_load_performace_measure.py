import os
import shutil
from StorageBucketStuff import download_blob, upload_blob, exists_bucket,\
    list_blobs, create_bucket
from queue import Queue

def serial(project_id: str, bucket_name: str,
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


def parallel(number_of_threads: int, project_id: str, bucket_name: str,
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

project_name = 'idc-tcia'
d_bucket_name = 'idc-tcia-tcga-kich'
d_folder = 'dicom/1.3.6.1.4.1.14519.5.2.1.1357.4011.125120931083013189922694218456/1.3.6.1.4.1.14519.5.2.1.1357.4011.213846823699400886279698296072/'
u_bucket_name = 'preformance-test'

create_bucket(project_name, u_bucket_name, True)
home = os.path.expanduser("~")
local_tmp_folder = os.path.join(home,"Tmp")
if os.path.exists(local_tmp_folder):
    shutil.rmtree(local_tmp_folder)

local_d_folder = os.path.join(local_tmp_folder, 'download')
serial(project_name, d_bucket_name, d_folder,
       local_d_folder, u_bucket_name)




