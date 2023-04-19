import os
import sqlite3


def create_table(conn, table, schema):
    # Create table if it does not exist
    query = f"CREATE TABLE IF NOT EXISTS {table} ({schema})"
    conn.execute(query)


def insert_data(conn, table, data):
    # Insert data into table
    for row in data:
        columns = ", ".join(row.keys())
        placeholders = ", ".join("?" for _ in row.values())
        values = tuple(row.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        conn.execute(query, values)


def select_all(conn, table):
    # Select all data from table
    query = f"SELECT * FROM {table}"
    return conn.execute(query).fetchall()


def select_sales_by_date(conn, table, date):
    # Select sales by date
    query = f"SELECT * FROM {table} WHERE date=?"
    return conn.execute(query, (date,)).fetchall()


def select_total_quantity_and_price(conn, table, item):
    # Select total quantity and price for given item
    query = f"SELECT SUM(quantity), SUM(price) FROM {table} WHERE item=?"
    return conn.execute(query, (item,)).fetchone()


def select_sales_with_min_quantity(conn, table, quantity):
    # Select sales with a quantity greater than or equal to the given value
    query = f"SELECT * FROM {table} WHERE quantity >= ?"
    return conn.execute(query, (quantity,)).fetchall()


def select_sales_with_product_in_name(conn, table):
    # Select sales with a product name that contains 'Product'
    query = f"SELECT * FROM {table} WHERE item LIKE '%Product%'"
    return conn.execute(query).fetchall()


def select_total_revenue(conn, table):
    # Select the total revenue (quantity x price) of all sales
    query = f"SELECT SUM(quantity * price) FROM {table}"
    return conn.execute(query).fetchone()


def add_column(conn, table, column, datatype):
    # Add a new column to table
    query = f"ALTER TABLE {table} ADD COLUMN {column} {datatype}"
    conn.execute(query)


def remove_column(conn, table, column):
    # Remove a column from table
    query = f"ALTER TABLE {table} DROP COLUMN {column}"
    conn.execute(query)


def run_scenario(scenario):
    # Create database connection
    conn = sqlite3.connect(scenario['data']['database'])

    # Create table if it does not exist
    schema = ", ".join(
        f"{v[0]} {v[1]}" for v in scenario['data']['schema'].items())
    create_table(conn, scenario['data']['table'], schema)

    # Insert data into table
    insert_data(conn, scenario['data']['table'], scenario['data']['data'])

    while True:
        # Prompt user to select objective
        print("Available objectives:")
        for objective in scenario['objectives']:
            print(f"{objective['id']}. {objective['description']}")
        print("0. Exit")

        operation = input("Select an objective: ")

        if operation == "0":
            break

        objective = next(
            (o for o in scenario['objectives'] if o['id'] == operation), None)
        if not objective:
            print(f"Invalid operation ID: {operation}")
            continue

        if operation == "01":
            # Select all sales from January 1, 2022
            query = "SELECT * FROM sales WHERE date='2022-01-01'"
            result = conn.execute(query).fetchall()
            print("Sales from January 1, 2022:")
            for row in result:
                print(row)
        if operation == "02":
            # Select the total quantity and price of all sales of Product A
            query = "SELECT SUM(quantity), SUM(price*quantity) FROM sales WHERE item='Product A'"
            result = conn.execute(query).fetchone()
            print("Total quantity and revenue from sales of Product A:")
            print(f"Quantity: {result[0]}, Revenue: {result[1]}")
        if operation == "03":
            # Select all sales with a quantity of 10 or more
            query = "SELECT * FROM sales WHERE quantity>=10"
            result = conn.execute(query).fetchall()
            print("Sales with a quantity of 10 or more:")
            for row in result:
                print(row)
        if operation == "04":
            # Select all sales of products that have 'Product' in the name
            query = "SELECT * FROM sales WHERE item LIKE '%Product%'"
            result = conn.execute(query).fetchall()
            print("Sales of products with 'Product' in the name:")
            for row in result:
                print(row)
        if operation == "05":
            # Select the total revenue (quantity x price) of all sales
            query = "SELECT SUM(quantity*price) FROM sales"
            result = conn.execute(query).fetchone()
            print("Total revenue from all sales:")
            print(result[0])
        else:
            print(f"Invalid operation ID: {operation}")

    # Close database connection
    conn.close()
