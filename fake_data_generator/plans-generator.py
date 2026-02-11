import pandas as pd

plans = [
    {"plan_id": 1, "plan_name": "Basic", "monthly_price": 20, "currency": "USD", "billing_cycle": "monthly"},
    {"plan_id": 2, "plan_name": "Pro", "monthly_price": 50, "currency": "USD", "billing_cycle": "monthly"},
    {"plan_id": 3, "plan_name": "Business", "monthly_price": 90, "currency": "USD", "billing_cycle": "monthly"},
    {"plan_id": 4, "plan_name": "Enterprise", "monthly_price": 200, "currency": "USD", "billing_cycle": "monthly"},
]

df = pd.DataFrame(plans)
df.to_csv("plans.csv", index=False)

print("plans.csv generated successfully")
