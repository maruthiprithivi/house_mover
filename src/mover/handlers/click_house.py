from datetime import datetime
import clickhouse_connect as cc
from mover.handlers.config import source, destination

def get_client(creds:dict):
    client = cc.get_client(
        host=creds.get("host"),
        user=creds.get("user"),
        password=creds.get("password"),
        secure=True,
    )
    # print("Result:", client.query("SELECT 1").result_set[0][0])
    return client


def get_database_list(creds:dict):
    database_info = {}
    client = get_client(creds)
    res = client.query("SHOW DATABASES").result_set
    database_list = [db[0] for db in res]
    database_info["total_databases_count"] = len(database_list)
    database_info["total_user_databases_count"] = database_info["total_databases_count"] - 3
    database_info["system_databases"] = ['INFORMATION_SCHEMA', 'information_schema', 'system']
    database_info["user_databases"] = [db for db in database_list if db not in database_info["system_databases"]]
    database_info["last_updated_at"] = datetime.now().isoformat() # To store the last updated time in the local system timezone
    return database_info


def get_table_list(creds:dict, request_type:str ="user", database:str | list = None):
    client = get_client(creds)
    if database is None:
        database_info = get_database_list(creds)
    if request_type:
        if request_type == "user":
            databases = database_info["user_databases"]
        elif request_type == "system":
            databases = database_info["system_databases"]
        else:
            databases = database_info["user_databases"] + database_info["system_databases"]
    else:
        databases = [database]
    table_info = {}
    table_list = []
    for database in databases:
        res = client.query(f"SHOW TABLES FROM {database}").result_set
        tables = [f"{database}.{table[0]}" for table in res]
        table_list.extend(tables)
    table_info["total_tables_count"] = len(table_list)
    table_info["tables"] = table_list
    table_info["last_updated_at"] = datetime.now().isoformat() # To store the last updated time in the local system timezone
    return table_info

def get_table_info(creds:dict, table: str | list = None):
    client = get_client(creds)
    if table is None:
        table_list = get_table_list(creds)
    elif isinstance(table, str):
        table_list = [table]
    else:
        table_list = table
    table_info = {}
    for table in table_list.get("tables"):
        res = client.query(f"DESCRIBE TABLE {table}").result_set
        # print("Result => /n", res, "\n")
        table_info[table] = res
    table_info["last_updated_at"] = datetime.now().isoformat() # To store the last updated time in the local system timezone
    return table_info


def get_create_table_query(creds:dict, table:str | list= None):
    client = get_client(creds)
    if table is None:
        table_list = get_table_list(creds)
    elif isinstance(table, str):
        table_list = [table]
    else:
        table_list = table
    create_table_query = {}    
    for table in table_list.get("tables"):
        res = client.query(f"SHOW CREATE TABLE {table}").result_set
        create_table_query[table] = res
    create_table_query["last_updated_at"] = datetime.now().isoformat() # To store the last updated time in the local system timezone
    return create_table_query

def get_materialized_view_list(creds:dict, database:str | list = None):
    client = get_client(creds)
    if database is None:
        database_info = get_database_list(creds)
        databases = database_info["user_databases"]
    elif isinstance(database, str):
        databases = [database]
    else:
        databases = database
    materialized_view_list = []
    for database in databases:
        res = client.query(f"SHOW MATERIALIZED VIEWS FROM {database}").result_set
        print("Result => /n", res, "\n")
        materialized_view_list.extend(res)
    return materialized_view_list

def get_materialized_view_info(creds:dict, materialized_view:str | list = None):
    client = get_client(creds)
    if materialized_view is None:
        materialized_view_list = get_materialized_view_list(creds)
    elif isinstance(materialized_view, str):
        materialized_view_list = [materialized_view]
    else:
        materialized_view_list = materialized_view
    materialized_view_info = {}

def get_materialized_view_create_query(creds:dict, materialized_view:str | list = None):
    client = get_client(creds)
    if materialized_view is None:
        materialized_view_list = get_materialized_view_list(creds)
    elif isinstance(materialized_view, str):
        materialized_view_list = [materialized_view]
    else:
        materialized_view_list = materialized_view
    materialized_view_create_query = {}

if __name__ == "__main__":
    # print("\n ############### get_database_list(source) ############### \n", get_database_list(source))  # To test the database list
    # print("\n ############### get_table_list(source, 'user') ############### \n", get_table_list(source, 'user'))  # To test the table list
    # print("\n ############### get_table_info(source) ############### \n", get_table_info(source))  # To test the table info
    print("\n ############### get_create_table_query(source) ############### \n", get_create_table_query(source))  # To test the create table query
    print("\n ############### get_materialized_view_list(source) ############### \n", get_materialized_view_list(source))  # To test the materialized view list
    pass # Keep this line to prevent the script from running into error when not testing