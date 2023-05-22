def run_scenario(scenario):
    print("Welcome to the Star Schema Design scenario!")
    print("In this scenario, you will design a star schema for a given dataset.")
    print("A star schema is a type of data modeling schema commonly used in data warehousing.")
    print("It consists of a fact table surrounded by dimension tables, forming a star-like shape.")
    print("The fact table contains the measures or numerical data, while the dimension tables provide descriptive information about the measures.")
    print("Each dimension table has a primary key that uniquely identifies its records. The fact table references these primary keys using foreign keys, establishing relationships between the tables.\n")

    print("\nYour task is to complete the star schema for this dataset.")

    table_schemas = {
        "Retail Sales": {
            "Fact Table": "Sales",
            "Measures": ["Revenue", "Quantity", "Discount"],
            "Dimension Tables": {
                "Product": ["Product ID", "Product Name", "Category", "Brand"],
                "Customer": ["Customer ID", "First Name", "Last Name", "Email"],
                "Store": ["Store ID", "Store Name", "Location"],
                "Time": ["Time ID", "Date", "Month", "Year"]
            }
        },
        "Hospital Records": {
            "Fact Table": "Patient Records",
            "Measures": ["Visit Duration", "Treatment Cost", "Medication Cost"],
            "Dimension Tables": {
                "Patient": ["Patient ID", "First Name", "Last Name", "Age", "Sex"],
                "Doctor": ["Doctor ID", "First Name", "Last Name", "Specialization"],
                "Treatment": ["Treatment ID", "Treatment Name"],
                "Time": ["Time ID", "Date", "Month", "Year"]
            }
        },
        "E-commerce Orders": {
            "Fact Table": "Orders",
            "Measures": ["Total Amount", "Number of Items", "Shipping Cost"],
            "Dimension Tables": {
                "Product": ["Product ID", "Product Name", "Category", "Brand"],
                "Customer": ["Customer ID", "First Name", "Last Name", "Email"],
                "Shipping Address": ["Address ID", "Street", "City", "State", "Country"],
                "Time": ["Time ID", "Date", "Month", "Year"]
            }
        }
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

    print(f"\nCompleting Star Schema: {selected_schema}\n")
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

    print("\nNow, let's complete the star schema by adding primary keys and relations.")

    star_schema = {
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
                star_schema["Fact Table"]["Primary Key"] = primary_key
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
                    star_schema["Dimension Tables"][dim_table] = {
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
                star_schema["Fact Table"]["Foreign Keys"][dim_table] = foreign_key
            else:
                print("Invalid input. Please provide a foreign key.")
        except KeyboardInterrupt:
            print("\n\nExiting the scenario...")
            return

    print("\nStar Schema Design Completed!")
    print("\nHere is the completed star schema:")

    print("\nFact Table:")
    print(f"  Table Name: {star_schema['Fact Table']['Table Name']}")
    print(f"  Primary Key: {star_schema['Fact Table']['Primary Key']}")
    for dim_table, dim_info in star_schema["Dimension Tables"].items():
        if dim_table in star_schema["Fact Table"]["Foreign Keys"]:
            print(f"    Foreign Key: {star_schema['Fact Table']['Foreign Keys'][dim_table]}")

    print("  Measures:")
    for measure in star_schema["Fact Table"]["Measures"]:
        print(f"    - {measure}")
    print("Dimension Tables:")
    
    for dim_table, dim_info in star_schema["Dimension Tables"].items():
        print(f"  - {dim_table}")
        print(f"    Primary Key: {dim_info['Primary Key']}")
        print(f"    Columns: {dim_info['Columns']}")

    print("\nVisualization of the Star Schema:")
    print("Fact Table in the center:")
    print(f"  [ {star_schema['Fact Table']['Table Name']} ]")
    print("Surrounded by Dimension Tables:")
    for dim_table in star_schema["Dimension Tables"].keys():
        print(f"   --> [ {dim_table} ]")
    print("Each arrow ' --> ' represents a foreign key relationship from the dimension table to the fact table.")

    print("\nScenario completed.")
    print("Now, let's test your understanding of the concepts.")

    print("\nQuiz:")
    print("What is a star schema?")
    print("a) A data modeling schema with a single table")
    print("b) A data modeling schema with a central fact table and multiple dimension tables")
    print("c) A data modeling schema with multiple tables and complex relationships")
    print("d) A data modeling schema with nested tables")

    answer = input("Enter your answer (a, b, c, or d): ")

    if answer.lower() == "b":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'b) A data modeling schema with a central fact table and multiple dimension tables.'")

    print("\nA star schema is a data modeling schema with a central fact table and multiple dimension tables.")
    print("The fact table contains the measures or numerical data, while the dimension tables provide descriptive information about the measures.")
    print("This schema design simplifies data analysis and reporting as it allows for easy navigation and aggregation of data.")
    print("It is widely used in data warehousing and business intelligence applications.")
