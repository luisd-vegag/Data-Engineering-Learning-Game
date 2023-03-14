import os
import time
import psutil


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


def measure_function(func, *args):
    '''
    # TODO:
        Fix and implement disk usage metric for all scenarios. Removed in commit 'Temporary removed disk usage performance metric'
    # 
    '''

    # Get the starting CPU time and usage for each core and total usage
    start_time = time.process_time()
    start_usage = psutil.cpu_percent(percpu=True)
    start_total_usage = psutil.cpu_percent()

    args = [*args]

    # Call the function with the provided arguments to measure
    result = func(*args)

    # Get the ending CPU time and usage for each core and total usage
    end_time = time.process_time()
    end_usage = psutil.cpu_percent(percpu=True)
    end_total_usage = psutil.cpu_percent()

    # Calculate the CPU time and usage for each core and total usage
    cpu_time = end_time - start_time
    cpu_usage = []
    for i in range(len(start_usage)):
        usage = end_usage[i] - start_usage[i]
        cpu_usage.append(round(usage, 4))

    cpu_total_usage = end_total_usage - start_total_usage

    # Return the result and measurements
    return result, cpu_time, cpu_total_usage, cpu_usage


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
    cpu_total_usage_diffs = {}

    for method in other_methods:
        cpu_time_diff = method_dict['cpu_time'] - method['cpu_time']
        cpu_total_usage_diff = method_dict['cpu_total_usage'] - \
            method['cpu_total_usage']

        cpu_time_diffs[method['method']] = cpu_time_diff
        cpu_total_usage_diffs[method['method']] = cpu_total_usage_diff
        cpu_usage_per_core_per_method[method['method']
                                      ] = method['cpu_usage']

    # Create a dictionary with the comparison results
    comparison_results = {
        'method': selected_method,
        'cpu_time': method_dict['cpu_time'],
        'cpu_total_usage': method_dict['cpu_total_usage'],
        'cpu_time_diffs': cpu_time_diffs,
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
    print(f"CPU total usage: {results['cpu_total_usage']:.2f}%")

    if len(results['cpu_time_diffs']) > 0:
        print("")
        print("CPU time differences compared to other methods (`+` is less than selected):")
        for method, diff in results['cpu_time_diffs'].items():
            diff_percent = (diff / results['cpu_time']) * 100
            if diff > 0:
                print(f"{method}: +{diff_percent:.2f}%")
            else:
                print(f"{method}: {diff_percent:.2f}%")

        print("")

    print(f"Core usage per method:")

    for method, core_usage in results['cpu_usage_per_core_per_method'].items():
        print(f"{method.rjust(35)}: {core_usage}")
