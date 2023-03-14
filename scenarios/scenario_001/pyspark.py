from pyspark.sql import SparkSession

# Define a function to read CSV files using PySpark


def read_csv_files(files):
    # Create Spark session
    spark = SparkSession.builder.appName("ReadCSVFiles").getOrCreate()
    # Set the log level to ERROR to remove WARN and INFO logs
    spark.sparkContext.setLogLevel("ERROR")
    df = spark.read.csv(files, header=True, inferSchema=True)
    results = df.collect()
    # Stop python sesion
    spark.stop()
    return results
