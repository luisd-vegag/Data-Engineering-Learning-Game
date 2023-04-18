import csv
import multiprocessing
from typing import Callable, List


# Define a function to read a CSV file


def read_csv_file(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        return data


# Define a function to read CSV files using multiprocessing
def read_csv_files(files):
    with multiprocessing.Pool() as pool:
        results = pool.map(read_csv_file, files)
    return results


def square(number):
    result = 0
    for i in range(number):
        result += i ** 2
    return result


# Define a function to run the square function using concurrent.futures
def run_square(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    return results


# ---------------------------------------------------------
def generate_csv_files(path: str, num_rows: int, generate_funcs: List[Callable[[str, int], str]]) -> List[str]:
    if not generate_funcs:
        return None
    files = []
    with multiprocessing.Pool() as pool:
        results = []
        for generate_func in generate_funcs:
            result = pool.apply_async(generate_func, (path, num_rows))
            results.append(result)
        for result in results:
            file = result.get()
            if file:
                files.append(file)
    return files
