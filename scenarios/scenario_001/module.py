from ..processing_methods import cf_process_pool, cf_thread_pool, multiprocessing, threading, dask, pyspark
from .. import performance_metrics as pm
import generate_data as gd


def run_scenario(scenario):

    # Generate csv files
    input_files = gd.generate_csv_files(
        path=scenario['input_dir_path'], num_rows=10000)

    # Display list of scenarios
    print("Available Methods:")
    for i, method in enumerate(scenario["methods"]):
        print(f"{i}: {method}")
    # Prompt user to select processing method
    method_index = int(
        input("Please select a method to run this scenario by entering its index number: "))

    if method_index >= len(scenario['methods']):
        print(
            f"Invalid method index. Please select a number between 0 and {len(scenario['methods']) - 1}")
        return
    selected_method = scenario['methods'][method_index]
    # Prompt user to ask if want to compare avaiabe methods
    compare_methods = input(
        "Do you want to compare the available methods? (y/n): ")
    if compare_methods.lower() == "y":
        compare_methods = True
    elif compare_methods.lower() == "n":
        compare_methods = False
    else:
        print("Invalid response.")
        return

    processing_results = list()

    if compare_methods:
        for method in scenario['methods']:
            print(f'Processing {method}')
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = run_operation(
                method, input_files)

            processing_results.append(
                {'method': method, 'cpu_time': cpu_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage, 'disk_usage': disk_usage})
    else:
        print(f'Processing {selected_method}')
        results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = run_operation(
            selected_method, input_files)
        processing_results.append(
            {'method': selected_method, 'cpu_time': cpu_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage, 'disk_usage': disk_usage})

    # gd.delete_files(input_files)

    methods_comparation = pm.compare_method(
        selected_method, processing_results)


def run_operation(method, input_files):
    # Define the number of iterations to perform
    num_iterations = 4

    # Initialize empty lists to store the measurements for each iteration
    results_list = []
    cpu_time_list = []
    cpu_total_usage_list = []
    cpu_usage_list = []
    disk_usage_list = []
    # Execute the selected method for the specified number of iterations
    for i in range(num_iterations):
        # Read in the input files using the selected parallel file I/O method
        if method == "multiprocessing":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                multiprocessing.read_csv_files, input_files)
        elif method == "threading":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                threading.read_csv_files, input_files)
        elif method == "concurrent_futures_process_pool":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                cf_process_pool.read_csv_files, input_files)
        elif method == "concurrent_futures_thread_pool":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                cf_thread_pool.read_csv_files, input_files)
        elif method == "dask":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                dask.read_csv_files, input_files)
        elif method == "pyspark":
            results, cpu_time, cpu_total_usage, cpu_usage, disk_usage = pm.measure_function(
                pyspark.read_csv_files, input_files)
        else:
            raise ValueError("Invalid method selected.")

        # Append the measurements to the corresponding lists
        cpu_time_list.append(cpu_time)
        cpu_total_usage_list.append(cpu_total_usage)
        cpu_usage_list.append(cpu_usage)
        disk_usage_list.append(disk_usage)

    # Average the measurements across all iterations
    cpu_time = sum(cpu_time_list) / num_iterations
    cpu_total_usage = sum(cpu_total_usage_list) / num_iterations
    disk_usage = sum(disk_usage_list) / num_iterations
    cpu_usage = []

    # Sort the cpu_usage list in descending order and format each item to 2 decimal places
    cpu_usage_list = [[usage for usage in sorted(cpu, reverse=True)]
                      for cpu in cpu_usage_list]

    # Calculate the average cpu usage
    cpu_usage = [round(sum(core)/len(core), 2)
                 for core in zip(*cpu_usage_list)]

    return results, cpu_time, cpu_total_usage, cpu_usage, disk_usage
