from llm.answer_pipeline import answer_question
from llm.llm_model import ollama_llm
from db_connection import engine
from llm.sql_generator import generate_sql

if __name__ == "__main__": 
    question = "How many active subscriptions does each plan have?"
    
    # Debug: See the SQL first
    generated_sql = generate_sql(ollama_llm, question)
    print(f"--- DEBUG SQL ---\n{generated_sql}\n-----------------")
    
    answer = answer_question(ollama_llm, engine, question)
    print(f"Final Answer: {answer}")
