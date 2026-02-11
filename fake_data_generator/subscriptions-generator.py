import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()
random.seed(42)
Faker.seed(42)

customers_df = pd.read_csv("customers.csv")


plans_df = pd.read_csv("plans.csv")
plan_ids = plans_df["plan_id"].tolist()

subscriptions = []
subscription_id = 1

for _, customer in customers_df.iterrows():
    customer_id = customer["customer_id"]
    signup_date = pd.to_datetime(customer["signup_date"])
    customer_segment = customer["customer_segment"]

    # Plan selection logic (Enterprise customers more likely to be on higher plans)
    if customer_segment == "Enterprise":
        plan_id = random.choices(plan_ids, weights=[1, 2, 3, 6])[0]
        churn_probability = 0.15
    else:
        plan_id = random.choices(plan_ids, weights=[4, 4, 2, 1])[0]
        churn_probability = 0.30

    start_date = signup_date + timedelta(days=random.randint(0, 30))

    if random.random() < churn_probability:
        status = "cancelled"
        active_days = random.randint(30, 900)
        end_date = start_date + timedelta(days=active_days)
    else:
        status = "active"
        end_date = None

    subscriptions.append({
        "subscription_id": subscription_id,
        "customer_id": customer_id,
        "plan_id": plan_id,
        "start_date": start_date.date(),
        "end_date": end_date.date() if end_date else None,
        "status": status
    })

    subscription_id += 1

df = pd.DataFrame(subscriptions)
df.to_csv("subscriptions.csv", index=False)

print("subscriptions.csv generated successfully")