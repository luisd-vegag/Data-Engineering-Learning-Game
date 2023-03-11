import time
from pyspark.sql import SparkSession

# Define a function to read CSV files using PySpark


def read_csv_files(spark, files):
    df = spark.read.csv(files, header=True, inferSchema=True)
    results = df.collect()

    return results
