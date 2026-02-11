import pandas as pd
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta


random.seed(42)


plans = pd.read_csv("plans.csv")
subscriptions = pd.read_csv("subscriptions.csv")

plans_dict = plans.set_index("plan_id")["monthly_price"].to_dict()

today = datetime.today().date()

payments = []
payment_id = 1

# -------------------------
# Helper function
# -------------------------
def generate_payment_status():
    return random.choices(
        ["success", "failed", "refunded"],
        weights=[90, 7, 3],
        k=1
    )[0]

# -------------------------
# Generate payments
# -------------------------
for _, sub in subscriptions.iterrows():
    subscription_id = sub["subscription_id"]
    plan_id = sub["plan_id"]
    start_date = pd.to_datetime(sub["start_date"]).date()

    if pd.isna(sub["end_date"]):
        end_date = today
    else:
        end_date = pd.to_datetime(sub["end_date"]).date()

    amount = plans_dict[plan_id]

    payment_date = start_date

    while payment_date <= end_date:
        status = generate_payment_status()

        payments.append({
            "payment_id": payment_id,
            "subscription_id": subscription_id,
            "payment_date": payment_date,
            "amount": amount,
            "payment_status": status
        })

        payment_id += 1
        payment_date += relativedelta(months=1)

# -------------------------
# Create payments.csv
# -------------------------
payments_df = pd.DataFrame(payments)
payments_df.to_csv("payments.csv", index=False)

print(f"Generated {len(payments_df)} payment records")
