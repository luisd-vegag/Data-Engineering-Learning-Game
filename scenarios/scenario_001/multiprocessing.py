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
