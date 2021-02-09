import logging
import logging.config
import os
import shutil
from rightdicom.dcmfix.study_dependent_patches import *
from gcloud.BigQueryStuff import *
def QueryReferencedStudySequence(source_table: str):
    q = """
    WITH UIDTABLE AS (
    SELECT  SOPINSTANCEUID, SOPCLASSUID FROM `{0}`),
    REFTABLE AS(
        SELECT SOPINSTANCEUID,
                X.REFERENCEDSOPCLASSUID AS REFERENCEDSOPCLASSUID,
                X.REFERENCEDSOPINSTANCEUID AS REFERENCEDSOPINSTANCEUID,
            FROM  `{0}` AS T CROSS JOIN UNNEST(T.REFERENCEDSTUDYSEQUENCE) AS X ),
    REFUIDTABLE AS( SELECT 
                UIDTABLE.SOPINSTANCEUID,
                REFERENCEDSOPCLASSUID,
                REFERENCEDSOPINSTANCEUID,
            FROM UIDTABLE FULL OUTER JOIN REFTABLE ON UIDTABLE.SOPINSTANCEUID = REFTABLE.SOPINSTANCEUID
            WHERE REFERENCEDSOPCLASSUID IS NULL AND REFERENCEDSOPINSTANCEUID IS NOT NULL
        )
    SELECT REFUIDTABLE.SOPINSTANCEUID,
            REFUIDTABLE.REFERENCEDSOPCLASSUID,
            REFUIDTABLE.REFERENCEDSOPINSTANCEUID, 
            UIDTABLE.SOPINSTANCEUID AS FOUND_SOPINSTANCEUID,
            UIDTABLE.SOPCLASSUID AS FOUND_SOPCLASSUID,
            FROM REFUIDTABLE FULL OUTER JOIN UIDTABLE ON UIDTABLE.SOPINSTANCEUID = REFUIDTABLE.REFERENCEDSOPINSTANCEUID 
            WHERE REFUIDTABLE.SOPINSTANCEUID IS NOT NULL AND UIDTABLE.SOPCLASSUID IS NOT NULL
            ORDER BY UIDTABLE.SOPINSTANCEUID DESC
    """.format(source_table)
    # print(q)
    res = query_string_with_result(q)
    ref_sop_class_uids = {}
    if res is not None:
        for row in res:
            # print(row.SOPINSTANCEUID)
            cur_inst_uid = row.SOPINSTANCEUID
            ref_class_uid = row.REFERENCEDSOPCLASSUID
            ref_inst_uid = row.REFERENCEDSOPINSTANCEUID
            found_inst_uid = row.FOUND_SOPINSTANCEUID
            found_class_uid = row.FOUND_SOPCLASSUID
            # if found_class_uid is not None:
            ref_sop_class_uids[found_inst_uid] = found_class_uid
    return ref_sop_class_uids

