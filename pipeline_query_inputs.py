import logging
import logging.config
import os
import shutil
from gcloud.bigquery_tools import *
from query_reference import QueryReferencedStudySequence
import json


def query_all( 
        source_bq_tableview: str = 'ref',
        ref_json_file: str = 'ref',
        json_file: str = 'testfile', 
        json_var: str = 'data' ,
        mx_number_of_series_in_file: int = -1,
        mx_number_of_series: int = -1
    ) -> None:
    logger = logging.getLogger(__name__)
    parent = os.path.dirname(json_file)
    if parent and not os.path.exists(parent):
        os.makedirs(parent)
    parent = os.path.dirname(ref_json_file)
    if parent and not os.path.exists(parent):
        os.makedirs(parent)
    Limit = ''
    if mx_number_of_series > 0:
        Limit = 'LIMIT {}'.format(mx_number_of_series)
    query = r"""
    WITH 
        ARS AS (
            SELECT 
                StudyInstanceUID, 
                STRING_AGG(DISTINCT X.CODEVALUE, '\n') AS CodeValue,
                STRING_AGG(DISTINCT X.CodeMeaning, '\n') AS CodeMeaning,
                STRING_AGG(DISTINCT X.CodingSchemeDesignator, '\n') AS CodingSchemeDesignator,
                COUNT(DISTINCT X.CODEVALUE) AS CodeValue_COUNT,
                COUNT(DISTINCT X.CodeMeaning) AS CodeMeaning_COUNT,
                COUNT(DISTINCT X.CodingSchemeDesignator) AS CodingSchemeDesignator_COUNT
            FROM `{0}` 
                CROSS JOIN UNNEST(AnatomicRegionSequence) AS X 
                GROUP BY 
                StudyInstanceUID
        )
        ,BPE AS (
            SELECT StudyInstanceUID, 
            STRING_AGG(DISTINCT BODYPARTEXAMINED, '\n') AS BodyPartExamined, 
            COUNT(DISTINCT BodyPartExamined) AS BPE_COUNT
            FROM `{0}` 
            GROUP BY StudyInstanceUID
        )
        , ANATOMY AS (
            SELECT 
                IF(BPE.StudyInstanceUID IS NOT NULL, BPE.StudyInstanceUID, ARS.StudyInstanceUID) AS StudyInstanceUID,
                BodyPartExamined,
                BPE_COUNT,
                CodeValue,
                CodeMeaning,
                CodingSchemeDesignator,
                CodeValue_COUNT AS ARS_COUNT,
                FROM BPE FULL OUTER JOIN ARS ON BPE.StudyInstanceUID=ARS.StudyInstanceUID
                WHERE (BPE.StudyInstanceUID IS NOT NULL OR ARS.StudyInstanceUID IS NOT NULL) 
                    AND (BPE_COUNT  < 2 OR BPE_COUNT IS NULL)
                    AND (CodeValue_COUNT  < 2 OR CodeValue_COUNT IS NULL)
        )
        , DISTINGUISHED AS(
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
            FROM `{0}` AS ORG
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
            ARRAY_AGG(FORMAT('%s', LEFT(GCS_URL, INSTR(GCS_URL, '#', -1, 1) - 1))) AS SERIES_PATH,
            ANY_VALUE(BodyPartExamined) AS BodyPartExamined,
            ANY_VALUE(CodeValue) AS CodeValue,
            ANY_VALUE(CodeMeaning) AS CodeMeaning,
            ANY_VALUE(CodingSchemeDesignator) AS CodingSchemeDesignator,
            ANY_VALUE(BPE_COUNT) AS BPE_COUNT,
            ANY_VALUE(ARS_COUNT) AS ARS_COUNT,
    FROM DISTINGUISHED INNER JOIN SINGLE_FRAMESETS 
    ON DISTINGUISHED.SeriesInstanceUID = SINGLE_FRAMESETS.SeriesInstanceUID
    LEFT OUTER JOIN ANATOMY ON ANATOMY.StudyInstanceUID = DISTINGUISHED.StudyInstanceUID
    GROUP BY 
            GCS_BUCKET,
            COLLECTION_ID,
            DISTINGUISHED.StudyInstanceUID, 
            DISTINGUISHED.SeriesInstanceUID
    ORDER BY StudyInstanceUID, SeriesInstanceUID
    {1}
    """.format(source_bq_tableview, Limit)
    logger.info(query)
    client = bigquery.Client()
    query_job = client.query(query)
    q_results = query_job.result()
    content = ''
    size_limit = 10000000
    if q_results is not None:
        file_counter = 0
        vec_data = []
        sz_factor: float = 1
        for i, row in enumerate(q_results):
            data1 = {}
            data1['GCS_BUCKET'] = row.GCS_BUCKET
            data1['COLLECTION_ID'] = row.COLLECTION_ID
            data1['StudyInstanceUID'] = row.StudyInstanceUID
            data1['SeriesInstanceUID'] = row.SeriesInstanceUID
            data1['INSTANCES'] = row.INSTANCES
            data1['SERIES_PATH'] = row.SERIES_PATH
            data1['BodyPartExamined'] = row.BodyPartExamined
            data1['CodeValue'] = row.CodeValue
            data1['CodeMeaning'] = row.CodeMeaning
            data1['CodingSchemeDesignator'] = row.CodingSchemeDesignator
            data1['BPE_COUNT'] = row.BPE_COUNT
            data1['ARS_COUNT'] = row.ARS_COUNT
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
                # print('number of series: {}'.format(len(vec_data)))
                vec_data = [vec_data[-1]]
        
        filename = '{}_{:08d}.json'.format(json_file, file_counter)
        with open(filename, 'w') as fp:
            json.dump(
                {json_var: vec_data}, fp, indent=4)
    ref_info = QueryReferencedStudySequence(source_bq_tableview)
    with open('{}.json'.format(ref_json_file), 'w') as ref_p:
        json.dump(ref_info, ref_p, indent=4)
    
    

# query_all('gitexcluded_queries/refs', 'gitexcluded_jsons/series', 'data', 10, 100)