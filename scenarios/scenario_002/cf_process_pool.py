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
