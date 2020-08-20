from google.cloud import storage


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def bucket_metadata(bucket_name):
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    print("ID: {}".format(bucket.id))
    print("Name: {}".format(bucket.name))
    print("Storage Class: {}".format(bucket.storage_class))
    print("Location: {}".format(bucket.location))
    print("Location Type: {}".format(bucket.location_type))
    print("Cors: {}".format(bucket.cors))
    print(
        "Default Event Based Hold: {}".format(bucket.default_event_based_hold)
    )
    print("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
    print("Metageneration: {}".format(bucket.metageneration))
    print(
        "Retention Effective Time: {}".format(
            bucket.retention_policy_effective_time
        )
    )
    print("Retention Period: {}".format(bucket.retention_period))
    print("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
    print("Requester Pays: {}".format(bucket.requester_pays))
    print("Self Link: {}".format(bucket.self_link))
    print("Time Created: {}".format(bucket.time_created))
    print("Versioning Enabled: {}".format(bucket.versioning_enabled))
    print("Labels:")
# gsutil cp -r gs://SOURCE_BUCKET/* gs://DESTINATION_BUCKET
# gsutil rm -r gs://SOURCE_BUCKET
# gsutil rm -a gs://SOURCE_BUCKET/**

def add_bucket_label(bucket_name):
    """Add a label to a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    labels = bucket.labels
    labels["example"] = "label"
    bucket.labels = labels
    bucket.patch()

    print("Updated labels on {}.".format(bucket.name))
    pprint.pprint(bucket.labels)

def get_bucket_labels(bucket_name):
    """Prints out a bucket's labels."""
    # bucket_name = 'your-bucket-name'
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)

    labels = bucket.labels
    pprint.pprint(labels)

def remove_bucket_label(bucket_name):
    """Remove a label from a bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    labels = bucket.labels

    if "example" in labels:
        del labels["example"]

    bucket.labels = labels
    bucket.patch()

    print("Removed labels on {}.".format(bucket.name))
    pprint.pprint(bucket.labels)

def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print("Bucket {} deleted".format(bucket.name))