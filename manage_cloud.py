from gcloud.BigQueryStuff import *
from gcloud.DicomStoreStuff import *
from gcloud.DicomWebStuff import *
from gcloud.StorageBucketStuff import *
import re

def print_list(list_: list, pr: bool = True, ):
    str_ = '[\n{}]'
    content = ''
    for element in list_:
        content += "    '{}',\n".format(element)
    output = str_.format(content)
    if pr:
        print(output)
    return output

def print_dict(dict_: dict, pr: bool = True):
    output = '{{\n{}}}'
    contents = ''
    for key, val in dict_.items():
        contents += '    {}: {},\n'.format(key, print_list(val, False))
    output = output.format(contents)
    if pr:
        print(output)
    return output

proj_id = 'idc-tcia'
cloud_region = 'us'
# bq_ds = list_bq_dataset_names(proj_id)
# print_list(bq_ds)
# want_to_delete = [
#     'idc-tcia.afshin_results_02_idc_tcia_mvp_wave0',
# ]
# for dl in want_to_delete:
# #     delete_bq_dataset(dl)
# ll = list_datasets_and_dicomstores(proj_id, cloud_region)
# print_list(ll)
dicom_stores = [
    'projects/idc-tcia/locations/us/datasets/afshin_tests/dicomStores/xx00',

]
# for dstore in dicom_stores:
#     # exists_dicom_store()
#     delete_dicom_store_directly(dstore)
dicom_store = 'xx00'
dataset = 'afshin_tests'
delete_dataset_directly('projects/idc-tcia/locations/us/datasets/afshin_tests')
# create_dataset(proj_id, cloud_region, dataset)
# create_dicom_store(proj_id, cloud_region, dataset, dicom_store)
# recreate_dataset(proj_id, cloud_region, dataset)
ll = list_datasets(proj_id, cloud_region)
print_list(ll)


# gcloud healthcare dicom-stores create 'ff' --dataset='afshin_test_dataset_form_gcloud' --location='us' --pubsub-topic="projects/idc-tcia"
# gcloud healthcare dicom-stores create 'FIXED' --dataset='afshin_results_00_idc_tcia_mvp_wave0' --location='us' --pubsub-topic="projects/idc-tcia"
#   projects/idc-tcia/locations/us/datasets/afshin_results_00_idc_tcia_mvp_wave0 (or it may be malformed or not exist
# gcloud healthcare dicom-store  create --dataset=DATASET_ID