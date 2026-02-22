import mysql.connector
from config import DB_CONFIG

def get_connection(database=None):
    config = DB_CONFIG.copy()
    if database:
        config["database"] = database
    return mysql.connector.connect(**config)

def get_databases():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        conn.close()
        return [db[0] for db in databases]
    except Exception as e:
        return str(e)

def get_tables(database):
    try:
        conn = get_connection(database)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        conn.close()
        return [table[0] for table in tables]
    except Exception as e:
        return str(e)

def get_schema(database):
    try:
        conn = get_connection(database)
        cursor = conn.cursor()

        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        schema = ""

        for table in tables:
            table_name = table[0]
            schema += f"\nTable: {table_name}\n"

            cursor.execute(f"DESCRIBE {table_name};")
            columns = cursor.fetchall()

            for column in columns:
                column_name = column[0]
                column_type = column[1]
                schema += f"  - {column_name} ({column_type})\n"

        conn.close()
        return schema

    except Exception as e:
        return str(e)

def execute_query(database, query):
    try:
        # 🚨 Allow only SELECT queries
        if not query.strip().lower().startswith("select"):
            return None, "Only SELECT queries are allowed."

        conn = get_connection(database)
        cursor = conn.cursor()

        cursor.execute(query)

        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        conn.close()

        return columns, rows

    except Exception as e:
        return None, str(e)
