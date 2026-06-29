from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Read the dataset
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "PS_20174392719_1491204439457_log.csv")

df = pd.read_csv(csv_path)
print("Sending transactions to Kafka...")

# Send first 100 transactions
for _, row in df.head(100).iterrows():
    transaction = row.to_dict()
    producer.send("transactions_v2", transaction)

    print(f"Sent: {transaction['type']} | Amount: {transaction['amount']}")

    time.sleep(1)

producer.flush()

print("All transactions sent successfully!")