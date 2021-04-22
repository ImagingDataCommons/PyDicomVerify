from gcloud.bigquery_tools import (
    create_all_tables,
    query_string,
    query_string_with_result
)
from gcloud.storage_tools import (
    download_blob,
    upload_blob,
    exists_bucket,
    list_blobs,
    create_bucket,
    delete_bucket
)
import common.common_tools as ct
import common.parallelization as pl
from datetime import timedelta
import time


def get_bucket_size(project_id: str, bucket_name:str):
    blob_list = list_blobs(project_id, bucket_name)
    size = float(0)
    for bl in blob_list:
        size += bl.size
        # print(size)
    return (bucket_name, size)

def show_progress(start_time):
    n = 5
    toc = time.time()
    e_sec = round(toc - start_time)
    nn = e_sec % n
    e_t = timedelta(seconds=e_sec)
    dots = ''
    for i in range(n):
        if i <= nn:
            dots += ' .'
        else:
            dots += '  '
    print(
        "WAIT UNTIL FETCH THE "
        "BUCKET SIZES. ELAPSED TIME: {} {}".format(dots, e_t),
        flush=True, end='\r')

if __name__ == '__main__':
    progress = pl.Periodic(show_progress, [time.time()], .5)
    progress.start()
    collection_query = """
        SELECT DISTINCT GCS_BUCKET FROM 
        `{}` 
        ORDER BY GCS_BUCKET
    """.format('canceridc-data.idc_views.dicom_all')
    q_results = query_string_with_result(
        collection_query, project_name='idc-tcia')
    all_sizes = {}
    whole_siz = 0.0
    pss = pl.ProcessPool(16, 'size')
    for row in q_results:
        bucket_name = row.GCS_BUCKET
        pss.queue.put(
            (
                get_bucket_size,
                ('idc-tcia', bucket_name,),
            )
        )
    pss.queue.join()
    pss.kill_them_all()
    progress.kill_timer()
    for args, (bucket_name, b_size) in pss.output:
        all_sizes[bucket_name] = (b_size, ct.get_human_readable_string(b_size))
        print(ct.get_human_readable_string(b_size))
        whole_siz += b_size
    print(whole_siz)
    all_sizes['whole'] = (
        whole_siz, ct.get_human_readable_string(whole_siz))
    print(ct.dict2str(all_sizes))
