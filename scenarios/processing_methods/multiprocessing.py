import csv
import multiprocessing


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
