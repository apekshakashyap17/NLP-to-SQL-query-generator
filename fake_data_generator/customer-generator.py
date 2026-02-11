import pandas as pd
from faker import Faker
import random

fake = Faker()
random.seed(42)
Faker.seed(42)

NUM_CUSTOMERS = 50000

customer_segments = ["Individual", "Startup", "SMB", "Mid-Market", "Enterprise"]

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": customer_id,                     
        "name": fake.name(),
        "email": f"user{customer_id}@example.com",      
        "country": fake.country(),
        "customer_segment": random.choice(customer_segments),
        "signup_date": fake.date_between(start_date="-10y", end_date="today")
    })

df = pd.DataFrame(customers)
df.to_csv("customers.csv", index=False)

print("customers.csv generated successfully")
