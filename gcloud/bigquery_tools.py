from google.cloud import bigquery
import logging
import common.common_tools as ctools
schema_originated_from = [
        bigquery.SchemaField("PARENT_TABLE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("PARENT_SOPInstanceUID", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("CHILD_TABLE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("CHILD_SOPInstanceUID", "STRING", mode="REQUIRED"),
    ]
schema_issue = [
    bigquery.SchemaField("DCM_TABLE_NAME", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("SOPInstanceUID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("ISSUE_MSG", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("MESSAGE", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("TYPE", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("MODULE_MACRO", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("KEYWORD", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("TAG", "INT64", mode="NULLABLE"),
]
schema_fix = [
    bigquery.SchemaField("SOPInstanceUID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("SHORT_ISSUE", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("ISSUE", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("FIX", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("TYPE", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("MODULE_MACRO", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("KEYWORD", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("TAG", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("FIX_FUNCTION1", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("FIX_FUNCTION1_LINK", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("FIX_FUNCTION2", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("FIX_FUNCTION2_LINK", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("MESSAGE", "STRING", mode="REQUIRED"),
]
schema_defective = [
    bigquery.SchemaField("GCS_Bucket", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("StudyInstanceUID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("SeriesInstanceUID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("SOPInstanceUID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("FLAW", "STRING", mode="REQUIRED"),
]
tables: dict = {
    'ORIGINATED_FROM': schema_originated_from,
    'FIX_REPORT': schema_fix,
    'ISSUE': schema_issue,
    'DEFECTIVE': schema_defective,
}


def create_table(table_id, schema, project_id: str = None):
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project=project_id)
    t = bigquery.Table(table_id, schema)
    try:
        client.get_table(t)
        logger.info(
            'Table {} alread exists. No table is created'.format(table_id))
    except BaseException:
        client.create_table(t)
        logger.info('Table {} is created'.format(table_id))


def delete_bq_dataset(dataset_id, project_id: str = None):
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project=project_id)
    client.delete_dataset(dataset_id, delete_contents=True)
    if bq_dataset_exists(dataset_id, project_id):
        logger.info(
            'Bigquery dataset {} was not deleted successfully'.format(
                dataset_id))
    else:
        logger.info(
            'Bigquery dataset {} was deleted successfully'.format(
                dataset_id))


def delete_table(proj_id: str, bq_dataset_id: str, table_name: str):
    table_id = '{}.{}.{}'.format(proj_id, bq_dataset_id, table_name)
    client = bigquery.Client(project=proj_id)
    client.delete_table(table_id, not_found_ok=True)


def list_bq_dataset_names(proj_id: str, ):
    client = bigquery.Client(project=proj_id)
    datasets = list(client.list_datasets())  # Make an API request.
    output = []
    for ds in datasets:
        output.append('{}.{}'.format(proj_id, ds.dataset_id))
    return output


def create_bq_dataset(dataset_id, region: str, project_id: str = None):
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project=project_id)
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = region
    dataset = client.create_dataset(dataset)  # Make an API request.
    logger.info("Created bigquery dataset {}.{}".format(
        client.project, dataset.dataset_id))


def bq_dataset_exists(dataset_id, project_id: str = None) -> bool:
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project=project_id)
    try:
        client.get_dataset(dataset_id)  # Make an API request.
        logger.debug("Bigquery dataset {} already exists".format(dataset_id))
        return True
    except BaseException:
        logger.debug("Bigquery dataset {} is not found".format(dataset_id))
        return False


def query_string(q: str, table_name: str = '',
                 silent: bool = True, project_id: str = None):
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project=project_id)
    job_config = bigquery.QueryJobConfig(priority=bigquery.QueryPriority.BATCH)
    try:
        # if table_name != '':
        if not silent:
            logger.info("running query for '{}".format(table_name))
        # logger.info(q[:1024])
        client.query(q, job_config=job_config)
        # query_job.result()
    except BaseException as err:
        logger.error('{:-^100}'.format('BIG QUERY POPULATING ERROR'))
        logger.error(err, exc_info=True)
        print('sth went wrong')


def stream_insert_with_ids(table_id: str, rows_to_insert: list, schema):
    logger = logging.getLogger(__name__)
    if len(rows_to_insert) == 0:
        return True
    job_config = bigquery.LoadJobConfig(priority=bigquery.QueryPriority.BATCH)
    client = bigquery.Client(default_query_job_config=job_config)
    rows = []
    for r in rows_to_insert:
        rows.append(r[1])
    try:
        mx_retries = 30
        retries = 0
        while retries < mx_retries:
            output = ctools.retry_if_failes(
                client.insert_rows,
                (table_id, rows, schema),
                50, 1, True, 5
            )
            if len(output) == 0:
                break
            else:
                retries += 1
        if len(output) != 0:
            success = False
            for elem in output:
                if isinstance(elem, dict):
                    msg = ctools.dict2str(elem)
                else:
                    msg = str(elem)
                logger.error(msg)
        else:
            success = True
    except BaseException as err:
        logger.error('{:-^100}'.format('BIG QUERY POPULATING ERROR'))
        logger.error(err, exc_info=True)
        success = False
    return success
    # try:
    #     client.insert_rows_json(
    #         table_id, rows_to_insert, row_ids=[None]*len(rows_to_insert))
    # except BaseException as err:
    #     logger.error('{:-^100}'.format('BIG QUERY POPULATING ERROR'))
    #     logger.error(err, exc_info=True)


def stream_insert(table_id: str, rows_to_insert: list, schema):
    logger = logging.getLogger(__name__)
    job_config = bigquery.QueryJobConfig(priority=bigquery.QueryPriority.BATCH)
    client = bigquery.Client(default_query_job_config=job_config)
    # ctools.retry_if_failes(
    #     client.insert_rows,
    #     (table_id, rows_to_insert, schema),
    #     30, 10, True, 5
    # )
    try:
        client.insert_rows_json(
            table_id, rows_to_insert, row_ids=[None]*len(rows_to_insert))
    except BaseException as err:
        logger.error('{:-^100}'.format('BIG QUERY POPULATING ERROR'))
        logger.error(err, exc_info=True)


def query_string_with_result(q: str, project_name: str = None):
     # print(q)
    logger = logging.getLogger(__name__)
    client = bigquery.Client(project_name)
    try:
        query_job = client.query(q)
        return query_job.result()
    except BaseException as err:
        logger.error('{:-^100}'.format('BIG QUERY POPULATING ERROR'))
        logger.error(err, exc_info=True)
        # print('sth went wrong')
        return None


def create_all_tables(dataset_id: str, dataset_region: str,
                      rmove_if_exists: bool = False, 
                      project_id: str = None):
    if bq_dataset_exists(dataset_id, project_id) and rmove_if_exists:
        delete_bq_dataset(dataset_id, project_id)
    create_bq_dataset(dataset_id, dataset_region, project_id=project_id)
    
    client = bigquery.Client(project=project_id)
    clear_tables = """
        IF EXISTS (SELECT  RT.ROUTINE_NAME
            FROM   `{0}`.INFORMATION_SCHEMA.ROUTINES  AS RT
            WHERE  ROUTINE_NAME = 'CLEAR_TABLES_ROUTINES') THEN
            CALL `{0}`.CLEAR_TABLES_ROUTINES();
        END IF;
    """
    query_job = client.query(clear_tables.format(dataset_id))
    query_job.result()
    for t_id, sch in tables.items():
        t_id = '{}.{}'.format(dataset_id, t_id)
        t = bigquery.Table(t_id, sch)
        try:
            client.get_table(t)
        except BaseException:
            client.create_table(t)
    all_queies = []
    clear_all =\
        """
        CREATE OR REPLACE PROCEDURE `{0}`.CLEAR_TABLES_ROUTINES ()
        BEGIN
            DECLARE SQL STRING DEFAULT '';
            DECLARE N, i INT64 DEFAULT 0;
            CREATE TEMP TABLE SQL_COMMANDS AS (SELECT CONCAT(' DROP TABLE `' ,TABLE_CATALOG, '`.', TABLE_SCHEMA , '.', TABLE_NAME , '; ') AS SQL_COMMAND
            FROM   `{0}`.INFORMATION_SCHEMA.TABLES
            WHERE  TABLE_TYPE = 'BASE TABLE'
            UNION ALL
            SELECT CONCAT(' DROP PROCEDURE `' ,ROUTINE_CATALOG, '`.', ROUTINE_SCHEMA , '.', ROUTINE_NAME , '; ') AS SQL_COMMAND
            FROM   `{0}`.INFORMATION_SCHEMA.ROUTINES
            WHERE  ROUTINE_TYPE = 'PROCEDURE' );
            SET N = (SELECT COUNT(*) FROM SQL_COMMANDS);
            WHILE i < N DO
            EXECUTE IMMEDIATE 'SELECT SQL_COMMAND FROM SQL_COMMANDS LIMIT 1 OFFSET ?;' INTO SQL USING I;
            SELECT FORMAT('%d : %s', i, SQL) AS RESULT;
            EXECUTE IMMEDIATE SQL;
            SET i = i + 1;
            END WHILE;
        END;
        """
    all_queies.append(clear_all)
    merge_tables = """
CREATE OR REPLACE PROCEDURE `{0}`.MERGE_TABLES(
    NAME STRING)
BEGIN
    DECLARE UNION_Q, DELETE_Q, DATA_SET, TARGET_TABLE,
        FINAL_COMMAND, COMMAND_PTRN STRING;
    DECLARE N, I INT64 DEFAULT 0;
    CREATE TEMP TABLE SQL_COMMANDS AS(
        SELECT 
            CONCAT(' SELECT * FROM `' ,TABLE_CATALOG, '`.', TABLE_SCHEMA , '.', TABLE_NAME , ' ') AS SQL_COMMAND, 
            CONCAT('`' ,TABLE_CATALOG, '`.', TABLE_SCHEMA) as DATASET_NAME,
            CONCAT(' DROP TABLE IF EXISTS`' ,TABLE_CATALOG, '`.', TABLE_SCHEMA , '.', TABLE_NAME , ';') AS DELETE_COMMAND, 
            
        FROM   `{0}`.INFORMATION_SCHEMA.TABLES where TABLE_NAME like CONCAT(NAME , "_%")
        );
    SET UNION_Q = (select string_agg(SQL_COMMAND, " UNION ALL ") from SQL_COMMANDS group by DATASET_NAME);
    SET DATA_SET = (SELECT DATASET_NAME FROM SQL_COMMANDS LIMIT 1 OFFSET 0);
    SET DELETE_Q = FORMAT("%s %s.%s","DROP TABLE IF EXISTS", DATA_SET, NAME);
    EXECUTE IMMEDIATE DELETE_Q;
    SET TARGET_TABLE = CONCAT(DATA_SET, ".", NAME);
    SET COMMAND_PTRN = "CREATE TABLE %s AS( %s )";
    SET FINAL_COMMAND = FORMAT(COMMAND_PTRN, TARGET_TABLE, UNION_Q);
    EXECUTE IMMEDIATE FINAL_COMMAND;
    SET N = (SELECT COUNT(*) FROM SQL_COMMANDS);
    WHILE I < N DO
        EXECUTE IMMEDIATE 'SELECT DELETE_COMMAND FROM SQL_COMMANDS LIMIT 1 OFFSET ?;' INTO DELETE_Q USING I;
        SELECT FORMAT('%d : %s', i, DELETE_Q) AS RESULT;
        EXECUTE IMMEDIATE DELETE_Q;
        SET I = I + 1;
    END WHILE;
END;
    """
    all_queies.append(merge_tables)
    q = ''
    for s in all_queies:
        q += s
    query_job = client.query(q.format(dataset_id))
    query_job.result()


def list_bq_datasets(project_id: str):
    client = bigquery.Client(project_id)
    datasets = list(client.list_datasets())  # Make an API request.
    return datasets
