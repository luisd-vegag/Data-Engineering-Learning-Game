def run_scenario(scenario):
    print("Welcome to the Snowflake Schema Design scenario!")
    print("In this scenario, you will design a snowflake schema for a given dataset.")
    print("A snowflake schema is an extension of the star schema, where dimension tables are further normalized into multiple tables.")
    print("This normalization reduces redundancy but increases complexity in joining tables.")
    print("The fact table and dimension tables in a snowflake schema are connected through primary key and foreign key relationships.")

    print("\nYour task is to complete the snowflake schema for this dataset.")

    # Note that some dimension tables have been broken down further to depict the snowflake schema
    table_schemas = {
        "Retail Sales": {
            "Fact Table": "Sales",
            "Measures": ["Revenue", "Quantity", "Discount"],
            "Dimension Tables": {
                "Product": ["Product ID", "Product Name", "Category", "Brand"],
                "Category": ["Category ID", "Category Name", "Category Description"],
                "Brand": ["Brand ID", "Brand Name"],
                "Customer": ["Customer ID", "First Name", "Last Name", "Email"],
                "Store": ["Store ID", "Store Name", "Location"],
                "Location": ["Location ID", "City", "State", "Country"],
                "Time": ["Time ID", "Date", "Month", "Year"]
            }
        },
    }
    print("\nAvailable Table Schemas:")
    for i, schema_name in enumerate(table_schemas.keys(), start=1):
        schema = table_schemas[schema_name]
        fact_table = schema["Fact Table"]
        measures = schema["Measures"]
        dimension_tables = schema["Dimension Tables"]
        print(f"{i}. {schema_name}")
        print("Fact Table:")
        print(f"  Fact Table Name: {fact_table}")
        print("  Measures:")
        for measure in measures:
            print(f"    - {measure}")
        print("Dimension Tables:")
        for dim_table, columns in dimension_tables.items():
            print(f"  - {dim_table}")
            for column in columns:
                print(f"    - {column}")
        print()

    while True:
        try:
            schema_choice = int(input("Enter the number corresponding to the table schema you want to complete: "))
            if schema_choice in range(1, len(table_schemas) + 1):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

    selected_schema = list(table_schemas.keys())[schema_choice - 1]
    schema = table_schemas[selected_schema]

    fact_table = schema["Fact Table"]
    measures = schema["Measures"]
    dimension_tables = schema["Dimension Tables"]

    print(f"\nCompleting Snowflake Schema: {selected_schema}\n")
    print("Fact Table:")
    print(f"  Fact Table Name: {fact_table}")
    print("  Measures:")
    for measure in measures:
        print(f"    - {measure}")
    print("Dimension Tables:")
    for dim_table, columns in dimension_tables.items():
        print(f"  - {dim_table}")
        for column in columns:
            print(f"    - {column}")

    print("\nNow, let's complete the snowflake schema by adding primary keys and relations.")

    snowflake_schema = {
        "Fact Table": {
            "Table Name": fact_table,
            "Measures": measures,
            "Primary Key": None,
            "Foreign Keys": {}
        },
        "Dimension Tables": {}
    }

    print("\nProvide the primary key for each table:")
    while True:
        try:
            primary_key = input(f"Primary Key for {fact_table}: ")
            if primary_key:
                snowflake_schema["Fact Table"]["Primary Key"] = primary_key
                break
            else:
                print("Invalid input. Please provide a primary key.")
        except KeyboardInterrupt:
            print("\n\nExiting the scenario...")
            return

    for dim_table in dimension_tables:
        while True:
            try:
                primary_key = input(f"Primary Key for {dim_table}: ")
                if primary_key:
                    snowflake_schema["Dimension Tables"][dim_table] = {
                        "Primary Key": primary_key,
                        "Columns": dimension_tables[dim_table]
                    }
                    break
                else:
                    print("Invalid input. Please provide a primary key.")
            except KeyboardInterrupt:
                print("\n\nExiting the scenario...")
                return

    print("\nProvide the relations between dimension tables and the fact table:")

    for dim_table in dimension_tables:
        try:
            foreign_key = input(f"Foreign Key from {dim_table} to {fact_table}: ")
            if foreign_key:
                snowflake_schema["Fact Table"]["Foreign Keys"][dim_table] = foreign_key
            else:
                print("Invalid input. Please provide a foreign key.")
        except KeyboardInterrupt:
            print("\n\nExiting the scenario...")
            return

    print("\nSnowflake Schema Design Completed!")
    print("\nHere is the completed snowflake schema:")

    print("\nFact Table:")
    print(f"  Table Name: {snowflake_schema['Fact Table']['Table Name']}")
    print(f"  Primary Key: {snowflake_schema['Fact Table']['Primary Key']}")
    for dim_table, dim_info in snowflake_schema["Dimension Tables"].items():
        if dim_table in snowflake_schema["Fact Table"]["Foreign Keys"]:
            print(f"    Foreign Key: {snowflake_schema['Fact Table']['Foreign Keys'][dim_table]}")

    print("  Measures:")
    for measure in snowflake_schema["Fact Table"]["Measures"]:
        print(f"    - {measure}")
    print("Dimension Tables:")

    for dim_table, dim_info in snowflake_schema["Dimension Tables"].items():
        print(f"  - {dim_table}")
        print(f"    Primary Key: {dim_info['Primary Key']}")
        print(f"    Columns: {dim_info['Columns']}")

    print("\nVisualization of the Snowflake Schema:")
    print("Fact Table in the center:")
    print(f"  [ {snowflake_schema['Fact Table']['Table Name']} ]")
    print("Connected to Dimension Tables:")
    for dim_table in snowflake_schema["Dimension Tables"].keys():
        print(f"   --> [ {dim_table} ]")
    print("Each arrow ' --> ' represents a foreign key relationship from the dimension table to the fact table.")

    print("\nScenario completed.")
    print("Now, let's test your understanding of the concepts.")

    print("\nQuiz:")
    print("What is a snowflake schema?")
    print("a) A data modeling schema with a single table")
    print("b) A data modeling schema with a central fact table and multiple dimension tables")
    print("c) A data modeling schema where dimension tables are normalized into multiple tables")
    print("d) A data modeling schema with nested tables")

    answer = input("Enter your answer (a, b, c, or d): ")

    if answer.lower() == "c":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'c) A data modeling schema where dimension tables are normalized into multiple tables.'")

    print("\nA snowflake schema is an extension of the star schema, where dimension tables are further normalized into multiple tables.")
    print("This normalization reduces redundancy but increases complexity in joining tables.")
    print("The fact table and dimension tables in a snowflake schema are connected through primary key and foreign key relationships.")
    print("Snowflake schemas are commonly used in data warehousing and analytical applications.")