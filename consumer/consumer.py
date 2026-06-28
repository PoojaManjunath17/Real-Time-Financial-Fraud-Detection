from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transactions",
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

        print(
            f"[{count}] "
            f"Type: {transaction['type']} | "
            f"Amount: {transaction['amount']}"
        )

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")

finally:
    consumer.close()
    print("Kafka Consumer Closed.")