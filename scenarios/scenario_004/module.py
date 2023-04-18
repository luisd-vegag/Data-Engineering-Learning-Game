import sqlite3
import os


def run_scenario(scenario):

    # Create database directory if it doesn't exist
    db_directory = os.path.dirname(scenario['database'])
    if not os.path.exists(db_directory):
        os.makedirs(db_directory)

    # Create database connection
    conn = sqlite3.connect(scenario['database'])

    # Prompt user to select operation
    print("Available operations:")
    print("1. Create table")
    print("2. Insert data into table")
    print("3. List tables")
    print("4. Remove table")
    print("5. Clear all data in table")
    print("6. View table data")

    operation = input("Please select an operation by entering its number: ")

    # Perform selected operation
    if operation == "1":
        # Check if table already exists and delete it if it does
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'")
        result = cursor.fetchone()
        if result is not None:
            cursor.execute(f"DROP TABLE {scenario['table']}")

        # Prompt user to select SQL command for creating the table
        create_table_options = ["CREATE TABLE", "NEW TABLE", "MAKE TABLE"]
        print("Please select an option for creating the table:")
        for i, option in enumerate(create_table_options):
            print(f"{i}: {option}")
        command_index = int(
            input("Enter the index number of your selection: "))
        if command_index not in range(len(create_table_options)):
            print(
                f"Invalid selection. Please enter an index number between 0 and {len(create_table_options)-1}.")
            return
        selected_command = create_table_options[command_index]

        # Verify that the selected command is correct
        if selected_command != "CREATE TABLE":
            print(
                f"Invalid selection. '{selected_command}' is not a valid command for creating a table.")
            return

        # Create table in database
        create_table_query = f"CREATE TABLE {scenario['table']} ({scenario['schema']['column1']} {scenario['schema']['datatype1']}, {scenario['schema']['column2']} {scenario['schema']['datatype2']}, {scenario['schema']['column3']} {scenario['schema']['datatype3']}, {scenario['schema']['column4']} {scenario['schema']['datatype4']})"
        conn.execute(create_table_query)
        print(
            f"Table '{scenario['table']}' created in database '{scenario['database']}'")

    elif operation == "2":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # List current tables
        print("Current tables in database:")
        table_query = "SELECT name FROM sqlite_master WHERE type='table'"
        tables = conn.execute(table_query).fetchall()
        for table in tables:
            print(table[0])

        # Insert data into table
        for record in scenario['data']:
            keys = ', '.join(record.keys())
            values = ', '.join(['?' for _ in range(len(record))])
            insert_query = f"INSERT INTO {scenario['table']} ({keys}) VALUES ({values})"
            try:
                conn.execute(insert_query, tuple(record.values()))
                print(
                    f"Data inserted into table '{scenario['table']}' in database '{scenario['database']}'")
            except sqlite3.IntegrityError:
                print(
                    f"Record '{record}' not inserted. Unique constraint failed.")
                continue

    elif operation == "3":
        # List all tables in database
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Current tables:")
        for table in tables:
            print(table[0])

    elif operation == "4":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Remove table
        remove_query = f"DROP TABLE {scenario['table']}"
        conn.execute(remove_query)
        print(
            f"Table '{scenario['table']}' removed from database '{scenario['database']}'")

    elif operation == "5":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Clear data from table
        conn.execute(f"DELETE FROM {scenario['table']}")
        print(
            f"Data cleared from table '{scenario['table']}' in database '{scenario['database']}'")

    elif operation == "6":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Retrieve data from table and print it
        select_query = f"SELECT * FROM {scenario['table']}"
        cursor = conn.execute(select_query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print(f"No data found in table '{scenario['table']}'")
        else:
            print(f"Data in table '{scenario['table']}':")
            headers = [description[0] for description in cursor.description]
            for header in headers:
                print(f"{header}\t", end="")
            print()
            for row in rows:
                for value in row:
                    print(f"{value}\t", end="")
                print()

    else:
        print("Invalid operation.")

    # Commit changes and close database connection
    conn.commit()
    conn.close()
