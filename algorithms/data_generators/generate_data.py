import csv
from typing import List
from faker import Faker
import random
import os


def generate_csv_files(path: str = 'local/data/', num_rows: int = 100) -> List:
    files = list()
    files.append(generate_users_data(path, num_rows))
    files.append(generate_sales_data(path, num_rows))
    files.append(generate_product_date(path, num_rows))
    files.append(generate_customer_data(path, num_rows))
    return files


def delete_files(files: list) -> None:
    for file in files:
        try:
            os.remove(file)
            # print(f"File {file} deleted successfully.")
        except OSError as e:
            print(f"Error deleting file {file}: {e}")


def generate_users_data(path: str = '', num_rows: int = 100) -> str:
    # Set the filename and number of rows
    filename = path + "users.csv"

    # Delete the file if it already exists
    if os.path.exists(filename):
        return filename
        # os.remove(filename)
        # print(f"File {filename} deleted successfully.")

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
            print(i)

    print(f"File {filename} created successfully.")
    return filename


def generate_sales_data(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "sales.csv"

    # Delete the file if it already exists
    if os.path.exists(filename):
        return filename
        # os.remove(filename)
        # print(f"File {filename} deleted successfully.")

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
            print(i)

    print(f"File {filename} created successfully.")
    return filename


def generate_product_date(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "products.csv"

    # Delete the file if it already exists
    if os.path.exists(filename):
        return filename
        # os.remove(filename)
        # print(f"File {filename} deleted successfully.")

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
            print(i)

    print(f"File {filename} created successfully.")
    return filename


def generate_customer_data(path: str = '', num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = path + "customers.csv"

    # Delete the file if it already exists
    if os.path.exists(filename):
        return filename
        # os.remove(filename)
        # print(f"File {filename} deleted successfully.")

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
            print(i)

    print(f"File {filename} created successfully.")
    return filename


if __name__ == '__main__':
    generate_csv_files()
