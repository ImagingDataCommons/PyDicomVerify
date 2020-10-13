from BigQueryStuff import create_all_tables,\
                          query_string,\
                          query_string_with_result
from StorageBucketStuff import download_blob, upload_blob, exists_bucket,\
    list_blobs, create_bucket,empty_bukcet, delete_bucket
import common.common_tools as ct
import parallelization as pl


def get_bucket_size(project_id: str, bucket_name:str):
    blob_list = list_blobs(project_id, bucket_name)
    size = float(0)
    for bl in blob_list:
        size += bl.size
        # print(size)
    return (bucket_name, size)
collection_query = """
            WITH DICOMS AS (
            SELECT SOPINSTANCEUID  
            FROM {} 
            WHERE
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.2" OR 
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.4" OR 
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.128" 
                 ) 
                SELECT DISTINCT 
                    COLLECTION_TABLE.GCS_Bucket, 
                FROM DICOMS JOIN 
                    {} AS 
                    COLLECTION_TABLE ON 
                    COLLECTION_TABLE.SOPINSTANCEUID = DICOMS.SOPINSTANCEUID 
""".format('`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_dicom_metadata`', 
           '`idc-dev-etl.idc_tcia_mvp_wave0.idc_tcia_auxilliary_metadata`')
q_results = query_string_with_result(collection_query)
all_sizes = {}
whole_siz = 0.0
ths = pl.ThreadPool(pl.MAX_NUMBER_OF_THREADS, 'size')
for row in q_results:
    bucket_name = row.GCS_Bucket
    ths.queue.put(
        (
            get_bucket_size,
            ('idc-tcia', bucket_name,),
        )
    )
ths.queue.join()
ths.kill_them_all()
for bucket_name, b_size in ths.output:
    all_sizes[bucket_name] = (b_size, ct.get_human_readable_string(b_size))
    print(ct.get_human_readable_string(b_size))
    whole_siz += b_size
all_sizes['whole'] = (whole_siz, ct.get_human_readable_string(whole_siz))
print(all_sizes)