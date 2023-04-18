from .scenario_001 import module as scenario_001_module
from .scenario_002 import module as scenario_002_module
from .scenario_003 import module as scenario_003_module
from .scenario_004 import module as scenario_004_module

'''
# TODO:
    - Add synchronous processing method to compare overhead
'''

scenarios = [
    {
        "id": "001",
        "topic": "Parallel computing",
        "name": "Calculate big numbers",
        "description": "Demonstrate the performance by processing method for a CPU-bound operation using a synthetic example.",
        "numbers": [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_001_module
    },
    {
        "id": "002",
        "topic": "Parallel computing",
        "name": "Generate 4 files with 100k random records",
        "description": "Demonstrate the performance by processing method for generating data using a synthetic example.",
        "functions": ["generate_users_data", "generate_sales_data", "generate_product_date", "generate_customer_data"],
        "num_rows": 100000,
        "output_dir_path": "./system/data_100k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_002_module
    },
    {
        "id": "003",
        "topic": "Parallel computing",
        "name": "Read CSV files",
        "description": "Demonstrate the performance by processing method to read multiple csv files.",
        "input_dir_path": "./system/data_100k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool", "dask", "pyspark"],
        "module": scenario_003_module
    },
    {
        "id": "004",
        "topic": "SQL",
        "name": "Creating a table and inserting data",
        "description": "Demonstrate how to create a table in a SQLite database and insert data into it.",
        "database": "./system/scenario_004/data.db",
        "table": "students",
        "schema": {"column1": "id",
                   "datatype1": "INTEGER PRIMARY KEY",
                   "column2": "name",
                   "datatype2": "TEXT",
                   "column3": "age",
                   "datatype3": "INTEGER",
                   "column4": "gender",
                   "datatype4": "TEXT"},
        "data": [
            {"id": 1, "name": "John", "age": 20, "gender": "Male"},
            {"id": 2, "name": "Sarah", "age": 22, "gender": "Female"},
            {"id": 3, "name": "Bob", "age": 19, "gender": "Male"},
            {"id": 4, "name": "Linda", "age": 21, "gender": "Female"}
        ],
        "module": scenario_004_module
    },
]
