 # Real-Time Financial Fraud Detection Pipeline

## Project Overview

This project detects fraudulent financial transactions in real time using **Apache Kafka**, **Apache Spark**, and **Machine Learning**. The system streams financial transactions from the PaySim dataset, processes them through Kafka, and prepares the data for real-time fraud detection.

---

## Dataset

**PaySim Synthetic Financial Transactions Dataset**

---

## Tech Stack

* Python
* Apache Kafka
* Apache Spark
* MongoDB / Cassandra
* Docker
* Docker Compose
* Pandas
* JSON
* kafka-python

---

## Project Structure

```
Week2Project/
│── producer/
│   └── producer.py
│── consumer/
│   └── consumer.py
│── data/
│   └── PS_20174392719_1491204439457_log.csv
│── docker-compose.yml
│── requirements.txt
│── README.md
```

---

## Running the Project

### 1. Start Kafka and ZooKeeper

```bash
docker compose up -d
```

### 2. Start the Kafka Consumer

```bash
python consumer/consumer.py
```

### 3. Start the Kafka Producer

```bash
python producer/producer.py
```

The consumer receives and displays transactions streamed from the Kafka topic in real time.

---

# Week 1 Progress Report

## Week 1 Objective

Set up the project environment, configure Apache Kafka using Docker, and implement Kafka Producer and Consumer to simulate real-time financial transactions using the PaySim dataset.

---

## Day 1 – Infrastructure Setup

* Installed Python and required libraries.
* Installed Docker Desktop.
* Configured Docker Compose.
* Started Kafka and ZooKeeper containers.
* Verified Docker services.

---

## Day 2 – Kafka Configuration

* Created the Kafka topic (`transactions`).
* Verified Kafka connectivity.
* Tested Kafka using Docker commands.
* Fixed configuration issues.

---

## Day 3 – Dataset Preparation

* Downloaded the PaySim dataset.
* Loaded the dataset using Pandas.
* Prepared transaction data for streaming.

---

## Day 4 – Kafka Producer

* Developed a Kafka Producer in Python.
* Read transaction data from the PaySim dataset.
* Converted transactions into JSON format.
* Published transaction messages to the Kafka topic.

---

## Day 5 – Continuous Transaction Streaming

* Modified the Producer to simulate continuous real-time streaming.
* Added a 1-second delay between transactions.
* Verified continuous transaction publishing.

---

## Day 6 – Kafka Consumer

* Implemented a Kafka Consumer.
* Consumed transactions from the Kafka topic.
* Displayed transaction details in real time.
* Verified Producer–Consumer communication.

---

## Day 7 – Enhanced Consumer

* Displayed complete transaction details.
* Displayed transaction number, type, amount, origin, and destination accounts.
* Added fraud detection using the `isFraud` field.
* Counted processed and fraudulent transactions.
* Improved console output formatting.

---

## Technologies Used

* Python
* Apache Kafka
* Docker & Docker Compose
* Pandas
* JSON
* kafka-python

---

## Week 1 Outcome

Successfully built a real-time transaction streaming pipeline using Apache Kafka. The Producer continuously streams PaySim transactions, while the Consumer receives, displays, and monitors them for fraudulent activity in real time. This completes the Week 1 infrastructure and streaming pipeline, providing the foundation for machine learning–based fraud detection in the following weeks.
