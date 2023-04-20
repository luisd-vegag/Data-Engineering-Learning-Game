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
    print("7. Update record in table")
    print("8. Add column to table")
    # print("9. Remove column from table")

    operation = input("Please select an operation by entering its number: ")

    # Perform selected operation
    # Create table
    if operation == "1":
        # Check if table already exists and delete it if it does
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'")
        result = cursor.fetchone()
        if result is not None:
            cursor.execute(f"DROP TABLE {scenario['table']}")

        # Prompt user to select SQL command for creating the table
        operation_options = ["CREATE TABLE", "NEW TABLE", "MAKE TABLE"]
        print("Please select an option for creating the table:")
        selected_command = prompt_options(operation_options)

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

    # Insert data into table
    elif operation == "2":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to select SQL command for creating the table
        operation_options = ["INSERT TO",
                             "INSERT INTO", "INSERT IN", "INSERT"]
        print("Please select an option for inserting data the table:")
        selected_command = prompt_options(operation_options)

        # Verify that the selected command is correct
        if selected_command != "INSERT INTO":
            print(
                f"Invalid selection. '{selected_command}' is not a valid command for creating a table.")
            return

        # Insert data into table
        existing_data = False
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
                existing_data = True
                continue
        if existing_data:
            print("Your answer was right but the table already had data")

    # List tables
    elif operation == "3":
        # List all tables in database
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Current tables:")
        for table in tables:
            print(table[0])

    # Remove table
    elif operation == "4":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to select SQL command for creating the table
        operation_options = ["EMPTY",
                             "REMOVE", "DROP", "DOWN", "CLEAN"]
        print("Please select an option for remove/delete the table:")
        selected_command = prompt_options(operation_options)

        # Verify that the selected command is correct
        if selected_command != "DROP":
            print(
                f"Invalid selection. '{selected_command}' is not a valid command for creating a table.")
            return

        # Remove table
        remove_query = f"DROP TABLE {scenario['table']}"
        conn.execute(remove_query)
        print(
            f"Table '{scenario['table']}' removed from database '{scenario['database']}'")

    # Clear all data in table
    elif operation == "5":

        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to select SQL command for creating the table
        operation_options = ["DELETE", "DROP", "FULL DROP", "REMOVE"]
        print("Please select an option for clear the table:")
        selected_command = prompt_options(operation_options)

        # Verify that the selected command is correct
        if selected_command != "DELETE":
            print(
                f"Invalid selection. '{selected_command}' is not a valid command for creating a table.")
            return

        # Clear data from table
        conn.execute(f"DELETE FROM {scenario['table']}")
        print(
            f"Data cleared from table '{scenario['table']}' in database '{scenario['database']}'")

    # SHOW DATA
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

    # Update record in table
    elif operation == "7":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to enter ID of record to update
        record_id = input("Enter the ID of the record to update: ")

        # Check if record with given ID exists
        query = f"SELECT * FROM {scenario['table']} WHERE id=?"
        result = conn.execute(query, (record_id,)).fetchone()
        if not result:
            print(
                f"Record with ID '{record_id}' not found in table '{scenario['table']}'")
            return

        # Prompt user to enter new value for record
        column = input("Enter the column to update: ")
        # Check if column name exists
        query = f"PRAGMA table_info({scenario['table']})"
        columns = [row[1] for row in conn.execute(query)]
        if column not in columns:
            print(
                f"Column '{column}' does not exist in table '{scenario['table']}'")
            return
        value = input("Enter the new value: ")

        # Update record
        update_query = f"UPDATE {scenario['table']} SET {column}=? WHERE id=?"
        conn.execute(update_query, (value, record_id))
        print(
            f"Record with ID '{record_id}' updated in table '{scenario['table']}'")
    # Add column to table
    elif operation == "8":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to enter column name and datatype
        column_name = input("Enter column name: ")
        column_datatype = input("Enter column datatype: ")

        # Add column to table
        add_column_query = f"ALTER TABLE {scenario['table']} ADD COLUMN {column_name} {column_datatype}"
        conn.execute(add_column_query)
        print(f"Column '{column_name}' added to table '{scenario['table']}'")
    else:
        print("Invalid operation.")
    """
    # Remove column from table
    elif operation == "9":
        # Check if table exists
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{scenario['table']}'"
        result = conn.execute(query).fetchone()
        if not result:
            print(
                f"Table '{scenario['table']}' does not exist in database '{scenario['database']}'")
            return

        # Prompt user to select column to remove
        column_to_remove = input("Enter the name of the column to remove: ")

        # Check if column exists in table
        query = f"SELECT {column_to_remove} FROM {scenario['table']}"
        try:
            conn.execute(query)
        except sqlite3.OperationalError:
            print(
                f"Column '{column_to_remove}' does not exist in table '{scenario['table']}'")
            return

        # Remove column from table
        alter_query = f"ALTER TABLE {scenario['table']} DROP COLUMN {column_to_remove}"
        print(alter_query)
        conn.execute(alter_query)
        print(
            f"Column '{column_to_remove}' removed from table '{scenario['table']}'")
    
    """

    # Commit changes and close database connection
    conn.commit()
    conn.close()


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
