from sqlalchemy import text

def execute_sql(engine, sql: str):
    if not sql.strip().lower().startswith("select"):
        raise ValueError("Unsafe SQL detected")

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = list(result.keys())

    return columns, rows
