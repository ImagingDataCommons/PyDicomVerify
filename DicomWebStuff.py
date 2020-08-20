from google.auth.transport import requests
from google.oauth2 import service_account
_BASE_URL = "https://healthcare.googleapis.com/v1"
import os

def get_session():
    """Creates an authorized Requests Session."""
    credentials = service_account.Credentials.from_service_account_file(
        filename='/Users/afshin/.config/gcloud/idc-tcia-b9f07d34173d.json',
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    # Create a requests Session object with the credentials.
    session = requests.AuthorizedSession(credentials)
    return session

def dicomweb_store_instance(
    base_url, project_id, cloud_region, dataset_id, dicom_store_id, dcm_file
):
    """Handles the POST requests specified in the DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies".format(
        url, dataset_id, dicom_store_id
    )
    # Make an authenticated API request
    session = get_session()
    with open(dcm_file, "rb") as dcm:
        dcm_content = dcm.read()
    content_type = "application/dicom"
    headers = {"Content-Type": content_type}
    response = session.post(dicomweb_path, data=dcm_content, headers=headers)
    response.raise_for_status()
    print("Stored DICOM instance:")
    print(response.text)
    return response

def dicomweb_search_instance(
    base_url, project_id, cloud_region, dataset_id, dicom_store_id
):
    """Handles the GET requests specified in DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/instances".format(
        url, dataset_id, dicom_store_id
    )
    # Make an authenticated API request
    session = get_session()
    headers = {"Content-Type": "application/dicom+json; charset=utf-8"}
    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()
    instances = response.json()
    print("Instances:")
    print(json.dumps(instances, indent=2))
    return instances

def dicomweb_retrieve_study(
    base_url, project_id, cloud_region, dataset_id, dicom_store_id, study_uid
):
    """Handles the GET requests specified in the DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies/{}".format(
        url, dataset_id, dicom_store_id, study_uid
    )
    # When specifying the output file, use an extension like ".multipart."
    # Then, parse the downloaded multipart file to get each individual
    # DICOM file.
    file_name = "study.multipart"
    # Make an authenticated API request
    session = get_session()
    response = session.get(dicomweb_path)
    response.raise_for_status()
    with open(file_name, "wb") as f:
        f.write(response.content)
        print("Retrieved study and saved to {} in current directory".format(file_name))
    return response

def dicomweb_search_studies(
    base_url, project_id, cloud_region, dataset_id, dicom_store_id
):
    """Handles the GET requests specified in the DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies".format(
        url, dataset_id, dicom_store_id
    )
    # Refine your search by appending DICOM tags to the
    # request in the form of query parameters. This sample
    # searches for studies containing a patient's name.
    params = {"PatientName": "Sally Zhang"}
    session = get_session()
    response = session.get(dicomweb_path, params=params)
    response.raise_for_status()
    print("Studies found: response is {}".format(response))
    # Uncomment the following lines to process the response as JSON.
    # patients = response.json()
    # print('Patients found matching query:')
    # print(json.dumps(patients, indent=2))
    # return patients

def dicomweb_retrieve_instance(
    base_url,
    project_id,
    cloud_region,
    dataset_id,
    dicom_store_id,
    study_uid,
    series_uid,
    instance_uid,
    destination_file_name
):
    """Handles the GET requests specified in the DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicom_store_path = "{}/datasets/{}/dicomStores/{}".format(
        url, dataset_id, dicom_store_id
    )
    dicomweb_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}".format(
        dicom_store_path, study_uid, series_uid, instance_uid
    )
    directory = os.path.dirname(destination_file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # file_name = "instance.dcm"
    # Make an authenticated API request
    session = get_session()
    headers = {"Accept": "application/dicom; transfer-syntax=*"}
    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()
    with open(destination_file_name, "wb") as f:
        f.write(response.content)
        print(
            "Retrieved DICOM instance and saved to {} in current directory".format(
                destination_file_name
            )
        )
    return response

def dicomweb_retrieve_rendered(
    base_url,
    project_id,
    cloud_region,
    dataset_id,
    dicom_store_id,
    study_uid,
    series_uid,
    instance_uid,
):
    """Handles the GET requests specified in the DICOMweb standard."""
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicom_store_path = "{}/datasets/{}/dicomStores/{}".format(
        url, dataset_id, dicom_store_id
    )
    instance_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}".format(
        dicom_store_path, study_uid, series_uid, instance_uid
    )
    dicomweb_path = "{}/rendered".format(instance_path)
    file_name = "rendered_image.png"
    # Make an authenticated API request
    session = get_session()
    headers = {"Accept": "image/png"}
    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()
    with open(file_name, "wb") as f:
        f.write(response.content)
        print(
            "Retrieved rendered image and saved to {} in current directory".format(
                file_name
            )
        )
    return response

def dicomweb_delete_study(
    base_url, project_id, cloud_region, dataset_id, dicom_store_id, study_uid
):
    """Handles DELETE requests equivalent to the GET requests specified in
    the WADO-RS standard.
    """
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, cloud_region)
    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies/{}".format(
        url, dataset_id, dicom_store_id, study_uid
    )
    # Make an authenticated API request
    session = get_session()
    headers = {"Content-Type": "application/dicom+json; charset=utf-8"}
    response = session.delete(dicomweb_path, headers=headers)
    response.raise_for_status()
    print("Deleted study.")
    return response