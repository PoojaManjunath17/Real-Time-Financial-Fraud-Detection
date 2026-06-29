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
fraud_count = 0

try:
    for message in consumer:
        transaction = message.value

        count += 1

        if int(transaction.get("isFraud", 0)) == 1:
            fraud_count += 1

        print("=" * 50)
        print(f"Transaction #{count}")
        print(f"Type        : {transaction.get('type', 'N/A')}")
        print(f"Amount      : {transaction.get('amount', 'N/A')}")
        print(f"Origin      : {transaction.get('nameOrig', 'N/A')}")
        print(f"Destination : {transaction.get('nameDest', 'N/A')}")
        print(f"Fraud       : {transaction.get('isFraud', 'N/A')}")

        if int(transaction.get("isFraud", 0)) == 1:
            print("🚨 FRAUD TRANSACTION DETECTED!")
        else:
            print("✅ Normal Transaction")

        print(f"Total Transactions Processed : {count}")
        print(f"Fraud Transactions           : {fraud_count}")
        print("=" * 50)

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")

finally:
    consumer.close()
    print("Kafka Consumer Closed.")