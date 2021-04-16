from google.cloud import storage
import inspect
import sys, os
import logging
import time
import common.common_tools as ct
import common.parallelization as parallel
from requests.exceptions import RequestException

def create_bucket(project_id: str, bucket_name: str, replace: bool = False):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"
    if exists_bucket(project_id, bucket_name) and replace:
        delete_bucket(project_id, bucket_name)
    elif exists_bucket(project_id, bucket_name) and not replace:
        return        
    storage_client = storage.Client(project_id)
    bucket = storage_client.create_bucket(bucket_name)
    logger = logging.getLogger(__name__)
    logger.debug("Bucket {} created".format(bucket.name))



def list_blobs(project_id: str, bucket_name: str, prefix: str = None):

    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"
    logger = logging.getLogger(__name__)
    max_retries = 30
    retries = 0
    blobs = []
    logger.debug("project_id: {}, bucket_name: {}, prefix: {}".format(
        project_id, bucket_name, prefix))
    while retries < max_retries:
        try:
            storage_client = storage.Client(project_id)
            logger.debug(
                "After building clietn object and before "
                "construction a bucket object <{}>".format(project_id))
            bucket_obj = storage_client.bucket(bucket_name, project_id)
            logger.debug(
                "After construction a bucket object <{}> and"
                " before retrieving blob list".format(bucket_name))
            if prefix is None:
                blobs = storage_client.list_blobs(bucket_obj, timeout=5)
            else:
                blobs = storage_client.list_blobs(
                    bucket_obj, prefix=prefix, delimiter=None, timeout=5)
            break
        except Exception as err:
            retries += 1
            if retries % 5 == 0 and retries < max_retries:
                logger.info("Couldn't load blobs, retry number {}".format(
                    retries))
            else:
                logger.error(err, exc_info=True)
                logger.debug(
                    "Couln't retrieve blob list after {} retries".format(
                        retries)) 
    return blobs


def list_buckets(project_id: str):
    """Lists all buckets."""

    storage_client = storage.Client(project_id)
    buckets = storage_client.list_buckets()
    logger = logging.getLogger(__name__)
    for bucket in buckets:
        logger.debug('{}{}'.format(bucket.name))


def bucket_metadata(project_id: str, bucket_name: str):
    logger = logging.getLogger(__name__)
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client(project_id)
    bucket_obj = storage_client.bucket(bucket_name, project_id)
    bucket = storage_client.get_bucket(bucket_obj)
    
    logger.debug("ID: {}".format(bucket.id))
    logger.debug("Name: {}".format(bucket.name))
    logger.debug("Storage Class: {}".format(bucket.storage_class))
    logger.debug("Location: {}".format(bucket.location))
    logger.debug("Location Type: {}".format(bucket.location_type))
    logger.debug("Cors: {}".format(bucket.cors))
    logger.debug("Default Event Based Hold: {}".format(
        bucket.default_event_based_hold)
    )
    logger.debug("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
    logger.debug("Metageneration: {}".format(bucket.metageneration))
    logger.debug("Retention Effective Time: {}".format(
            bucket.retention_policy_effective_time
        )
    )
    logger.debug("Retention Period: {}".format(bucket.retention_period))
    logger.debug("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
    logger.debug("Requester Pays: {}".format(bucket.requester_pays))
    logger.debug("Self Link: {}".format(bucket.self_link))
    logger.debug("Time Created: {}".format(bucket.time_created))
    logger.debug("Versioning Enabled: {}".format(bucket.versioning_enabled))
    logger.debug("Labels:")
# gsutil cp -r gs://SOURCE_BUCKET/* gs://DESTINATION_BUCKET
# gsutil rm -r gs://SOURCE_BUCKET
# gsutil rm -a gs://SOURCE_BUCKET/**


def add_bucket_label(project_id: str, bucket_name: str):
    logger = logging.getLogger(__name__)
    """Add a label to a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client(project_id)

    bucket_obj = storage_client.bucket(bucket_name, project_id)
    bucket = storage_client.get_bucket(bucket_obj)
    labels = bucket.labels
    labels["example"] = "label"
    bucket.labels = labels
    bucket.patch()

    logger.debug("Updated labels on {}.".format(bucket.name))
    # pprint.pprint(bucket.labels)


def get_bucket_labels(project_id: str, bucket_name: str):
    logger = logging.getLogger(__name__)
    """Prints out a bucket's labels."""
    # bucket_name = 'your-bucket-name'
    storage_client = storage.Client(project_id)

    bucket_obj = storage_client.bucket(bucket_name, project_id)
    bucket = storage_client.get_bucket(bucket_obj)

    labels = bucket.labels
    # pprint.pprint(labels)


def remove_bucket_label(project_id: str, bucket_name: str):
    logger = logging.getLogger(__name__)
    """Remove a label from a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client(project_id)
    bucket_obj = storage_client.bucket(bucket_name, project_id)
    bucket = storage_client.get_bucket(bucket_obj)

    labels = bucket.labels

    if "example" in labels:
        del labels["example"]

    bucket.labels = labels
    bucket.patch()

    logger.debug("Removed labels on {}.".format(bucket.name))
    # pprint.pprint(bucket.labels)


def delete_bucket(project_id: str, bucket_name: str):
    logger = logging.getLogger(__name__)
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"
    logger.debug(
        "project_id: {}, bucket_name: {}".format(project_id, bucket_name))
    storage_client = storage.Client(project_id)

    bucket_obj = storage_client.bucket(bucket_name, project_id)
    bucket = storage_client.get_bucket(bucket_obj)
    bucket.delete(force=True)

    logger.info("Bucket {} deleted".format(bucket.name))


def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    logger = logging.getLogger(__name__)
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"
    
    storage_client = storage.Client(project_id)

    source_bucket = storage_client.bucket(bucket_name, project_id)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    logger.debug("Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


def get_blob(project_id: str, bucket_name: str, blob_name) -> bool:
    """ retrieves a blob from the bucket."""
    logger = logging.getLogger(__name__)
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    logger.debug("project_id: {}, bucket_name: {}, blob_name: {}".format(
        project_id, bucket_name, blob_name))
    retries = 0
    max_retries = 30
    bl = None
    while retries < max_retries:
        try:
            storage_client = storage.Client(project_id,)
            bucket = storage_client.bucket(bucket_name, project_id)
            bl = bucket.get_blob(blob_name, timeout=5)
            break
        except BaseException as err:
            retries += 1
            if retries < max_retries:
                if retries % 10 == 0:
                    logger.info(
                        "couldn't get the blob. retry number {}".format(
                            retries))
            else:
                logger.error(err, exc_info=True)
    return bl


def delete_blob(project_id: str, bucket_name: str, blob_name) -> bool:
    logger = logging.getLogger(__name__)
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    logger.debug("project_id: {}, bucket_name: {}, blob_name: {}".format(
        project_id, bucket_name, blob_name))
    storage_client = storage.Client(project_id)

    bucket = storage_client.bucket(bucket_name, project_id)
    blob = bucket.blob(blob_name)
    ct.retry_if_failes(blob.delete, None, 30, 10, True, 10)
    return True



def download_blob(project_id: str, bucket_name: str,
                  source_blob_name, destination_file_name) -> bool:
    logger = logging.getLogger(__name__)
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"
    logger.debug(
        "project_id: {}, bucket_name: {}, src_blob_name: {}, \n"
        "dest_file_name: {}".format(
            project_id, bucket_name, source_blob_name, destination_file_name))
    storage_client = storage.Client(project_id)

    bucket = storage_client.bucket(bucket_name, project_id)
    blob = bucket.blob(source_blob_name)
    parent_folder = os.path.dirname(destination_file_name)
    if not os.path.exists(parent_folder) and parent_folder != '':
        os.makedirs(parent_folder)
    maximum_retry = 15
    retries = 0
    success = False
    try:
        ct.retry_if_failes(
            blob.download_to_filename, (destination_file_name,),
            maximum_retry, 10, True, 10)
        success = True
    except BaseException as err:
        success = False
    # while retries < maximum_retry:
    #     try:
    #         blob.download_to_filename(destination_file_name)
    #         logger.debug("Blob {} downloaded to {}.".format(
    #             source_blob_name, destination_file_name))
    #         success = True
    #         break
    #     except BaseException as err:
    #         retries += 1
    #         if retries >= maximum_retry:
    #             logger.error(
    #                 "after {} retries couldn't "
    #                 "download the file\n{}\n{} ".format(
    #                     retries, destination_file_name, err), exc_info=True)
    #             break
    #         else:
    #             if retries % 10 == 0:
    #                 logger.info(
    #                     '({})retrying connection for file \n{}'.format(
    #                         retries, destination_file_name))
    return success


def upload_blob(project_id: str, bucket_name: str,
                destination_blob_name, source_file_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"
    logger = logging.getLogger(__name__)
    logger.debug(
        "project_id: {}, bucket_name: {}, dest_blob_name: {}, \n"
        "src_file_name: {}".format(
            project_id, bucket_name, destination_blob_name, source_file_name))
    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name, project_id)
    blob = bucket.blob(destination_blob_name)
    maximum_retry = 15
    retries = 0
    success = False
    try:
        ct.retry_if_failes(
            blob.upload_from_filename, (source_file_name,),
            maximum_retry, 10, True, 10)
        success = True
    except BaseException as err:
        success = False
    # while retries < maximum_retry:
    #     try:
    #         blob.upload_from_filename(source_file_name)
    #         logger.debug("File {} uploaded to {}.".format(
    #                 source_file_name, destination_blob_name
    #             )
    #         )
    #         success = True
    #         break
    #     except BaseException as err:
    #         retries += 1
    #         if retries >= maximum_retry:
    #             logger.error(
    #                 "after {} retries couldn't upload the file\n{}\n{}".format(
    #                     retries, source_file_name, err), exc_info=True)
    #             break
    #         else:
    #             if retries % 5 == 0:
    #                 logger.info(
    #                     '({})retrying connection for file \n{}'.format(
    #                         retries, source_file_name))
    return success


def exists_bucket(project_id: str, bucket_name: str) -> bool:
    storage_client = storage.Client(project_id)
    try:
        bucket_obj = storage_client.bucket(bucket_name, project_id)
        bucket = storage_client.get_bucket(bucket_obj)
        return True
    except:
        return False


def delete_blob_directly(blob) -> bool:
    # logger = logging.getLogger(__name__)
    max_retries = 30
    # retries = 0
    success = False
    success = ct.retry_if_failes(blob.delete, None, max_retries, 10, True, 10)
    # return True
    # while True:
    #     try:
    #         blob.delete()
    #         logger.debug("Blob {} deleted.".format(blob))
    #         success = True
    #         break
    #     except BaseException as err:
    #         if retries >= max_retries:
    #             logger.error(
    #                 "after {} retries couldn't "
    #                 "delete the file\n{}\n{} ".format(
    #                     retries, blob, err), exc_info=True)
    #             break
    #         else:
    #             logger.info(
    #                 '({})retrying connection for file \n{}'.format(
    #                     retries, blob))
    return success