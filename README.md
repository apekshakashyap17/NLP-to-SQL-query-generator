# NLP to SQL Generator

A locally deployed LLM-powered system that translates plain English questions into executable SQL queries — no SQL knowledge required from the user.

## What it does

Ask a business question in plain language and the system generates the correct SQL query, runs it against a MySQL database, and returns a natural language answer via a Streamlit dashboard.

## How it works

1. User enters a plain English question in the Streamlit interface (`app.py`)
2. The question is passed to a locally deployed LLM via Ollama with schema context injected into the prompt
3. The LLM generates an executable SQL query
4. The query is run against a MySQL database using SQLAlchemy (`db_connection.py`)
5. The result is returned and displayed as a readable answer

## Tech Stack

- **LLM:** Ollama (locally deployed)
- **Database:** MySQL via SQLAlchemy
- **Frontend:** Streamlit
- **Language:** Python

## Performance

- 90%+ query accuracy on complex 5-table joins
- Tested on a 50,000-record SaaS schema (customers, subscriptions, payments, churn)

## Setup

```bash
pip install -r requirements.txt
```

Make sure Ollama is running locally, then:

```bash
streamlit run app.py
```

## Why local?

No API keys, no cost, full data privacy — everything runs on your machine.
