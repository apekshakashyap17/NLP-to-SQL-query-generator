import streamlit as st
from llm.answer_pipeline import answer_question
from llm.llm_model import ollama_llm
from llm.sql_generator import generate_sql
from db_connection import engine


st.set_page_config(page_title="SQL Data Talk", page_icon="📊")

st.title("📊 Chat with Your MySQL Data")
st.markdown("Ask questions about subscriptions, plans, and payments in plain English.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sql" in message:
            with st.expander("View Generated SQL"):
                st.code(message["sql"], language="sql")


if prompt := st.chat_input("e.g., How many active subscriptions per plan?"):
  
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

   
    with st.chat_message("assistant"):
        with st.spinner("Analyzing data..."):
            try:
                generated_sql = generate_sql(ollama_llm, prompt)
                
                answer = answer_question(ollama_llm, engine, prompt)
                
                st.markdown(answer)
                with st.expander("View Generated SQL"):
                    st.code(generated_sql, language="sql")
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer, 
                    "sql": generated_sql
                })
            except Exception as e:
                st.error(f"Error: {str(e)}")
