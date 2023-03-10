import resource
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
    # Get the starting CPU time and resource usage
    start_time = time.process_time()
    start_usage = resource.getrusage(resource.RUSAGE_SELF)

    # Call the function with the provided arguments to measure
    result = func(*args)

    # Get the ending CPU time and resource usage
    end_time = time.process_time()
    end_usage = resource.getrusage(resource.RUSAGE_SELF)

    # Calculate the CPU time and resource usage
    cpu_time = end_time - start_time
    cpu_usage = end_usage.ru_utime - start_usage.ru_utime

    # Return the result and measurements
    return result, cpu_time, cpu_usage


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

    # Find the method to compare and separate it from the other methods
    for method in processing_results:
        if method['method'] == selected_method:
            method_dict = method
        else:
            other_methods.append(method)

    # Calculate the CPU time and usage differences for each other method compared to the target method
    cpu_time_diffs = {}
    cpu_usage_diffs = {}

    for method in other_methods:
        cpu_time_diff = method_dict['cpu_time'] - method['cpu_time']
        cpu_usage_diff = method_dict['cpu_usage'] - method['cpu_usage']

        cpu_time_diffs[method['method']] = cpu_time_diff
        cpu_usage_diffs[method['method']] = cpu_usage_diff

    # Create a dictionary with the comparison results
    comparison_results = {
        'method': selected_method,
        'cpu_time': method_dict['cpu_time'],
        'cpu_usage': method_dict['cpu_usage'],
        'cpu_time_diffs': cpu_time_diffs,
        'cpu_usage_diffs': cpu_usage_diffs
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
    print(f"CPU time: {results['cpu_time']}")
    print(f"CPU usage: {results['cpu_usage']}")
    print("")
    print("CPU time differences compared to other methods (`+` is better):")

    for method, diff in results['cpu_time_diffs'].items():
        diff_percent = (diff / results['cpu_time']) * 100
        if diff > 0:
            print(f"{method}: +{diff_percent:.2f}%")
        else:
            print(f"{method}: {diff_percent:.2f}%")

    print("")
    print("CPU usage differences compared to other methods (`+` is better):")

    for method, diff in results['cpu_usage_diffs'].items():
        diff_percent = (diff / results['cpu_usage']) * 100
        if diff > 0:
            print(f"{method}: +{diff_percent:.2f}%")
        else:
            print(f"{method}: {diff_percent:.2f}%")
