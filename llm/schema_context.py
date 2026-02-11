SCHEMA_CONTEXT = """
You are querying a MySQL database.

Tables:

customers (
  customer_id INT PRIMARY KEY 
  name VARCHAR(255) 
  email VARCHAR(255) 
  country VARCHAR(100) 
  customer_segment VARCHAR(50) 
  signup_date DATE
)

plans (
  plan_id INT PRIMARY KEY,
  plan_name VARCHAR(100),
  monthly_price DECIMAL,
  currency VARCHAR(10),
  billing_cycle VARCHAR(50)
)

subscriptions (
  subscription_id INT PRIMARY KEY,
  customer_id INT,
  plan_id INT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(20)
)

payments (
  payment_id INT PRIMARY KEY,
  subscription_id INT,
  payment_date DATE,
  amount DECIMAL(10, 2),
  payment_status VARCHAR(20)
)

churn_events (
  churn_id INT PRIMARY KEY,
  subscription_id INT,
  churn_date DATE,
  churn_reason VARCHAR,
)

Relationships:
- subscriptions.customer_id → customers.customer_id
- subscriptions.plan_id → plans.plan_id
- payments.subscription_id → subscriptions.subscription_id
- churn_events.subscription_id → subscriptions.subscription_i

Business logic:
- Active subscriptions have status = 'active' or end_date IS NULL [cite: 61325]
- Revenue is derived from payments.amount where payment_status = 'success' [cite: 55767]
- A subscription can have multiple payments
"""
