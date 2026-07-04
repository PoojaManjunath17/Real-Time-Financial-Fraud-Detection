from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("FraudDetectionStreaming") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    ) \
    .getOrCreate()
print("=" * 50)
print("SPARK STREAMING CONFIGURATION")
print("=" * 50)
print("Kafka Server : localhost:9092")
print("Kafka Topic  : transactions_v2")
print("Spark Version:", spark.version)
print("=" * 50)

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions_v2") \
    .load()

transactions = df.selectExpr(
    "CAST(key AS STRING)",
    "CAST(value AS STRING)"
)

print("Kafka Streaming DataFrame Created!")
transactions.printSchema()

spark.stop()