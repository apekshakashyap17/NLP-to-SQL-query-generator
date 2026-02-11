def build_sql_prompt(user_question: str, schema: str) -> str:
    return f"""
You are a senior MySQL expert. Based on the schema provided, write one high-quality SQL query.

{schema}

STRICT RULES FOR SUCCESS:
1. **GROUP BY & SELECT**: If you use GROUP BY, you MUST include both the grouping column and the COUNT/SUM in the SELECT clause.
2. **REVENUE**: Always use `SUM(p.amount)` and JOIN the `payments` table. Filter by `p.payment_status = 'success'`.
3. **DATES**: 
   - For "Monthly" questions, use: `DATE_FORMAT(date_column, '%Y-%m')`.
   - For "Yearly" questions, use: `YEAR(date_column)`.
4. **CHURN**: Join `churn_events` to `subscriptions`. Use `churn_reason` for categorical analysis.
5. **LIMITS**: If the user asks for "Top" or "Most", always use `ORDER BY ... DESC` and `LIMIT`.
6. **NO MARKDOWN**: Output only the raw SQL. No ```sql, no explanations.

User Question: {user_question}
SQL:"""