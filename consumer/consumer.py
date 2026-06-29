from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transactions_v2",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("=" * 50)
print("Kafka Consumer Started")
print("Waiting for transactions...")
print("=" * 50)

count = 0

try:
    for message in consumer:
        transaction = message.value
        count += 1
        print("=" * 50)
        print(f"Transaction #{count}")
        print(f"Type        : {transaction['type']}")
        print(f"Amount      : {transaction['amount']}")
        print(f"Origin      : {transaction['nameOrig']}")
        print(f"Destination : {transaction['nameDest']}")
        print(f"Fraud       : {transaction['isFraud']}")

        if int(transaction["isFraud"]) == 1:
            print("🚨 FRAUD TRANSACTION DETECTED!")
        else:
            print("✅ Normal Transaction")

        print("=" * 50)

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")

finally:
    consumer.close()
    print("Kafka Consumer Closed.")