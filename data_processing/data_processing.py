from . import multiprocessing, threading, concurrent_futures, dask, pyspark
import pandas as pd
import compute_measurements as cm
from pyspark.sql import SparkSession


def run_scenario(scenario, input_files, method):
    # Read in the input files using the selected parallel file I/O method
    if method == "multiprocessing":
        results, cpu_time, cpu_usage = cm.measure_function(
            multiprocessing.read_csv_files, input_files)
    elif method == "threading":
        results, cpu_time, cpu_usage = cm.measure_function(
            threading.read_csv_files, input_files)
    elif method == "concurrent_futures":
        results, cpu_time, cpu_usage = cm.measure_function(
            concurrent_futures.read_csv_files, input_files)
    elif method == "dask":
        results, cpu_time, cpu_usage = cm.measure_function(
            dask.read_csv_files, input_files)
    elif method == "pyspark":
        spark = SparkSession.builder.appName("ReadCSVFiles").getOrCreate()
        # Set the log level to ERROR to remove WARN and INFO logs
        spark.sparkContext.setLogLevel("ERROR")
        results, cpu_time, cpu_usage = cm.measure_function(
            pyspark.read_csv_files, spark, input_files)
        spark.stop()
    else:
        raise ValueError("Invalid method selected.")

    return results, cpu_time, cpu_usage
