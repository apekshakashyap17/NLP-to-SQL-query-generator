import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()
random.seed(42)
Faker.seed(42)

# Load subscriptions
subscriptions = pd.read_csv("subscriptions.csv")

usage_rows = []
usage_id = 1

PLAN_USAGE_LIMITS = {
    1: {"api_calls": (100, 1000), "storage": (1, 5), "users": (1, 3)},      # Basic
    2: {"api_calls": (1000, 5000), "storage": (5, 20), "users": (3, 10)},   # Pro
    3: {"api_calls": (5000, 20000), "storage": (20, 100), "users": (10, 50)},# Business
    4: {"api_calls": (20000, 100000), "storage": (100, 500), "users": (50, 500)} # Enterprise
}

for _, row in subscriptions.iterrows():
    start = pd.to_datetime(row["start_date"])
    end = pd.to_datetime(row["end_date"]) if pd.notna(row["end_date"]) else pd.Timestamp.today()

    plan_limits = PLAN_USAGE_LIMITS[row["plan_id"]]

    current_date = start

    while current_date <= end:
        usage_rows.append({
            "usage_id": usage_id,
            "subscription_id": row["subscription_id"],
            "usage_date": current_date.date(),
            "api_calls": random.randint(*plan_limits["api_calls"]),
            "storage_gb": round(random.uniform(*plan_limits["storage"]), 2),
            "active_users": random.randint(*plan_limits["users"])
        })
        usage_id += 1
        current_date += timedelta(days=30)  # monthly snapshot

usage_df = pd.DataFrame(usage_rows)
usage_df.to_csv("usage_metrics.csv", index=False)

print("usage_metrics.csv generated successfully")
