from googleapiclient import discovery
import json

def get_client():
    """Returns an authorized API client by discovering the Healthcare API and
    creating a service object using the service account credentials in the
    GOOGLE_APPLICATION_CREDENTIALS environment variable."""
    api_version = "v1"
    service_name = "healthcare"
    return discovery.build(service_name, api_version)

def create_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Creates a new DICOM store within the parent dataset."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .create(parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
    )
    response = request.execute()
    print("Created DICOM store: {}".format(dicom_store_id))
    return response

def delete_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Deletes the specified DICOM store."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .delete(name=dicom_store_name)
    )
    response = request.execute()
    print("Deleted DICOM store: {}".format(dicom_store_id))
    return response

def get_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Gets the specified DICOM store."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    dicom_stores = client.projects().locations().datasets().dicomStores()
    dicom_store = dicom_stores.get(name=dicom_store_name).execute()
    print(json.dumps(dicom_store, indent=2))
    return dicom_store

def list_dicom_stores(project_id, cloud_region, dataset_id):
    """Lists the DICOM stores in the given dataset."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_stores = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .list(parent=dicom_store_parent)
        .execute()
        .get("dicomStores", [])
    )
    for dicom_store in dicom_stores:
        print(dicom_store)
    return dicom_stores

def exists_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Lists the DICOM stores in the given dataset."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_stores = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .list(parent=dicom_store_parent)
        .execute()
        .get("dicomStores", [])
    )
    for dicom_store in dicom_stores:
        if dicom_store['name'].endswith(dicom_store_id):
            return True
    return False

def patch_dicom_store(
    project_id, cloud_region, dataset_id, dicom_store_id, pubsub_topic
):
    """Updates the DICOM store."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    patch = {
        "notificationConfig": {
            "pubsubTopic": "projects/{}/topics/{}".format(project_id, pubsub_topic)
        }
    }
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .patch(name=dicom_store_name, updateMask="notificationConfig", body=patch)
    )
    response = request.execute()
    print(
        "Patched DICOM store {} with Cloud Pub/Sub topic: {}".format(
            dicom_store_id, pubsub_topic
        )
    )
    return response


def export_dicom_instance_bigquery(
    dicomstore_project_id,
    dicomstore_cloud_region,
    dicomstore_dataset_id,
    dicom_store_id,
    bigquery_project_id,
    bigquery_dataset_id,
    bigquery_table_id
):
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        dicomstore_project_id, dicomstore_cloud_region, dicomstore_dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(
        dicom_store_parent,
        dicom_store_id)
    uri_prefix = '{}.{}.{}'.format(
        dicomstore_project_id,
        bigquery_dataset_id,
        bigquery_table_id)
    body = {"bigqueryDestination": {"tableUri": "bq://{}".format(uri_prefix)}}
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .export(name=dicom_store_name, body=body)
    )
    response = request.execute()
    # print("Exported DICOM instances to bigquery: bq://{}".format(uri_prefix))
    return response

def export_dicom_instance(
    project_id, cloud_region, dataset_id, dicom_store_id, uri_prefix
):
    """Export data to a Google Cloud Storage bucket by copying
    it from the DICOM store."""
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    body = {"gcsDestination": {"uriPrefix": "gs://{}".format(uri_prefix)}}
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .export(name=dicom_store_name, body=body)
    )
    response = request.execute()
    print("Exported DICOM instances to bucket: gs://{}".format(uri_prefix))
    return response

def import_dicom_instance(
    project_id, cloud_region, dataset_id, dicom_store_id, content_uri
):
    """Import data into the DICOM store by copying it from the specified
    source.
    """
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, cloud_region, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    body = {"gcsSource": {"uri": "gs://{}".format(content_uri)}}
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .import_(name=dicom_store_name, body=body)
    )
    response = request.execute()
    print("Imported DICOM instance: {}".format(content_uri))
    return response

def create_dataset(project_id, cloud_region, dataset_id):
    """Creates a dataset."""
    client = get_client()
    dataset_parent = 'projects/{}/locations/{}'.format(
        project_id, cloud_region)
    request = client.projects().locations().datasets().create(
        parent=dataset_parent, body={}, datasetId=dataset_id)
    response = request.execute()
    print('Created dataset: {}'.format(dataset_id))
    return response

def delete_dataset(project_id, cloud_region, dataset_id):
    """Deletes a dataset."""
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    request = client.projects().locations().datasets().delete(
        name=dataset_name)
    response = request.execute()
    print('Deleted dataset: {}'.format(dataset_id))
    return response

def get_dataset(project_id, cloud_region, dataset_id):
    """Gets any metadata associated with a dataset."""
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    datasets = client.projects().locations().datasets()
    dataset = datasets.get(name=dataset_name).execute()
    print('Name: {}'.format(dataset.get('name')))
    print('Time zone: {}'.format(dataset.get('timeZone')))
    return dataset

def list_datasets(project_id, cloud_region):
    """Lists the datasets in the project."""
    client = get_client()
    dataset_parent = 'projects/{}/locations/{}'.format(
        project_id, cloud_region)
    datasets = client.projects().locations().datasets().list(
        parent=dataset_parent).execute().get('datasets', [])
    for dataset in datasets:
        print('Dataset: {}\nTime zone: {}'.format(
            dataset.get('name'),
            dataset.get('timeZone')
        ))
    return datasets

def exists_dataset(project_id, cloud_region, dataset_id):
    """Lists the datasets in the project."""
    client = get_client()
    dataset_parent = 'projects/{}/locations/{}'.format(
        project_id, cloud_region)
    datasets = client.projects().locations().datasets().list(
        parent=dataset_parent).execute().get('datasets', [])
    for dataset in datasets:
        if dataset['name'].endswith(dataset_id):
            return True
    return False

def patch_dataset(project_id, cloud_region, dataset_id, time_zone):
    """Updates dataset metadata."""
    client = get_client()
    dataset_parent = 'projects/{}/locations/{}'.format(
        project_id, cloud_region)
    dataset_name = '{}/datasets/{}'.format(dataset_parent, dataset_id)
    # Sets the time zone to GMT
    patch = {
        'timeZone': time_zone
    }
    request = client.projects().locations().datasets().patch(
        name=dataset_name, updateMask='timeZone', body=patch)
    response = request.execute()
    print(
        'Patched dataset {} with time zone: {}'.format(
            dataset_id,
            time_zone))
    return response

def deidentify_dataset(
        project_id,
        cloud_region,
        dataset_id,
        destination_dataset_id,
        keeplist_tags):
    """Creates a new dataset containing de-identified data
    from the source dataset.
    """
    client = get_client()
    source_dataset = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    destination_dataset = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, destination_dataset_id)
    body = {
        'destinationDataset': destination_dataset,
        'config': {
            'dicom': {
                'keepList': {
                    'tags': [
                        'Columns',
                        'NumberOfFrames',
                        'PixelRepresentation',
                        'MediaStorageSOPClassUID',
                        'MediaStorageSOPInstanceUID',
                        'Rows',
                        'SamplesPerPixel',
                        'BitsAllocated',
                        'HighBit',
                        'PhotometricInterpretation',
                        'BitsStored',
                        'PatientID',
                        'TransferSyntaxUID',
                        'SOPInstanceUID',
                        'StudyInstanceUID',
                        'SeriesInstanceUID',
                        'PixelData'
                    ]
                }
            }
        }
    }
    request = client.projects().locations().datasets().deidentify(
        sourceDataset=source_dataset, body=body)
    response = request.execute()
    print(
        'Data in dataset {} de-identified.'
        'De-identified data written to {}'.format(
            dataset_id,
            destination_dataset_id))
    return response

def get_dataset_iam_policy(project_id, cloud_region, dataset_id):
    """Gets the IAM policy for the specified dataset."""
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    request = client.projects().locations().datasets().getIamPolicy(
        resource=dataset_name)
    response = request.execute()
    print('etag: {}'.format(response.get('name')))
    return response

def set_dataset_iam_policy(
        project_id,
        cloud_region,
        dataset_id,
        member,
        role,
        etag=None):
    """Sets the IAM policy for the specified dataset.
        A single member will be assigned a single role. A member can be any of:
        - allUsers, that is, anyone
        - allAuthenticatedUsers, anyone authenticated with a Google account
        - user:email, as in 'user:somebody@example.com'
        - group:email, as in 'group:admins@example.com'
        - domain:domainname, as in 'domain:example.com'
        - serviceAccount:email,
            as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
        A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
        or 'roles/editor'
    """
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    policy = {
        "bindings": [
            {
                "role": role,
                "members": [
                    member
                ]
            }
        ]
    }
    if etag is not None:
        policy['etag'] = etag
    request = client.projects().locations().datasets().setIamPolicy(
        resource=dataset_name, body={'policy': policy})
    response = request.execute()
    print('etag: {}'.format(response.get('name')))
    print('bindings: {}'.format(response.get('bindings')))
    return response
# [END healthcare_dataset_set_iam_policy]