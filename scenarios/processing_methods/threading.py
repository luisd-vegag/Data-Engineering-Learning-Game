import csv
import threading
import queue as q


# Define a function to read a CSV file
def read_csv_file(file, queue):
    with open(file) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        queue.put(data)


# Define a function to read CSV files using threading
def read_csv_files(files):
    results = []
    queue = q.Queue()
    threads = []
    for file in files:
        t = threading.Thread(target=read_csv_file, args=(file, queue))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    while not queue.empty():
        result = queue.get()
        results.append(result)
    return results


def square(number, queue):
    result = 0
    for i in range(number):
        result += i ** 2
    queue.put(result)


# Define a function to run the square function using threading
def run_square(numbers):
    results = []
    queue = q.Queue()
    threads = []
    for number in numbers:
        t = threading.Thread(target=square, args=(number, queue))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    while not queue.empty():
        result = queue.get()
        results.append(result)
    return results
