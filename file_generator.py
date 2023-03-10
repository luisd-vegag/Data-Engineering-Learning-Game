import csv
from faker import Faker
import random


def generate_users_data(num_rows: int = 100) -> None:
    # Set the filename and number of rows
    filename = "system/users.csv"

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

    print(f"File {filename} created successfully.")


def generate_sales_data(num_rows: int = 100) -> None:

    # Set the filename and number of rows
    filename = "system/sales.csv"

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

    print(f"File {filename} created successfully.")


def generate_product_date():

    # Set the filename and number of rows
    filename = "system/products.csv"
    num_rows = 100

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

    print(f"File {filename} created successfully.")


def generate_customer_data():

    # Set the filename and number of rows
    filename = "system/customers.csv"
    num_rows = 100

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

    print(f"File {filename} created successfully.")
