from .sql_prompt import build_sql_prompt
from .schema_context import SCHEMA_CONTEXT

def clean_sql(sql: str) -> str:
    sql = sql.strip()
    idx = sql.lower().find("select")
    if idx == -1:
        raise ValueError("No SELECT statement found")
    return sql[idx:]

def generate_sql(llm, question: str) -> str:
    prompt = build_sql_prompt(question, SCHEMA_CONTEXT)
    raw_sql = llm(prompt)
    return clean_sql(raw_sql)
