from . import multiprocessing, threading, concurrent_futures, dask, pyspark
import pandas as pd
import compute_measurements as cm
from pyspark.sql import SparkSession


def run_scenario(scenario, input_files, method):
    # Define the number of iterations to perform
    num_iterations = 4

    # Initialize empty lists to store the measurements for each iteration
    results_list = []
    cpu_time_list = []
    cpu_total_usage_list = []
    cpu_usage_list = []

    # Create Spark session
    spark = SparkSession.builder.appName("ReadCSVFiles").getOrCreate()
    # Set the log level to ERROR to remove WARN and INFO logs
    spark.sparkContext.setLogLevel("ERROR")

    # Execute the selected method for the specified number of iterations
    for i in range(num_iterations):
        # Read in the input files using the selected parallel file I/O method
        if method == "multiprocessing":
            results, cpu_time, cpu_total_usage, cpu_usage = cm.measure_function(
                multiprocessing.read_csv_files, input_files)
        elif method == "threading":
            results, cpu_time, cpu_total_usage, cpu_usage = cm.measure_function(
                threading.read_csv_files, input_files)
        elif method == "concurrent_futures":
            results, cpu_time, cpu_total_usage, cpu_usage = cm.measure_function(
                concurrent_futures.read_csv_files, input_files)
        elif method == "dask":
            results, cpu_time, cpu_total_usage, cpu_usage = cm.measure_function(
                dask.read_csv_files, input_files)
        elif method == "pyspark":
            results, cpu_time, cpu_total_usage, cpu_usage = cm.measure_function(
                pyspark.read_csv_files, spark, input_files)
        else:
            raise ValueError("Invalid method selected.")

        # Append the measurements to the corresponding lists
        cpu_time_list.append(cpu_time)
        cpu_total_usage_list.append(cpu_total_usage)
        cpu_usage_list.append(cpu_usage)

    # Stop python sesion
    spark.stop()

    # Average the measurements across all iterations
    cpu_time = sum(cpu_time_list) / num_iterations
    cpu_total_usage = sum(cpu_total_usage_list) / num_iterations
    cpu_usage = []

    # Sort the cpu_usage list in descending order and format each item to 2 decimal places
    cpu_usage_list = [[usage for usage in sorted(cpu, reverse=True)]
                      for cpu in cpu_usage_list]

    # Calculate the average cpu usage
    cpu_usage = [round(sum(core)/len(core), 2)
                 for core in zip(*cpu_usage_list)]

    return results, cpu_time, cpu_total_usage, cpu_usage
