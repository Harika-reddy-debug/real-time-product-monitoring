from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.functions import col, from_json, expr

spark = SparkSession.builder \
    .appName("KafkaToClickHouse") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

kafka_topic = "customer-events"

schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("product", StringType()) \
    .add("action", StringType()) \
    .add("timestamp", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", kafka_topic) \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = json_df.writeStream \
    .format("jdbc") \
    .outputMode("append") \
    .option("url", "jdbc:clickhouse://clickhouse:8123") \
    .option("dbtable", "customer_events") \
    .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
    .start()

query.awaitTermination()

