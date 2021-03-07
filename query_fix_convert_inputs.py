import logging
import logging.config
import os
import shutil
from gcloud.BigQueryStuff import *
import json

def query_all(json_file: str = 'testfile', 
                json_var: str = 'data' ,
                mx_number_of_series_in_file: int = -1,
                mx_number_of_series: int = -1) -> dict:
    logger = logging.getLogger(__name__)
    parent = os.path.dirname(json_file)
    if parent and not os.path.exists(parent):
        os.makedirs(parent)
    Limit = ''
    if mx_number_of_series > 0:
        Limit = 'LIMIT {}'.format(mx_number_of_series)
    query = """
WITH DISTINGUISHED AS(
        SELECT  SOPInstanceUID,
                SeriesInstanceUID,
                StudyInstanceUID, 
                COLLECTION_ID,
                GCS_URL,
                GCS_BUCKET,
                ARRAY_TO_STRING(SoftwareVersions, '/') AS SoftwareVersions,
                ARRAY_TO_STRING(ImageType, '/') AS ImageType,
                FORMAT('%10.5f, %10.5f, %10.5f, %10.5f, %10.5f, %10.5f',
                        CAST(ImageOrientationPatient [SAFE_OFFSET(0)] AS FLOAT64 ),
                        CAST(ImageOrientationPatient [SAFE_OFFSET(1)] AS FLOAT64 ),
                        CAST(ImageOrientationPatient [SAFE_OFFSET(2)] AS FLOAT64 ),
                        CAST(ImageOrientationPatient [SAFE_OFFSET(3)] AS FLOAT64 ),
                        CAST(ImageOrientationPatient [SAFE_OFFSET(4)] AS FLOAT64 ),
                        CAST(ImageOrientationPatient [SAFE_OFFSET(5)] AS FLOAT64 )
                        ) AS ImageOrientationPatient,
                FORMAT('%10.5f, %10.5f',
                        CAST(PixelSpacing [SAFE_OFFSET(0)] AS FLOAT64 ),
                        CAST(PixelSpacing [SAFE_OFFSET(1)] AS FLOAT64 )
                        ) AS PixelSpacing,
                SliceThickness,
                ORG.Rows,
                ORG.Columns,
                PatientID,
                CONCAT(
                    ORG.PATIENTNAME.Alphabetic.FamilyName, '^',
                    ORG.PATIENTNAME.Alphabetic.GivenName, '^',
                    ORG.PATIENTNAME.Alphabetic.MiddleName, '^',
                    ORG.PATIENTNAME.Alphabetic.NamePrefix, '^',
                    ORG.PATIENTNAME.Alphabetic.NameSuffix
                ) AS PATIENTNAME,
                Manufacturer,
                StationName,
                ManufacturerModelName,
                DeviceSerialNumber,
                PixelPaddingValue,
                Modality,
                BurnedInAnnotation,
                SOPClassUID,
                BitsStored,
                BitsAllocated,
                HighBit,
                PixelRepresentation,
                PhotometricInterpretation,
                PlanarConfiguration,
                SamplesPerPixel,
                ProtocolName,
                FORMAT('%2.8E/%2.8E/%2.8E',
                    CAST(ImagePositionPatient[SAFE_OFFSET(0)] AS FLOAT64 ),
                    CAST(ImagePositionPatient[SAFE_OFFSET(1)] AS FLOAT64 ),
                    CAST(ImagePositionPatient[SAFE_OFFSET(2)] AS FLOAT64 )
                    ) AS ImagePositionPatient,
        FROM `canceridc-data.idc_views.dicom_all` AS ORG
        WHERE
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.2" OR
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.4" OR
                SOPCLASSUID = "1.2.840.10008.5.1.4.1.1.128"
), COUNT_TABLE AS(
        SELECT  COUNT(DISTINCT SOPInstanceUID) AS SOPInstanceUID_COUNT,
                SeriesInstanceUID,
                StudyInstanceUID, 
                COUNT(DISTINCT COLLECTION_ID) AS COLLECTION_ID_COUNT,
                COUNT(DISTINCT GCS_URL) AS GCS_URL_COUNT,
                COUNT(DISTINCT GCS_BUCKET) AS GCS_BUCKET_COUNT,
                COUNT(DISTINCT SoftwareVersions) AS SoftwareVersions_COUNT,
                COUNT(DISTINCT ImageType) AS ImageType_COUNT,
                COUNT(DISTINCT ImageOrientationPatient) AS ImageOrientationPatient_COUNT,
                COUNT(DISTINCT PixelSpacing) AS PixelSpacing_COUNT,
                COUNT(DISTINCT SliceThickness) AS SliceThickness_COUNT,
                COUNT(DISTINCT DISTINGUISHED.Rows) AS Rows_COUNT,
                COUNT(DISTINCT DISTINGUISHED.Columns) AS Columns_COUNT,
                COUNT(DISTINCT PatientID) AS PatientID_COUNT,
                COUNT(DISTINCT PATIENTNAME) AS PATIENTNAME_COUNT,
                COUNT(DISTINCT Manufacturer) AS Manufacturer_COUNT,
                COUNT(DISTINCT StationName) AS StationName_COUNT,
                COUNT(DISTINCT ManufacturerModelName) AS ManufacturerModelName_COUNT,
                COUNT(DISTINCT DeviceSerialNumber) AS DeviceSerialNumber_COUNT,
                COUNT(DISTINCT PixelPaddingValue) AS PixelPaddingValue_COUNT,
                COUNT(DISTINCT Modality) AS Modality_COUNT,
                COUNT(DISTINCT BurnedInAnnotation) AS BurnedInAnnotation_COUNT,
                COUNT(DISTINCT SOPClassUID) AS SOPClassUID_COUNT,
                COUNT(DISTINCT BitsStored) AS BitsStored_COUNT,
                COUNT(DISTINCT BitsAllocated) AS BitsAllocated_COUNT,
                COUNT(DISTINCT HighBit) AS HighBit_COUNT,
                COUNT(DISTINCT PixelRepresentation) AS PixelRepresentation_COUNT,
                COUNT(DISTINCT PhotometricInterpretation) AS PhotometricInterpretation_COUNT,
                COUNT(DISTINCT PlanarConfiguration) AS PlanarConfiguration_COUNT,
                COUNT(DISTINCT SamplesPerPixel) AS SamplesPerPixel_COUNT,
                COUNT(DISTINCT ProtocolName) AS ProtocolName_COUNT,
                COUNT(DISTINCT ImagePositionPatient) AS ImagePositionPatient_COUNT
        FROM DISTINGUISHED  
        GROUP BY  StudyInstanceUID, SeriesInstanceUID),
SINGLE_FRAMESETS AS(
        SELECT SeriesInstanceUID FROM COUNT_TABLE 
        WHERE
                SoftwareVersions_COUNT < 2 AND
                ImageType_COUNT < 2 AND
                ImageOrientationPatient_COUNT < 2 AND
                PixelSpacing_COUNT < 2 AND
                SliceThickness_COUNT < 2 AND
                Rows_COUNT < 2 AND
                Columns_COUNT < 2 AND
                PatientID_COUNT < 2 AND
                PATIENTNAME_COUNT < 2 AND
                Manufacturer_COUNT < 2 AND
                StationName_COUNT < 2 AND
                ManufacturerModelName_COUNT < 2 AND
                DeviceSerialNumber_COUNT < 2 AND
                PixelPaddingValue_COUNT < 2 AND
                Modality_COUNT < 2 AND
                BurnedInAnnotation_COUNT < 2 AND
                SOPClassUID_COUNT < 2 AND
                BitsStored_COUNT < 2 AND
                BitsAllocated_COUNT < 2 AND
                HighBit_COUNT < 2 AND
                PixelRepresentation_COUNT < 2 AND
                PhotometricInterpretation_COUNT < 2 AND
                PlanarConfiguration_COUNT < 2 AND
                SamplesPerPixel_COUNT < 2 AND
                ProtocolName_COUNT < 2 AND 
                ImagePositionPatient_COUNT = SOPInstanceUID_COUNT)
SELECT  GCS_BUCKET,
        COLLECTION_ID,
        DISTINGUISHED.StudyInstanceUID, 
        DISTINGUISHED.SeriesInstanceUID,
        ARRAY_AGG(SOPInstanceUID) AS INSTANCES,
        ARRAY_AGG(FORMAT('%s', LEFT(GCS_URL, INSTR(GCS_URL, '#', -1, 1) - 1))) AS SERIES_PATH
FROM DISTINGUISHED INNER JOIN SINGLE_FRAMESETS 
ON DISTINGUISHED.SeriesInstanceUID = SINGLE_FRAMESETS.SeriesInstanceUID
GROUP BY 
        GCS_BUCKET,
        COLLECTION_ID,
        DISTINGUISHED.StudyInstanceUID, 
        DISTINGUISHED.SeriesInstanceUID
ORDER BY StudyInstanceUID, SeriesInstanceUID
{}
    """.format(Limit)
    logger.info(query)
    client = bigquery.Client()
    query_job = client.query(query)
    q_results = query_job.result()
    content = ''
    size_limit = 10000000
    if q_results is not None:
        file_counter = 0
        vec_data = []
        sz_factor = 1
        for i, row in enumerate(q_results):
            data1 = {}
            data1['GCS_BUCKET'] = row.GCS_BUCKET
            data1['COLLECTION_ID'] = row.COLLECTION_ID
            data1['StudyInstanceUID'] = row.StudyInstanceUID
            data1['SeriesInstanceUID'] = row.SeriesInstanceUID
            data1['INSTANCES'] = row.INSTANCES
            data1['SERIES_PATH'] = row.SERIES_PATH
            vec_data.append(data1)
            size = len(
                json.dumps({json_var: vec_data}, indent=4)) * sz_factor
            size_1 = len(
                json.dumps({json_var: vec_data[0:-1]}, indent=4)) * sz_factor            
            if size > 0.99 * size_limit or (mx_number_of_series_in_file > 0 and 
                len(vec_data) > mx_number_of_series_in_file):
                filename = '{}_{:08d}.json'.format(
                    json_file, file_counter)
                with open(filename, 'w') as fp:
                    json.dump(
                        {json_var: vec_data[0:-1]}, fp, indent=4)
                sz = os.path.getsize(filename)
                sz_factor = sz / size_1
                file_counter += 1
                print('number of series: {}'.format(len(vec_data)))
                vec_data = [vec_data[-1]]
        
        filename = '{}_{:08d}.json'.format(json_file, file_counter)
        with open(filename, 'w') as fp:
            json.dump(
                {json_var: vec_data}, fp, indent=4)

# query_all('gs_jsons/series', 'data', 20, 1000)