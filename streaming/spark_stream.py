from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("FraudDetectionStreaming") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    ) \
    .getOrCreate()

# Streaming Configuration
print("=" * 50)
print("STREAMING CONFIGURATION")
print("=" * 50)
print("Application Name :", spark.sparkContext.appName)
print("Kafka Server     : localhost:9092")
print("Kafka Topic      : transactions_v2")
print("Spark Version    :", spark.version)
print("=" * 50)

# Read Kafka Stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions_v2") \
    .load()

# Convert binary columns to string
transactions = df.selectExpr(
    "CAST(key AS STRING)",
    "CAST(value AS STRING)"
)

# Day 20 - Commit 2
print("=" * 50)
print("PREPARING STREAM RECORDS FOR FRAUD SCORING")
print("=" * 50)
print("Incoming transactions will be processed by the ML model.")

print("\nKafka Streaming DataFrame Created!")

# Schema Validation
print("\nKafka Stream Schema")
transactions.printSchema()

print("\nStreaming pipeline initialized successfully.")

spark.stop()