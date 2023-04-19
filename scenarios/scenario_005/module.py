import os
import sqlite3


def create_table(conn, table, schema):
    # Create table if it does not exist
    schema_str = ", ".join(f"{s['column']} {s['datatype']}" for s in schema)
    query = f"CREATE TABLE IF NOT EXISTS {table} ({schema_str})"
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


def show_table(conn, table):
    # Retrieve data from table and print it
    select_query = f"SELECT * FROM {table}"
    cursor = conn.execute(select_query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print(f"No data found in table '{table}'")
    else:
        print(f"Data in table '{table}':")
        headers = [description[0] for description in cursor.description]
        for header in headers:
            print(f"{header}\t", end="")
        print()
        for row in rows:
            for value in row:
                print(f"{value}\t", end="")
            print()
    print("\n")


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


def prompt_options(operation_options):
    for i, option in enumerate(operation_options):
        print(f"{i+1}: {option}")
    command_index = int(
        input("Enter the index number of your selection: "))-1
    if command_index not in range(len(operation_options)):
        print(
            f"Invalid selection. Please enter an index number between 1 and {len(operation_options)}.")
        return
    selected_command = operation_options[command_index]
    return selected_command


def run_scenario(scenario):
    # Create database directory if it doesn't exist
    db_directory = os.path.dirname(scenario['data']['database'])
    if not os.path.exists(db_directory):
        os.makedirs(db_directory)

    # Create database connection
    conn = sqlite3.connect(scenario['data']['database'])

    # Create table if it does not exist
    schema = scenario['data']['schema']
    create_table(conn, scenario['data']['table'], schema)

    # Insert data into table
    insert_data(conn, scenario['data']['table'], scenario['data']['data'])

    # Show table
    print("Here is the table you are going to work with:\n")
    show_table(conn, scenario['data']['table'])
    while True:
        # Prompt user to select objective
        print("Available objectives:")
        for objective in scenario['objectives']:
            print(f"{objective['id']}. {objective['description']}")
        print("0. Exit\n")

        operation = input("Select an objective: ")
        print("\n")
        if operation == "0":
            break

        objective = next(
            (o for o in scenario['objectives'] if o['id'] == operation), None)
        if not objective:
            print(f"Invalid operation ID: {operation}")
            continue

        if operation == "1":

            # Prompt user to select the options
            operation_options = ["FILTER", "AT", "WHERE", "WHEN"]
            print(
                "Please select the missing SQL statement that select the data from January 1, 2022")
            print("SELECT * FROM sales ... date = '2020-01-01'")
            selected_command = prompt_options(operation_options)

            # Verify that the selected command is correct
            if selected_command != "WHERE":
                print(
                    f"Invalid selection. '{selected_command}' is not a valid statement to select the data from January 1, 2022.")
                return

            # Select all sales from January 1, 2022
            query = "SELECT * FROM sales WHERE date='2022-01-01'"
            result = conn.execute(query).fetchall()
            print(f"QUERY: {query}")
            print("Sales from January 1, 2022:")
            for row in result:
                print(row)
            print("\n")

        elif operation == "2":

            # Prompt user to select the options
            operation_options = ["SUM(quantity), SUM(price)*SUM(quantity)",
                                 "SUM(quantity), SUM(price*quantity)", "SUM(quantity) SUM(price*quantity)"]
            print(
                "Please select the missing SQL statement that select the total quantity and price of all sales of Product A")
            print("SELECT ... FROM sales WHERE item='Product A'")
            selected_command = prompt_options(operation_options)

            # Verify that the selected command is correct
            if selected_command != "SUM(quantity), SUM(price*quantity)":
                print(
                    f"Invalid selection. '{selected_command}' is not a valid statement to select the total quantity and price of all sales of Product A")
                return

            # Select the total quantity and price of all sales of Product A
            query = "SELECT SUM(quantity), SUM(price*quantity) FROM sales WHERE item='Product A'"
            result = conn.execute(query).fetchone()
            print(f"QUERY: {query}")
            print("Total quantity and revenue from sales of Product A:")
            print(f"Quantity: {result[0]}, Revenue: {result[1]}")
            print("\n")

        elif operation == "3":
            # Prompt user to select the options
            operation_options = ["* ... WHERE quantity>=10",
                                 "ALL ... WHERE quantity<=10",
                                 "* ... WHEN quantity>=10",
                                 "* ... WHEN quantity=0"]
            print(
                "Please select the missing SQL statement that selects all sales with a quantity of 10 or more")
            print("SELECT ... FROM sales ...")
            selected_command = prompt_options(operation_options)

            # Verify that the selected command is correct
            if selected_command != "* ... WHERE quantity>=10":
                print(
                    f"Invalid selection. '{selected_command}' is not a valid statement to select all sales with a quantity of 10 or more.")
                return

            # Select all sales with a quantity of 10 or more
            query = "SELECT * FROM sales WHERE quantity>=10"
            result = conn.execute(query).fetchall()
            print(f"QUERY: {query}")
            print("Sales with a quantity of 10 or more:")
            for row in result:
                print(row)
            print("\n")

        elif operation == "4":
            # Prompt user to select the options
            operation_options = ["FIND '%Product%'",
                                 "WHERE item LIKE '%Product%'",
                                 "FIND 'product'",
                                 "WHERE LIKE item '%Product'",
                                 "FIND '%product%'",
                                 "WHERE item FIND '%Product%'"
                                 "LIKE %product%"]
            print("Please select the missing SQL statement that selects all sales of products that have 'Product' in the name")
            print("SELECT * FROM sales ...")
            selected_command = prompt_options(operation_options)

            # Verify that the selected command is correct
            if selected_command != "WHERE item LIKE '%Product%'":
                print(
                    f"Invalid selection. '{selected_command}' is not a valid statement to select all sales of products that have 'Product' in the name.")
                return

            # Select all sales of products that have 'Product' in the name
            query = "SELECT * FROM sales WHERE item LIKE '%Product%'"
            result = conn.execute(query).fetchall()
            print(f"QUERY: {query}")
            print("Sales of products with 'Product' in the name:")
            for row in result:
                print(row)
            print("\n")

        elif operation == "5":
            # Prompt user to select the options
            operation_options = ["SUM(quantity) x SUM(price)",
                                 "SUM(quantity * price)",
                                 "COUNT(quantity) * AVG(price)",
                                 "COUNT(*) x AVG(quantity * price)"]
            print(
                "Please select the missing SQL statement that calculates the total revenue (quantity x price) of all sales")
            print("SELECT ... FROM sales")
            selected_command = prompt_options(operation_options)

            # Verify that the selected command is correct
            if selected_command != "SUM(quantity * price)":
                print(
                    f"Invalid selection. '{selected_command}' is not a valid statement to calculate the total revenue (quantity x price) of all sales.")
                return

            # Select the total revenue (quantity x price) of all sales
            query = "SELECT SUM(quantity * price) FROM sales"
            result = conn.execute(query).fetchone()
            print(f"QUERY: {query}")
            print("Total revenue from all sales:")
            print(result[0])
            print("\n")

        else:
            print(f"Invalid operation ID: {operation}")

    # Close database connection
    conn.close()
