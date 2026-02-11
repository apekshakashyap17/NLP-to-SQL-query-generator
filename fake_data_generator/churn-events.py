import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)
Faker.seed(42)

subscriptions = pd.read_csv("subscriptions.csv")

churn_reasons = [
    "price_too_high",
    "lack_of_features",
    "poor_support",
    "low_usage",
    "switched_competitor"
]

churn_rows = []
churn_id = 1

for _, row in subscriptions.iterrows():
    if row["status"] == "cancelled":
        churn_rows.append({
            "churn_id": churn_id,
            "subscription_id": row["subscription_id"],
            "churn_date": row["end_date"],
            "churn_reason": random.choice(churn_reasons)
        })
        churn_id += 1

churn_df = pd.DataFrame(churn_rows)
churn_df.to_csv("churn_events.csv", index=False)

print("churn_events.csv generated successfully")
