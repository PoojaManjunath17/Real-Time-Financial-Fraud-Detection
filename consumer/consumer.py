from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Waiting for transactions...\n")

for message in consumer:
    transaction = message.value

    print(
        f"Received: {transaction['type']} | "
        f"Amount: {transaction['amount']}"
    )