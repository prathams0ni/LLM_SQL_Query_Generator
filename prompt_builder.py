def build_prompt(schema, user_question, explain=False):

    if explain:
        instruction = """
Generate valid MySQL SQL query using given schema.
After SQL, provide short explanation of what the query does.
Return format:

SQL:
<query>

Explanation:
<short explanation>
"""
    else:
        instruction = """
Generate valid MySQL SQL query using given schema.
Use minimum required tables.
Do not use JOIN unless necessary.
Return ONLY raw SQL.
No explanation.
No markdown.
"""

    prompt = f"""
You are an expert MySQL query generator.

STRICT RULES:
1. Use only provided tables and columns.
2. Do not assume anything outside schema.

DATABASE SCHEMA:
{schema}

USER QUESTION:
{user_question}

{instruction}
"""
    return prompt

def build_error_correction_prompt(schema, failed_query, error_message):
    prompt = f"""
You are an expert MySQL query fixer.

The following SQL query failed.

DATABASE SCHEMA:
{schema}

FAILED QUERY:
{failed_query}

ERROR MESSAGE:
{error_message}

Fix the query using only the provided schema.
Return ONLY corrected SQL.
No explanation.
No markdown.
"""
    return prompt

