import csv
import concurrent.futures
from typing import Callable, List


# Define a function to read a CSV file
def read_csv_file(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        return data


# Define a function to read CSV files using concurrent.futures
def read_csv_files(files):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(read_csv_file, files))
    return results

# -------------------------------------------------------------------------------------


# Define a CPU-bound function to run in parallel
def square(number):
    result = 0
    for i in range(number):
        result += i ** 2
    return result


# Define a function to run the square function using concurrent.futures
def run_square(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))
    return results

# ----------------------------------------------------------------------------------------


def generate_csv_files(path: str, num_rows: int, generate_funcs: List[Callable[[str, int], str]]) -> List[str]:
    if not generate_funcs:
        return None
    files = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for generate_func in generate_funcs:
            future = executor.submit(generate_func, path, num_rows)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                files.append(result)
    return files
