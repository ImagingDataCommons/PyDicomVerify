import logging
import logging.config
import os
import pydicom
import shutil
import common.common_tools as ctools
import common.parallelization as pl


from gcloud.BigQueryStuff import (
    # FUNCTIONS
    query_string_with_result,
)
from gcloud.StorageBucketStuff import (
    # FUNCTIONS
    download_blob,
    list_blobs,
)
from multiprocessing import (
    # SUBMODULES
    freeze_support,
)

import json

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': './Logs/sampling_log.log',  # Default is stderr
            "mode": "w",
        },
    },
    'loggers': {
        'xxx': {  # root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    'root': {  # root logger
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': False
        }
}
logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger(__name__)
log.debug("Logging is configured.")
anatomic_attribs = ["ImageLaterality" ,
"BodyPartExamined",
"FrameAnatomySequence",
"AnatomicRegionSequence",]


def download_parallel(blob_list: list, destination_dir: str, bucket_name: str,
                      process_number: int=pl.MAX_NUMBER_OF_THREADS):
    logger = logging.getLogger(__name__)
    
    
    logger.info('Number of blobs to be downloaded {}'.format(len(blob_list)))
    if len(blob_list) == 0:
        return
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        # shutil.rmtree(destination_dir)
    ps = pl.ProcessPool(min(len(blob_list), process_number), 'down')
    dest_files = []
    for i, bl_name in enumerate(blob_list, 1):
        if i > 16:
            break
        file_name = bl_name.replace('gs://' + bucket_name + '/', '')
        dest_files.append( os.path.join(destination_dir, file_name))
        print(file_name)
        ps.queue.put(
            (
                download_blob,
                ('idc-tcia', bucket_name, file_name, os.path.join(
                    destination_dir, dest_files[-1])
                )
            ))
    ps.queue.join()
    ps.kill_them_all()
    return dest_files


def download_json(remote_file, local_file, data_folder):
    with open(remote_file) as json_file:
        jcontent = json.load(json_file)
    local_parent = os.path.dirname(local_file)
    if not os.path.exists(local_parent):
        os.makedirs(local_parent)
    all_series = jcontent['data']
    local_series = []
    for series in all_series:
        local_dict = {}
        for key, val in series.items():
            if key == 'SERIES_PATH':
                files = download_parallel(
                    val, data_folder, series['GCS_BUCKET'], 16)
                local_dict[key] = files
            elif key == 'INSTANCES':
                local_dict[key] = list(val[:16])
            else:
                local_dict[key] = val
        local_series.append(local_dict)
    whole = {'data': local_series}
    with open(local_file, 'w') as writej:
        json.dump(whole, writej, indent=4)


# if __name__ == '__main__':
#     freeze_support()
#     local = 'gitexcluded_local/0001.json'
#     remote = '/Users/afshin/Documents/work/VerifyDicom/gitexcluded_jsons/series_00000000.json'
#     download_json(remote, local, '/Users/afshin/Documents/work/VerifyDicom/gitexcluded_data')








