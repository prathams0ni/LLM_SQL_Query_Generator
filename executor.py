from llm import generate_sql
from prompt_builder import build_prompt, build_error_correction_prompt
from db import execute_query

MAX_RETRIES = 5


def validate_sql(sql):
    sql = sql.strip().lower()
    return sql.startswith("select")


def clean_sql_output(sql):
    if "```" in sql:
        sql = sql.replace("```sql", "").replace("```", "").strip()

    if "select" in sql.lower():
        sql = sql[sql.lower().index("select"):]

    return sql.strip()


def execute_with_retry(selected_db, schema, user_question):

    attempt = 0

    # 🔹 First SQL generation
    prompt = build_prompt(schema, user_question, explain=False)
    sql_query = generate_sql(prompt)
    sql_query = clean_sql_output(sql_query)

    while attempt < MAX_RETRIES:

        if not validate_sql(sql_query):
            return None, sql_query, "Only SELECT queries are allowed."

        columns, result = execute_query(selected_db, sql_query)

        if columns is not None:
            return (columns, result), sql_query, None

        # 🔹 Error occurred → Retry
        attempt += 1

        correction_prompt = build_error_correction_prompt(
            schema,
            sql_query,
            result
        )

        sql_query = generate_sql(correction_prompt)
        sql_query = clean_sql_output(sql_query)

    return None, sql_query, f"Failed after {MAX_RETRIES} attempts."
