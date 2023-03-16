from .. import performance_metrics as pm
from ..processing_methods import cf_process_pool, cf_thread_pool, multiprocessing, threading, dask, pyspark

import csv
from faker import Faker
import random
import os
import importlib
import shutil
import time

'''
# TODO:
'''


def run_scenario(scenario):

    # Display list of scenarios
    print("Available Methods:")
    for i, method in enumerate(scenario["methods"]):
        print(f"{i}: {method}")
    # Prompt user to select processing method
    method_index = int(
        input("Please select a method to run this scenario by entering its index number: "))

    if method_index >= len(scenario['methods']):
        print(
            f"Invalid method index. Please select a number between 0 and {len(scenario['methods']) - 1}")
        return
    selected_method = scenario['methods'][method_index]
    # Prompt user to ask if want to compare avaiabe methods
    compare_methods = input(
        "Do you want to compare the available methods? (y/n): ")
    if compare_methods.lower() == "y":
        compare_methods = True
    elif compare_methods.lower() == "n":
        compare_methods = False
    else:
        print("Invalid response.")
        return

    processing_results = list()

    if compare_methods:
        for method in scenario['methods']:
            print(f'Processing {method}')
            results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = run_operation(
                method,  scenario['output_dir_path'], scenario['num_rows'], scenario['functions'])

            processing_results.append(
                {'method': method, 'cpu_time': cpu_time, 'wall_clock_time': wall_clock_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage})
    else:
        print(f'Processing {selected_method}')
        results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = run_operation(
            selected_method,  scenario['output_dir_path'], scenario['num_rows'], scenario['functions'])
        processing_results.append(
            {'method': selected_method, 'cpu_time': cpu_time, 'wall_clock_time': wall_clock_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage})

    # gd.delete_files(input_files)

    methods_comparation = pm.compare_method(
        selected_method, processing_results)


def run_operation(method, path, num_rows, generate_funcs):
    # Define the number of iterations to perform
    num_iterations = 4

    # Initialize empty lists to store the measurements for each iteration
    results_list = []
    cpu_time_list = []
    cpu_total_usage_list = []
    cpu_usage_list = []
    wall_clock_time_list = []

    # Import the generate functions by their names
    generate_funcs = [getattr(importlib.import_module(
        f'{__package__}.module'), func_name) for func_name in generate_funcs]

    # Execute the selected method for the specified number of iterations
    for i in range(num_iterations):
        clear_directory(path)
        # Read in the input files using the selected parallel file I/O method
        if method == "multiprocessing":
            results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = pm.measure_performance(
                multiprocessing.generate_csv_files,  path, num_rows, generate_funcs)
        elif method == "threading":
            results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = pm.measure_performance(
                threading.generate_csv_files,  path, num_rows, generate_funcs)
        elif method == "concurrent_futures_process_pool":
            results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = pm.measure_performance(
                cf_process_pool.generate_csv_files,  path, num_rows, generate_funcs)
        elif method == "concurrent_futures_thread_pool":
            results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time = pm.measure_performance(
                cf_thread_pool.generate_csv_files,  path, num_rows, generate_funcs)
        else:
            raise ValueError("Invalid method selected.")

        # Append the measurements to the corresponding lists
        cpu_time_list.append(cpu_time)
        cpu_total_usage_list.append(cpu_total_usage)
        cpu_usage_list.append(cpu_usage)
        wall_clock_time_list.append(wall_clock_time)

    # Average the measurements across all iterations
    cpu_time = sum(cpu_time_list) / num_iterations
    wall_clock_time = sum(wall_clock_time_list) / num_iterations
    cpu_total_usage = sum(cpu_total_usage_list) / num_iterations
    cpu_usage = []

    # Sort the cpu_usage list in descending order and format each item to 2 decimal places
    cpu_usage_list = [[usage for usage in sorted(cpu, reverse=True)]
                      for cpu in cpu_usage_list]

    # Calculate the average cpu usage
    cpu_usage = [round(sum(core)/len(core), 2)
                 for core in zip(*cpu_usage_list)]

    return results, cpu_time, cpu_total_usage, cpu_usage, wall_clock_time


def clear_directory(directory_path):
    # Check if the directory exists
    if os.path.exists(directory_path):
        # Remove all files and subdirectories inside the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error removing file or directory {file_path}: {e}")
        # print(f"Directory {directory_path} in now empty")
    else:
        # If the directory does not exist, print an error message
        pass
        # print(f"Directory {directory_path} does not exist")


def generate_users_data(path: str = '', num_rows: int = 100) -> str:
    # Set the filename and number of rows
    filename = path + "users.csv"

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set the column names
    headers = ["id", "name", "age", "city"]

    # Generate the data and write to the CSV file
    fake = Faker()
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for i in range(num_rows):
            row = [
                i + 1,
                fake.name(),
                fake.random_int(min=18, max=65),
                fake.city(),
            ]
            writer.writerow(row)

    # print(f"File {filename} created successfully.")
    return filename


def generate_sales_data(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "sales.csv"

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set the column names
    headers = ["order_id", "quantity", "price", "total", "date"]

    # Generate the data and write to the CSV file
    fake = Faker()
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for i in range(num_rows):
            product_name = fake.word() + " " + fake.word()
            quantity = random.randint(1, 10)
            price = round(random.uniform(10.0, 100.0), 2)
            total = round(quantity * price, 2)
            date = fake.date_between(start_date="-30d", end_date="today")
            row = [
                i + 1,
                fake.name(),
                product_name,
                quantity,
                price,
                total,
                date,
            ]
            writer.writerow(row)

    # print(f"File {filename} created successfully.")
    return filename


def generate_product_date(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "products.csv"

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set the column names
    headers = ["product_id", "brand", "name", "category", "price"]

    # Define the shoe categories and brands
    shoe_categories = ["Sneakers", "Sandals", "Boots", "Loafers"]
    shoe_brands = ["Adidas", "Nike", "Puma", "Reebok", "Vans"]

    # Generate the data and write to the CSV file
    fake = Faker()
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for i in range(num_rows):
            brand = random.choice(shoe_brands)
            name = fake.word() + " " + fake.word()
            category = random.choice(shoe_categories)
            price = round(random.uniform(50.0, 150.0), 2)
            row = [
                i + 1,
                brand,
                name,
                category,
                price,
            ]
            writer.writerow(row)

    # print(f"File {filename} created successfully.")
    return filename


def generate_customer_data(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "customers.csv"

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set the column names
    headers = ["customer_id", "first_name",
               "last_name", "email", "phone_number", "address"]

    # Generate the data and write to the CSV file
    fake = Faker()
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for i in range(num_rows):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            address = fake.address()
            row = [
                i + 1,
                first_name,
                last_name,
                email,
                phone_number,
                address,
            ]
            writer.writerow(row)

    # print(f"File {filename} created successfully.")
    return filename
