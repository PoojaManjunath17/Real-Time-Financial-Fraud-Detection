# Week 3 Progress Report

## Project Title
**Real-Time Financial Fraud Detection Pipeline Using Apache Kafka, Apache Spark, and Machine Learning**

---

## Week 3 Objective

The objective of Week 3 was to integrate the trained Machine Learning model with Apache Spark Structured Streaming to perform real-time fraud detection on streaming transaction data from Apache Kafka.

---

# Day 15 – Apache Spark Setup

## Tasks Completed
- Installed PySpark.
- Configured Apache Spark environment.
- Created Spark Session.
- Verified Spark installation.
- Configured Hadoop for Windows.

## Outcome
Apache Spark was successfully configured for streaming applications.

---

# Day 16 – Spark and Kafka Integration

## Tasks Completed
- Connected Apache Spark with Apache Kafka.
- Configured Kafka topic (`transactions_v2`).
- Created Spark Streaming DataFrame.
- Converted Kafka messages from binary to string format.
- Displayed streaming schema.

## Outcome
Spark successfully connected to Kafka and was ready to consume streaming data.

---

# Day 17 – Streaming Pipeline Initialization

## Tasks Completed
- Read transactions from Kafka.
- Validated streaming schema.
- Displayed Spark configuration details.
- Initialized the streaming pipeline.

## Outcome
A real-time streaming pipeline was successfully created.

---

# Day 18 – Machine Learning Model Integration

## Tasks Completed
- Loaded the trained Logistic Regression model.
- Tested prediction using sample transaction.
- Displayed prediction probability.
- Verified successful model loading.

## Outcome
The machine learning model was successfully integrated into the project.

---

# Day 19 – Prediction Functions

## Tasks Completed
- Created reusable prediction function.
- Added batch prediction helper.
- Prepared streaming records for prediction.
- Validated prediction workflow.

## Outcome
Prediction functions were successfully prepared for streaming transactions.

---

# Day 20 – Fraud Scoring Pipeline

## Tasks Completed
- Added batch prediction helper.
- Prepared incoming stream records for fraud scoring.
- Displayed model scoring status.
- Added streaming pipeline summary.

## Outcome
The fraud detection pipeline was prepared to evaluate incoming transactions in real time.

---

# Day 21 – Fraud Alert Simulation

## Tasks Completed
- Implemented fraud alert helper function.
- Simulated fraud alert generation.
- Added fraud scoring summary.
- Simulated routing fraud alerts to a dedicated Fraud Alerts database.

## Outcome
The streaming pipeline was enhanced to simulate real-time fraud alert generation and routing.

---

# Technologies Used

- Python
- Apache Spark (PySpark)
- Apache Kafka
- Scikit-learn
- Pandas
- Joblib
- Docker
- JSON

---

# Project Structure

```text
Week2Project/
│
├── analysis/
│   ├── data_analysis.py
│   └── feature_engineering.py
│
├── producer/
│   └── producer.py
│
├── consumer/
│   └── consumer.py
│
├── models/
│   ├── train_model.py
│   └── fraud_detection_model.pkl
│
├── streaming/
│   ├── spark_stream.py
│   └── model_inference.py
│
└── WEEK3_REPORT.md
```

---

# Week 3 Outcome

- Apache Spark was successfully configured.
- Kafka streaming was integrated with Spark.
- The trained Logistic Regression model was loaded for prediction.
- Fraud prediction functions were developed.
- Fraud scoring pipeline was prepared.
- Fraud alert generation and database routing were successfully simulated.

---

# Next Week Plan (Week 4)

- Connect streaming pipeline to database.
- Store fraud alerts.
- Create monitoring dashboard.
- Visualize fraud statistics.
- Optimize streaming performance.