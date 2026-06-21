import datetime
import random
import pandas as pd
from sqlalchemy import create_engine

# 1. Generujemy losowe dane, żeby było z 200 wierszy do wykresów
categories = ["books", "electronics", "clothing", "food", "games"]
statuses = ["paid", "shipped", "cancelled", "paid", "paid"]

data = []
start_date = datetime.datetime(2026, 5, 1)

for i in range(200):
    user_id = f"u{random.randint(100, 999)}"
    category = random.choice(categories)
    amount = round(random.uniform(10.0, 500.0), 2)
    status = random.choice(statuses)
    # Losowy dzień w maju/czerwcu 2026
    event_time = start_date + datetime.timedelta(
        days=random.randint(0, 45), hours=random.randint(0, 23)
    )

    data.append([event_time, user_id, category, amount, status])

df = pd.DataFrame(
    data, columns=["event_time", "user_id", "category", "amount", "status"]
)

# 2. Pakujemy to do Postgresa
engine = create_engine("postgresql+psycopg2://bi:bi@localhost:5432/ntpd")
df.to_sql("transactions", engine, if_exists="replace", index=False)
