import csv
import concurrent.futures

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


# Define a CPU-bound function to run in parallel
def square(number):
    result = 0
    for i in range(number):
        result += i ** 2
    return result


# Define a function to run the square function using concurrent.futures
def run_square(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(square, numbers))
    return results
