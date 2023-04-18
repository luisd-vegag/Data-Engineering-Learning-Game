import csv
import threading
import queue as q
from typing import Callable, List


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

# ---------------------------------------------------


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


# ----------------------------------


def generate_csv_files(path: str, num_rows: int, generate_funcs: List[Callable[[str, int], str]]) -> List[str]:
    if not generate_funcs:
        return None
    files = []
    # Create a thread-safe queue to hold the generated file names
    result_queue = q.Queue()

    def generate_file(generate_func: Callable[[str, int], str]):
        # Generate the file using the given function and add the result to the queue
        result = generate_func(path, num_rows)
        if result:
            result_queue.put(result)

    # Create a thread for each generate function and start them
    threads = []
    for generate_func in generate_funcs:
        thread = threading.Thread(target=generate_file, args=(generate_func,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish and collect the results from the queue
    for thread in threads:
        thread.join()
    while not result_queue.empty():
        files.append(result_queue.get())

    return files
