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


def get_anatomy_info(anatomy_info, by_statistics: bool = True):
    if anatomy_info is not None:
        bpe = anatomy_info[0]
        if len(bpe) == 1:
            bpe = list(anatomy_info[0])[0]
        else:
            if by_statistics and len(bpe) > 1:
                bpe, vals = max(
                    bpe.items(), key=lambda x: (x[1][0], x[1][1]))
            else:
                bpe = None
        ars = anatomy_info[1]
        if str(code_item()) in ars:
            del ars[str(code_item())]
        if len(ars) == 1:
            ars = list(ars.values())[0][0]
            ars = (ars.value, ars.meaning, ars.scheme_designator)
        else:
            if by_statistics and len(ars) > 1:
                ars_str, ars_val = max(
                    ars.items(), key=lambda x: (x[1][1], x[1][2]))
                ars = ars_val[0]
            else:
                ars = (None, None, None)
    return (bpe, ars)


def quey_anatomy_from_tables(dcm_meta_table_name: str, dcm_auxiliary_table: str) -> dict:
    anatomy_query = """
WITH 
    T1 AS (
        SELECT 
            StudyInstanceUID, COUNT(DISTINCT SeriesInstanceUID) AS SERIESCOUNT,
            COUNT(DISTINCT SOPINSTANCEUID) AS INSTANCECOUNT,
            X.CODEVALUE AS CodeValue,
            X.CodeMeaning AS CodeMeaning,
            X.CodingSchemeDesignator AS CodingSchemeDesignator
        FROM {0} 
            CROSS JOIN UNNEST(AnatomicRegionSequence) AS X 
            GROUP BY 
            StudyInstanceUID,
            CodeValue, CodeMeaning, CodingSchemeDesignator
    ), 
    T2 AS (
        SELECT 
            SRC.StudyInstanceUID, 
            count(DISTINCT SRC.SeriesInstanceUID) as SERIESCOUNT,
            COUNT(DISTINCT SRC.SOPINSTANCEUID) AS INSTANCECOUNT,
            SRC.BodyPartExamined 
        FROM {0} AS SRC 
        GROUP BY StudyInstanceUID, BodyPartExamined
        ),
    ST AS (
        SELECT  AUX.GCS_BUCKET AS COLLECTIONNAME, DCM.STUDYINSTANCEUID 
        FROM {0} AS DCM 
            INNER JOIN {1} AS AUX 
            ON AUX.SOPINSTANCEUID=DCM.SOPINSTANCEUID 
        GROUP BY AUX.GCS_BUCKET, DCM.STUDYINSTANCEUID ),
    ANATOMY AS (
        SELECT 
            T2.StudyInstanceUID as BodyPartExamined_STUDYUID,
            T2.SERIESCOUNT as BPE_SERIESCOUNT,
            T2.INSTANCECOUNT AS BPE_INSTANCECOUNT,
            T1.StudyInstanceUID as AnatomicRegionSequence_STUDYUID,
            T1.SERIESCOUNT AS ARS_SERIESCOUNT,
            T1.INSTANCECOUNT AS ARS_INSTANCECOUNT,
            BodyPartExamined ,
            CodeValue, 
            CodeMeaning,
            CodingSchemeDesignator 
        FROM T1 FULL OUTER JOIN T2 ON T1.StudyInstanceUID=T2.StudyInstanceUID 
        GROUP BY  
            T2.StudyInstanceUID ,
            T2.SERIESCOUNT ,
            T2.INSTANCECOUNT ,
            T1.StudyInstanceUID ,
            T1.SERIESCOUNT ,
            T1.INSTANCECOUNT ,
            BodyPartExamined , 
            CodeValue, 
            CodeMeaning, 
            CodingSchemeDesignator 
        ORDER BY T2.StudyInstanceUID)
SELECT 
    COLLECTIONNAME,
    STUDYINSTANCEUID,
    BPE_SERIESCOUNT,
    BPE_INSTANCECOUNT,
    ARS_SERIESCOUNT,
    ARS_INSTANCECOUNT,
    BodyPartExamined ,
    CodeValue, 
    CodeMeaning,
    CodingSchemeDesignator,
    
FROM ANATOMY FULL OUTER JOIN ST ON (ST.STUDYINSTANCEUID = ANATOMY.BodyPartExamined_STUDYUID)
GROUP BY 
    COLLECTIONNAME,
    STUDYINSTANCEUID,
    BPE_SERIESCOUNT,
    BPE_INSTANCECOUNT,
    ARS_SERIESCOUNT,
    ARS_INSTANCECOUNT,
    BodyPartExamined ,
    CodeValue, 
    CodeMeaning,
    CodingSchemeDesignator
ORDER BY 
    COLLECTIONNAME,
    STUDYINSTANCEUID,
    BodyPartExamined ,
    CodeValue, 
    CodeMeaning,
    CodingSchemeDesignator
    """.format(dcm_meta_table_name, dcm_auxiliary_table)
    anatomies = query_string_with_result(anatomy_query)
    anatomy_info = {}
    for row in anatomies:
        st_uid = row.STUDYINSTANCEUID
        cln_name = row.COLLECTIONNAME
        bpe = row.BodyPartExamined
        bpe_se_count = row.BPE_SERIESCOUNT
        bpe_in_count = row.BPE_INSTANCECOUNT
        if bpe is not None:
            bpe = bpe.upper()
            bpe = re.sub(r'[^3-4A-Z]','', bpe)
            bpe = bpe[0] + re.sub(r'[^A-Z]', '', bpe[1:])
            if bpe not in BodyPartExamined2SCT:
                bpe = None# get_closest_body_part_examined(bpe)
        ars_se_count = row.ARS_SERIESCOUNT
        ars_in_count = row.ARS_INSTANCECOUNT       
        coding = code_item(
            row.CodeValue,
            row.CodeMeaning,
            row.CodingSchemeDesignator)
        if cln_name in anatomy_info:
            cln_stuff = anatomy_info[cln_name][0]
            study_anatomy_dict = anatomy_info[cln_name][1]
            if bpe is not None:
                if bpe in cln_stuff[0]:
                    cln_stuff[0][bpe][0] += bpe_se_count 
                    cln_stuff[0][bpe][1] += bpe_in_count 
                else:
                    cln_stuff[0][bpe] = [bpe_se_count, bpe_in_count]
            if not coding.is_empty():
                curr_code = str(coding)
                if curr_code in cln_stuff[1]:
                    cln_stuff[1][curr_code][1] += bpe_se_count 
                    cln_stuff[1][curr_code][2] += bpe_in_count 
                else:
                    cln_stuff[1][curr_code] = [
                        coding, bpe_se_count, bpe_in_count]
            # ==============================================================
            if st_uid in study_anatomy_dict:
                st_stuff = study_anatomy_dict[st_uid]
                if bpe is not None:
                    if bpe in st_stuff[0]:
                        st_stuff[0][bpe][0] += bpe_se_count 
                        st_stuff[0][bpe][1] += bpe_in_count 
                    else:
                        st_stuff[0][bpe] = [bpe_se_count, bpe_in_count]
                if not coding.is_empty():
                    curr_code = str(coding)
                    if curr_code in st_stuff[1]:
                        st_stuff[1][curr_code][1] += bpe_se_count 
                        st_stuff[1][curr_code][2] += bpe_in_count 
                    else:
                        st_stuff[1][curr_code] = [
                            coding, bpe_se_count, bpe_in_count]
            else:
                study_anatomy_dict[st_uid] = \
                    (
                        {bpe: [bpe_se_count, bpe_in_count]} if bpe is not None else {},
                        {str(coding): [coding, ars_se_count, ars_in_count]} if \
                            not coding.is_empty() else {}
                    )
        else:
            anatomy_info[cln_name] = (
                (
                    {bpe: [bpe_se_count, bpe_in_count]} if bpe is not None else {},
                    {str(coding): [coding, ars_se_count, ars_in_count]} if \
                        not coding.is_empty() else {}
                ),
                {
                    st_uid: (
                        {bpe: [bpe_se_count, bpe_in_count]} if bpe is not None else {},
                        {str(coding): [coding, ars_se_count, ars_in_count]} if \
                            not coding.is_empty() else {})
                }  
            ) 
    return anatomy_info