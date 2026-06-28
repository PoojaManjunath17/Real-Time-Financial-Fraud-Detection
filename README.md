# Real-Time Financial Fraud Detection Pipeline

## Project Overview
This project detects fraudulent financial transactions in real time using Apache Kafka, Apache Spark, and Machine Learning.

## Dataset
PaySim Synthetic Financial Transactions Dataset

## Tech Stack
- Python
- Apache Kafka
- Apache Spark
- MongoDB/Cassandra
- Grafana
- Docker
- ## Day 6 - Kafka Consumer

### Run Kafka Containers
```bash
docker compose up -d
```

### Start the Consumer
```bash
python consumer/consumer.py
```

### Start the Producer
```bash
python producer/producer.py
```

The consumer receives and displays transactions streamed from the Kafka topic in real time.

## Week 1 Goal
Setup project infrastructure and simulate transaction streaming.