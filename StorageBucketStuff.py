from google.cloud import storage
import inspect
import sys, os
import logging
import common_tools as ct

def create_bucket(project_id: str, bucket_name: str, replace: bool = False):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"
    if exists_bucket(project_id, bucket_name) and replace:
        delete_bucket(project_id, bucket_name)
    elif exists_bucket(project_id, bucket_name) and not replace:
        return        
    storage_client = storage.Client(project_id)
    bucket = storage_client.create_bucket(bucket_name)
    (logger, indent) = ct.GetFunctionLugger()
    logger.debug("{}Bucket {} created".format(indent, bucket.name))

def list_buckets(project_id: str):
    """Lists all buckets."""

    storage_client = storage.Client(project_id)
    buckets = storage_client.list_buckets()
    (logger, indent) = ct.GetFunctionLugger()
    for bucket in buckets:
        logger.debug('{}{}'.format(indent, bucket.name))


def bucket_metadata(project_id: str, bucket_name: str):
    (logger, indent) = ct.GetFunctionLugger()
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client(project_id)
    bucket = storage_client.get_bucket(bucket_name)
    
    logger.debug("{}ID: {}".format(indent, bucket.id))
    logger.debug("{}Name: {}".format(indent, bucket.name))
    logger.debug("{}Storage Class: {}".format(indent, bucket.storage_class))
    logger.debug("{}Location: {}".format(indent, bucket.location))
    logger.debug("{}Location Type: {}".format(indent, bucket.location_type))
    logger.debug("{}Cors: {}".format(indent, bucket.cors))
    logger.debug("{}Default Event Based Hold: {}".format(indent, bucket.default_event_based_hold)
    )
    logger.debug("{}Default KMS Key Name: {}".format(indent, bucket.default_kms_key_name))
    logger.debug("{}Metageneration: {}".format(indent, bucket.metageneration))
    logger.debug("{}Retention Effective Time: {}".format(indent, 
            bucket.retention_policy_effective_time
        )
    )
    logger.debug("{}Retention Period: {}".format(indent, bucket.retention_period))
    logger.debug("{}Retention Policy Locked: {}".format(indent, bucket.retention_policy_locked))
    logger.debug("{}Requester Pays: {}".format(indent, bucket.requester_pays))
    logger.debug("{}Self Link: {}".format(indent, bucket.self_link))
    logger.debug("{}Time Created: {}".format(indent, bucket.time_created))
    logger.debug("{}Versioning Enabled: {}".format(indent, bucket.versioning_enabled))
    logger.debug("{}Labels:")
# gsutil cp -r gs://SOURCE_BUCKET/* gs://DESTINATION_BUCKET
# gsutil rm -r gs://SOURCE_BUCKET
# gsutil rm -a gs://SOURCE_BUCKET/**


def add_bucket_label(project_id: str, bucket_name: str):
    (logger, indent) = ct.GetFunctionLugger()
    """Add a label to a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client(project_id)

    bucket = storage_client.get_bucket(bucket_name)
    labels = bucket.labels
    labels["example"] = "label"
    bucket.labels = labels
    bucket.patch()

    logger.debug("{}Updated labels on {}.".format(indent, bucket.name))
    pprint.pprint(bucket.labels)


def get_bucket_labels(project_id: str, bucket_name: str):
    (logger, indent) = ct.GetFunctionLugger()
    """Prints out a bucket's labels."""
    # bucket_name = 'your-bucket-name'
    storage_client = storage.Client(project_id)

    bucket = storage_client.get_bucket(bucket_name)

    labels = bucket.labels
    pprint.pprint(labels)


def remove_bucket_label(project_id: str, bucket_name: str):
    (logger, indent) = ct.GetFunctionLugger()
    """Remove a label from a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client(project_id)
    bucket = storage_client.get_bucket(bucket_name)

    labels = bucket.labels

    if "example" in labels:
        del labels["example"]

    bucket.labels = labels
    bucket.patch()

    logger.debug("{}Removed labels on {}.".format(indent, bucket.name))
    pprint.pprint(bucket.labels)


def delete_bucket(project_id: str, bucket_name: str):
    (logger, indent) = ct.GetFunctionLugger()
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client(project_id)

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    logger.debug("{}Bucket {} deleted".format(indent, bucket.name))


def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    (logger, indent) = ct.GetFunctionLugger()
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client(project_id)

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    logger.debug("{}Blob {} in bucket {} copied to blob {} in bucket {}.".format(indent, 
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


def delete_blob(project_id: str, bucket_name: str, blob_name):
    (logger, indent) = ct.GetFunctionLugger()
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client(project_id)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    logger.debug("{}Blob {} deleted.".format(indent, blob_name))


def download_blob(project_id: str, bucket_name: str, source_blob_name, destination_file_name):
    (logger, indent) = ct.GetFunctionLugger()
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client(project_id)

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    parent_folder = os.path.dirname(destination_file_name)
    if not os.path.exists(parent_folder):
        os.makedirs(parent_folder)

    blob.download_to_filename(destination_file_name)
    logger.debug("{}Blob {} downloaded to {}.".format(indent, 
            source_blob_name, destination_file_name
        )
    )


def upload_blob(project_id: str, bucket_name: str, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    (logger, indent) = ct.GetFunctionLugger()
    logger.debug("{}File {} uploaded to {}.".format(indent, 
            source_file_name, destination_blob_name
        )
    )


def exists_bucket(project_id: str, bucket_name: str) -> bool:
    storage_client = storage.Client(project_id)
    try:
        bucket = storage_client.get_bucket(bucket_name)
        return True
    except:
        return False