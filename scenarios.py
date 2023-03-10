from pyspark.sql import SparkSession
from pyspark.sql.functions import col

scenarios = {
    "csv_processing": {
        "name": "CSV processing",
        "description": "Process a large CSV file and output a summary report.",
        "input_file": "data.csv",
        "output_file": "report.txt",
        "num_processes": 4,
        "chunk_size": 100000,
    },
    "json_to_csv": {
        "name": "JSON to CSV",
        "description": "Convert a JSON file to a CSV file.",
        "input_file": "data.json",
        "output_file": "data.csv",
        "delimiter": ",",
    },
    "multiple_csv_to_parquet": {
        "name": "Multiple CSV to Parquet",
        "description": "Clean and join multiple CSV files and output a Parquet file with partitioning.",
        "input_files": ["sales.csv", "orders.csv"],
        "output_file": "output.parquet",
        "num_processes": 4,
        "chunk_size": 100000,
        "join_key": "order_id",
        "partition_keys": ["year", "month"],
    }
    # add more scenarios here
}


def multiple_csv_to_parquet(scenario):
    # Process the data
    spark = SparkSession.builder.appName("CSV to Parquet").getOrCreate()

    dfs = []
    for file in scenario["input_files"]:
        df = spark.read.format("csv").option("header", "true").load(file)
        # clean data here
        dfs.append(df)

    joined = dfs[0].join(dfs[1], on=scenario["join_key"])
    # more data cleaning and processing here

    partition_cols = scenario["partition_keys"]
    partition_data = joined.select(*partition_cols)
    joined = joined.drop(*partition_cols)

    joined.write.partitionBy(partition_cols).parquet(
        scenario["output_file"],
        compression="snappy",
    )

    # Provide feedback
    print("Processing complete.")
