from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transaction = {
    "transaction_id": 1,
    "amount": 5000,
    "type": "TRANSFER"
}

producer.send("transactions", transaction)
producer.flush()

print("Transaction sent successfully!")