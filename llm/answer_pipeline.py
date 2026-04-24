from .sql_generator import generate_sql
from .sql_executor import execute_sql

def build_answer_prompt(question, columns, rows):
  
    row_count = len(rows)
    data_sample = rows[:20] 
    
    return f"""
User Question: {question}
Total rows returned: {row_count}
Top Data Samples (Column names: {list(columns)}):
{data_sample}

Instructions:
1. Based on the data, provide a clear and concise answer.
2. If there are many rows (like {row_count} countries), summarize the top 3-5 results and mention the total count.
3. Do not say "it's difficult to provide an exact count" — the data is right there. Give the numbers!
"""
def answer_question(llm, engine, question):
    sql = generate_sql(llm, question)
    columns, rows = execute_sql(engine, sql)
    
    
    clean_rows = [tuple(row) for row in rows]
    
   
    answer_prompt = build_answer_prompt(question, columns, clean_rows)
    return llm(answer_prompt)
