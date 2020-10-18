from googleapiclient import discovery
import json
import logging
import os
# client.projects().locations()
#     datasets
#     get
#     list
#     list_next
# client.projects().locations().datasets()
#     create
#     deidentify
#     delete
#     dicomStores
#     fhirStores
#     get
#     getIamPolicy
#     hl7V2Stores
#     list
#     list_next
#     operations
#     patch
#     setIamPolicy
#     testIamPermissions
# client.projects().locations().datasets().dicomStores()
#     create
#     deidentify
#     delete
#     dicomStores
#     fhirStores
#     get
#     getIamPolicy
#     hl7V2Stores
#     list
#     list_next
#     operations
#     patch
#     setIamPolicy
#     testIamPermissions
# client.projects().locations().datasets().dicomStores()
#     create
#     deidentify
#     delete
#     export
#     get
#     getIamPolicy
#     import_
#     list
#     list_next
#     patch
#     searchForInstances
#     searchForSeries
#     searchForStudies
#     setIamPolicy
#     storeInstances
#     studies
#     testIamPermissions
# client.projects().locations().datasets().fhirStores()
#     create
#     deidentify
#     delete
#     export
#     fhir
#     get
#     getIamPolicy
#     import_
#     list
#     list_next
#     patch
#     setIamPolicy
#     testIamPermissions
def get_entitiy_path(project_id: str, cloud_region: str = '',
                     dataset_id: str = '', dicom_store: str = ''):
    output = ''
    if project_id != '':
        output += 'projects/{}'.format(project_id)
    if cloud_region != '':
        output += '/locations/{}'.format(cloud_region)
    if dataset_id != '':
        output += '/datasets/{}'.format(dataset_id)
    if dicom_store != '':
        output += '/dicomStores/{}'.format(dicom_store)
    return output


def decompose_path(full_path: str) -> tuple:
    parent = os.path.dirname(os.path.dirname(full_path))
    entity = os.path.basename(full_path)
    return (parent, entity)
    

def get_client():
    """Returns an authorized API client by discovering the Healthcare API and
    creating a service object using the service account credentials in the
    GOOGLE_APPLICATION_CREDENTIALS environment variable."""
    logger = logging.getLogger(__name__)
    api_version = "v1"
    service_name = "healthcare"
    return discovery.build(service_name, api_version)


def create_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Creates a new DICOM store within the parent dataset."""
    logger = logging.getLogger(__name__)
    if not exists_dataset(project_id, cloud_region, dataset_id):
        logger.info(
            "Checked before createion of dicom store, "
            "parent-dataset {} doesn't exist.".format(dataset_id))
        create_dataset(project_id, cloud_region, dataset_id)
    dicom_store_full_name = get_entitiy_path(
        project_id, cloud_region, dataset_id, dicom_store_id)
    return create_dicom_store_direct(dicom_store_full_name)


def create_dicom_store_direct(dicom_store_full_path: str):
    """Creates a new DICOM store within the parent dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dicom_store_parent, dicom_store_id = decompose_path(dicom_store_full_path)
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .create(
            parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
    )
    response = request.execute()
    logger.info("Created DICOM store: {}".format(dicom_store_id))
    return response

def recreate_dicom_store(
        project_id, cloud_region, dataset_id, dicom_store_id):
    logger = logging.getLogger(__name__)
    if exists_dataset(project_id, cloud_region, dataset_id):
        if exists_dicom_store(
                project_id, cloud_region, dataset_id, dicom_store_id):
            delete_dicom_store(
                project_id, cloud_region, dataset_id, dicom_store_id)
            logger.info(
                "dicomstore {} from dicom dataset {} was "
                "successfully deleted".format(dicom_store_id, dataset_id))
    create_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id)


def delete_dicom_store_directly(dicom_store_path_name):
    """Deletes the specified DICOM store."""
    logger = logging.getLogger(__name__)
    client = get_client()
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .delete(name=dicom_store_path_name)
    )
    response = request.execute()
    logger.info("Deleted DICOM store: {}".format(dicom_store_path_name))
    return response


def delete_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Deletes the specified DICOM store."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dicom_store_name = get_entitiy_path(
        project_id, cloud_region, dataset_id, dicom_store_id)
    return delete_dicom_store_directly(dicom_store_name)



def get_dicom_store_directly(dicom_store_name: str):
    """Gets the specified DICOM store."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dicom_stores = client.projects().locations().datasets().dicomStores()
    dicom_store = dicom_stores.get(name=dicom_store_name).execute()
    logger.info(json.dumps(dicom_store, indent=2))
    return dicom_store



def get_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Gets the specified DICOM store."""
    dicom_store_name = get_entitiy_path(
        project_id, cloud_region, dataset_id, dicom_store_id)
    return get_dicom_store_directly(dicom_store_name)


def list_dicom_stores_directly(dicom_store_parent: str):
    """Lists the DICOM stores in the given dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
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
        logger.info(dicom_store)
    return dicom_stores


def list_dicom_stores(project_id, cloud_region, dataset_id):
    """Lists the DICOM stores in the given dataset."""
    dicom_store_parent = get_entitiy_path(project_id, cloud_region, dataset_id)
    return list_dicom_stores_directly(dicom_store_parent)


def exists_dicom_store(project_id, cloud_region, dataset_id, dicom_store_id):
    """Lists the DICOM stores in the given dataset."""
    dicom_store_full_path = get_entitiy_path(
        project_id, cloud_region, dataset_id, dicom_store_id)
    try:
        if not exists_dataset(project_id, cloud_region, dataset_id):
            return False
        else:
            return exists_dicom_store_directly(dicom_store_full_path)
    except BaseException as err:
        return False #  Meaning the project doesn't exist 


def exists_dicom_store_directly(dicom_store_full_path: str):
    """Lists the DICOM stores in the given dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dicom_store_parent, dicom_store_id = decompose_path(dicom_store_full_path)
    try:
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
    except BaseException:
        pass
    return False

def patch_dicom_store(
    project_id, cloud_region, dataset_id, dicom_store_id, pubsub_topic
):
    """Updates the DICOM store."""
    logger = logging.getLogger(__name__)
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
    logger.info(
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
    # logger.info("Exported DICOM instances to bigquery: bq://{}".format(uri_prefix))
    return response

def export_dicom_instance(
    project_id, cloud_region, dataset_id, dicom_store_id, uri_prefix
):
    """Export data to a Google Cloud Storage bucket by copying
    it from the DICOM store."""
    logger = logging.getLogger(__name__)
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
    logger.info("Exported DICOM instances to bucket: gs://{}".format(uri_prefix))
    return response

def import_dicom_bucket(
    dicom_dataset_project_id, 
    dicom_dataset_cloud_region, 
    dicom_dataset_id, dicom_store_id, 
    bucket_project_id,
    bucket_name,
    sub_bucket_name=None
    ):
    logger = logging.getLogger(__name__)
    client = get_client()
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        dicom_dataset_project_id, dicom_dataset_cloud_region, dicom_dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)
    sub_bucket = '' if sub_bucket_name is None else '{}/'.format(sub_bucket_name)
    body = {"gcsSource": {"uri": "gs://{}/{}**.dcm".format(bucket_name, sub_bucket_name)}}
    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .import_(name=dicom_store_name, body=body)
    )
    response = request.execute()
    logger.info("Imported DICOM instance: {}".format(bucket_name))
    return response


def import_dicom_instance(
    project_id, cloud_region, dataset_id, dicom_store_id, content_uri
):
    """Import data into the DICOM store by copying it from the specified
    source.
    """
    logger = logging.getLogger(__name__)
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
    logger.info("Imported DICOM instance: {}".format(content_uri))
    return response


def create_dataset(project_id, cloud_region, dataset_id):
    """Creates a dataset."""
    dataset_parent = get_entitiy_path(project_id, cloud_region)
    return create_dataset_directly(dataset_parent, dataset_id)


def create_dataset_directly(dataset_parent: str, dataset_id: str):
    """Creates a dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    request = client.projects().locations().datasets().create(
        parent=dataset_parent, body={}, datasetId=dataset_id)
    response = request.execute()
    logger.info('Created dataset: {}'.format(dataset_id))
    return response


def recreate_dataset(project_id: str, cloud_region: str, dataset_id: str):
    dataset_parent_fullname = get_entitiy_path(project_id, cloud_region)
    recreate_dataset_directly(dataset_parent_fullname, dataset_id)


def recreate_dataset_directly(dataset_parent_fullname: str, dataset_id: str):
    if exists_dataset_directly(dataset_parent_fullname, dataset_id):
        delete_dataset_directly('{}/datasets/{}'.format(
            dataset_parent_fullname, dataset_id))
    create_dataset_directly(dataset_parent_fullname, dataset_id)


def delete_dataset(project_id, cloud_region, dataset_id):
    """Deletes a dataset."""
    dataset_name = get_entitiy_path(project_id, cloud_region, dataset_id)
    return delete_dataset_directly(dataset_name)


def delete_dataset_directly(dataset_name: str):
    """Deletes a dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    request = client.projects().locations().datasets().delete(
        name=dataset_name)
    response = request.execute()
    logger.info('Deleted dataset: {}'.format(dataset_name))
    return response


def get_dataset(project_id, cloud_region, dataset_id):
    """Gets any metadata associated with a dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    datasets = client.projects().locations().datasets()
    dataset = datasets.get(name=dataset_name).execute()
    logger.info('Name: {}'.format(dataset.get('name')))
    logger.info('Time zone: {}'.format(dataset.get('timeZone')))
    return dataset


def list_datasets_and_dicomstores(project_id, cloud_region):
    """Lists the datasets in the project."""
    logger = logging.getLogger(__name__)
    client = get_client()
    output = []
    dataset_parent = 'projects/{}/locations/{}'.format(
        project_id, cloud_region)
    datasets = client.projects().locations().datasets().list(
        parent=dataset_parent).execute().get('datasets', [])
    for dataset in datasets:
        logger.info('Dataset: {}\nTime zone: {}'.format(
            dataset.get('name'),
            dataset.get('timeZone')
        ))
        dicom_stores = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .list(parent=dataset['name'])
            .execute().get("dicomStores", []))
        for dstore in dicom_stores:
            output.append(dstore["name"])
    output.sort()
    return output


def list_datasets(project_id: str, cloud_region: str):
    """Lists the datasets in the project."""
    dataset_parent = get_entitiy_path(project_id, cloud_region)
    return list_datasets_directly(dataset_parent)


def list_datasets_directly(dataset_parent: str):
    """Lists the datasets in the project."""
    logger = logging.getLogger(__name__)
    client = get_client()
    datasets = client.projects().locations().datasets().list(
        parent=dataset_parent).execute().get('datasets', [])
    output = []
    for dataset in datasets:
        logger.info('Dataset: {}\nTime zone: {}'.format(
            dataset.get('name'),
            dataset.get('timeZone')
        ))
        output.append(dataset['name'])
    return output


def exists_dataset_directly(dataset_full_name: str):
    """Lists the datasets in the project."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dataset_id = os.path.basename(dataset_full_name)
    dataset_parent = os.path.dirname(os.path.dirname(dataset_full_name))
    datasets = client.projects().locations().datasets().list(
        parent=dataset_parent).execute().get('datasets', [])
    for dataset in datasets:
        if dataset['name'].endswith(dataset_id):
            logger.info('dataset {} exists'.format(dataset_id))
            return True
    logger.info("dataset {} doesn't exists".format(dataset_id))
    return False


def exists_dataset(project_id, cloud_region, dataset_id):
    """Lists the datasets in the project."""
    dataset_full_name = get_entitiy_path(project_id, cloud_region, dataset_id)
    return exists_dataset_directly(dataset_full_name)


def patch_dataset(project_id, cloud_region, dataset_id, time_zone):
    """Updates dataset metadata."""
    logger = logging.getLogger(__name__)
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
    logger.info(
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
    logger = logging.getLogger(__name__)
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
    logger.info(
        'Data in dataset {} de-identified.'
        'De-identified data written to {}'.format(
            dataset_id,
            destination_dataset_id))
    return response

def get_dataset_iam_policy(project_id, cloud_region, dataset_id):
    """Gets the IAM policy for the specified dataset."""
    logger = logging.getLogger(__name__)
    client = get_client()
    dataset_name = 'projects/{}/locations/{}/datasets/{}'.format(
        project_id, cloud_region, dataset_id)
    request = client.projects().locations().datasets().getIamPolicy(
        resource=dataset_name)
    response = request.execute()
    logger.info('etag: {}'.format(response.get('name')))
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
    logger = logging.getLogger(__name__)
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
    logger.info('etag: {}'.format(response.get('name')))
    logger.info('bindings: {}'.format(response.get('bindings')))
    return response
# [END healthcare_dataset_set_iam_policy]