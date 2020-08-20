from google.cloud import bigquery
from google.oauth2 import service_account


def delete_dataset(dataset_id):
    client = bigquery.Client()
    client.delete_dataset(
        dataset_id, delete_contents=True, not_found_ok=True
    )  
                    

def create_dataset(dataset_id):
    
    
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset)  # Make an API request.
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
    # [END bigquery_create_dataset]


def dataset_exists(dataset_id) -> bool:
    client = bigquery.Client()
    try:
        client.get_dataset(dataset_id)  # Make an API request.
        print("Dataset {} already exists".format(dataset_id))
        return True
    except BaseException:
        print("Dataset {} is not found".format(dataset_id))
        return False

def query_string (q: str):
    # print(q)
    job_config = bigquery.QueryJobConfig(priority=bigquery.QueryPriority.BATCH)
    
    client = bigquery.Client()
    try:
        query_job = client.query(q, job_config=job_config)
        # query_job.result()
    except BaseException as err:
        # print(err)
        print('sth went wrong')

def query_string_with_result(q: str):
     # print(q)    
    client = bigquery.Client()
    try:
        query_job = client.query(q)
        return query_job.result()
    except BaseException as err:
        print(err)
        # print('sth went wrong')  
        return None 

def create_all_tables(dataset_id: str, rmove_if_exists: bool=False):
    if not dataset_exists(dataset_id):
        create_dataset(dataset_id)
    schema_originated_from = [
        bigquery.SchemaField("PARENT_TABLE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("PARENT_SOP_INSATANCE_UID", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("CHILD_TABLE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("CHILD_SOP_INSATANCE_UID", "STRING", mode="REQUIRED"),

    ]
    schema_issue = [
        bigquery.SchemaField("DCM_TABLE_NAME", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("DCM_SOP_INSATANCE_UID", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("ISSUE_MSG", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("MESSAGE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("TYPE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("MODULE_MACRO", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("KEYWORD", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("TAG", "INT64", mode="NULLABLE"),
    ]

    schema_fix = [
        bigquery.SchemaField("DCM_SOP_INSATANCE_UID", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("SHORT_ISSUE", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("ISSUE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("FIX", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("TYPE", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("MODULE_MACRO", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("KEYWORD", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("TAG", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("FIX_FUNCTION1", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("FIX_FUNCTION2", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("MESSAGE", "STRING", mode="REQUIRED"),
    ]


    tables: dict = {'ORIGINATED_FROM': schema_originated_from,
        'FIX': schema_fix,
        'ISSUE': schema_issue,
    }
    client = bigquery.Client()
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
    q = ''
    for s in all_queies:
        q += s
    query_job = client.query(q.format(dataset_id))
    query_job.result()


