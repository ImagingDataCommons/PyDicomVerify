import logging
import logging.config
import os
import shutil
from rightdicom.dcmfix.study_dependent_patches import *
from gcloud.BigQueryStuff import *

class code_item:
    def __init__(self, 
                 value=None, meaning: str = None,
                 scheme_designator:str = None):
        self.value = value
        self.meaning = meaning
        self.scheme_designator = scheme_designator


    def is_empty(self):
        return (self.value is None) and \
            (self.meaning is None) and (self.scheme_designator is None)

    def __str__(self):
        indent = '    '
        out = '{0}CodeValue = {1}\n{0}CodeMenaing = {2}\n{0}'\
            'CodingSchemeDesignator = {3}'.format(
                indent, self.value, self.meaning, self.scheme_designator
            )
        return out


def query_anatomy_from_tables(dicom_bq_tableview: str) -> dict:
    anatomy_query = r"""
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
        )SELECT * FROM ANATOMY
    """.format(dicom_bq_tableview)
    # print(anatomy_query)
    anatomies = query_string_with_result(anatomy_query, project_name='idc-tcia')
    anatomy_info = {}
    for row in anatomies:
        st_uid = row.StudyInstanceUID
        bpe = row.BodyPartExamined
        if bpe is not None:
            bpe = bpe.upper()
            bpe = re.sub(r'[^3-4A-Z]','', bpe)
            bpe = bpe[0] + re.sub(r'[^A-Z]', '', bpe[1:])
            if bpe not in BodyPartExamined2SCT:
                bpe = None# get_closest_body_part_examined(bpe)      
        coding = (
            row.CodeValue,
            row.CodeMeaning,
            row.CodingSchemeDesignator)
        anatomy_info[st_uid] = (bpe, coding)
    return anatomy_info