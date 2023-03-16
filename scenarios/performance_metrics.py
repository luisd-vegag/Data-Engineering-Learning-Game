import os
import time
import psutil
import asyncio
import concurrent.futures


def show_compute_specs():
    # Get the number of CPU cores
    num_cores = psutil.cpu_count(logical=True)

    # Get the CPU frequency
    cpu_freq = psutil.cpu_freq()

    # Get the total and available system memory
    mem_info = psutil.virtual_memory()

    # Print the system information
    print(f"Number of cores: {num_cores}")
    print(f"CPU frequency: {cpu_freq.current:.2f} GHz")
    print(f"Total memory: {mem_info.total / (1024**3):.2f} GB")
    print(f"Available memory: {mem_info.available / (1024**3):.2f} GB")


def measure_performance(func, *args):
    '''
    Measure the performance of a function by calculating its CPU time, CPU usage, and wall clock time.

    Args:
    - func: the function to measure
    - args: the arguments to pass to the function

    Returns:
    - result: the return value of the function
    - cpu_time: the CPU time used by the function in seconds
    - cpu_usage: a list of the CPU usage for each core during the function execution
    - cpu_total_usage: the total CPU usage during the function execution
    - wall_clock_time: the wall clock time taken to execute the function in seconds
    '''

    # Get the starting CPU time and usage for each core and total usage
    start_time = time.process_time()
    start_usage = psutil.cpu_times_percent()

    # Get the starting wall clock time
    start_wall_clock_time = time.perf_counter()

    args = [*args]

    # Call the function with the provided arguments to measure
    result = func(*args)

    # Get the ending CPU time and usage for each core and total usage
    end_time = time.process_time()
    end_usage = psutil.cpu_times_percent()

    # Get the ending wall clock time
    end_wall_clock_time = time.perf_counter()

    # Calculate the CPU time and usage for each core and total usage
    cpu_time = end_time - start_time
    cpu_total_usage = end_usage.user + end_usage.system - \
        start_usage.user - start_usage.system

    cpu_usage = []
    for i in range(psutil.cpu_count()):
        usage = end_usage[i] - start_usage[i]
        cpu_usage.append(round(usage, 4))

    # Calculate the wall clock time for the function execution
    wall_clock_time = end_wall_clock_time - start_wall_clock_time

    # Return the result and measurements
    return result, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time


def compare_method(selected_method, processing_results):
    """
    Compares the CPU time and usage of a specific method to the other methods in the list.

    Args:
        selected_method (str): The name of the method to compare.
        processing_results (list): The list of method dictionaries to compare against.

    Returns:
        A dictionary containing the comparison results.
    """
    method_dict = {}
    other_methods = []
    cpu_usage_per_core_per_method = {}

    # Find the method to compare and separate it from the other methods
    for method in processing_results:
        if method['method'] == selected_method:
            method_dict = method
            cpu_usage_per_core_per_method[method['method']
                                          ] = method['cpu_usage']
        else:
            other_methods.append(method)

    # Calculate the CPU time and usage differences for each other method compared to the target method
    cpu_time_diffs = {}
    wall_clock_time_diffs = {}
    cpu_total_usage_diffs = {}

    for method in other_methods:
        cpu_time_diff = method_dict['cpu_time'] - method['cpu_time']
        wall_clock_time_diff = method_dict['wall_clock_time'] - \
            method['wall_clock_time']
        cpu_total_usage_diff = method_dict['cpu_total_usage'] - \
            method['cpu_total_usage']

        cpu_time_diffs[method['method']] = cpu_time_diff
        wall_clock_time_diffs[method['method']] = wall_clock_time_diff
        cpu_total_usage_diffs[method['method']] = cpu_total_usage_diff
        cpu_usage_per_core_per_method[method['method']
                                      ] = method['cpu_usage']

    # Create a dictionary with the comparison results
    comparison_results = {
        'method': selected_method,
        'cpu_time': method_dict['cpu_time'],
        'wall_clock_time': method_dict['wall_clock_time'],
        'cpu_total_usage': method_dict['cpu_total_usage'],
        'cpu_time_diffs': cpu_time_diffs,
        'wall_clock_time_diffs': wall_clock_time_diffs,
        'cpu_total_usage_diffs': cpu_total_usage_diffs,
        'cpu_usage_per_core_per_method': cpu_usage_per_core_per_method
    }
    display_comparison_results(comparison_results)
    return comparison_results


def display_comparison_results(results):
    """
    Displays the comparison results in a well-organized form with differences in percentage.

    Args:
        results (dict): The comparison results dictionary.
    """
    print("")
    print(f"Comparison results for {results['method']} method:")
    print(f"CPU time: {results['cpu_time']:.4f}")
    print(f"Wall clock time: {results['wall_clock_time']:.4f}")
    print(f"CPU usage: {results['cpu_total_usage']:.2f}%")

    if len(results['cpu_time_diffs']) > 0:
        print("")
        print("CPU time differences compared to other methods (`+` is less time than selected):")
        for method, diff in results['cpu_time_diffs'].items():
            diff_percent = (diff / results['cpu_time']) * 100
            if diff > 0:
                print(f"{method}: +{diff_percent:.2f}%")
            else:
                print(f"{method}: {diff_percent:.2f}%")

        print("")
        print("Wall clock time differences compared to other methods (`+` is less time than selected):")
        for method, diff in results['wall_clock_time_diffs'].items():
            diff_percent = (diff / results['wall_clock_time']) * 100
            if diff > 0:
                print(f"{method}: +{diff_percent:.2f}%")
            else:
                print(f"{method}: {diff_percent:.2f}%")

        print("")
        print("CPU usage differences compared to other methods (`+` is more CPU than selected):")
        for method, diff in results['cpu_total_usage_diffs'].items():
            diff = diff*-1
            diff_percent = (diff / results['cpu_total_usage']) * 100
            if diff > 0:
                print(f"{method}: +{diff_percent:.2f}%")
            else:
                print(f"{method}: {diff_percent:.2f}%")
        print("")

    print(f"Core usage per method:")

    for method, core_usage in results['cpu_usage_per_core_per_method'].items():
        print(f"{method.rjust(35)}: {core_usage}")
