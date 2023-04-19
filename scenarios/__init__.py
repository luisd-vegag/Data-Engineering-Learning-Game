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
        "name": "Generate 4 files with 10k random records",
        "description": "Demonstrate the performance by processing method for generating data using a synthetic example.",
        "functions": ["generate_users_data", "generate_sales_data", "generate_product_date", "generate_customer_data"],
        "num_rows": 10000,
        "output_dir_path": "./local/scenario_002/data_10k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_002_module
    },
    {
        "id": "003",
        "topic": "Parallel computing",
        "name": "Read CSV files",
        "description": "Demonstrate the performance by processing method to read multiple csv files with 10K rows each.",
        "input_dir_path": "./local/scenario_003/data_10k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool", "dask", "pyspark"],
        "module": scenario_003_module
    },
    {
        "id": "004",
        "topic": "SQL",
        "name": "SQL Table manipulation",
        "description": "Demonstrate how to interact with SQLite database with the table 'students'.",
        "database": "./local/scenario_004/data.db",
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
    {
        "id": "005",
        "name": "Single Table Query Practice",
        "description": "Practice common SQL single table query operations.",
        "data": {
            "table": "sales",
            "database": "local/scenario_005/sales.db",
            "schema": {
                "column1": "id",
                "datatype1": "INTEGER PRIMARY KEY",
                "column2": "date",
                "datatype2": "TEXT",
                "column3": "item",
                "datatype3": "TEXT",
                "column4": "quantity",
                "datatype4": "INTEGER",
                "column5": "price",
                "datatype5": "REAL"
            },
            "data": [
                {"id": 1, "date": "2022-01-01", "item": "Product A",
                    "quantity": 10, "price": 15.99},
                {"id": 2, "date": "2022-01-01", "item": "Product B",
                    "quantity": 5, "price": 9.99},
                {"id": 3, "date": "2022-01-02", "item": "Product C",
                    "quantity": 7, "price": 12.50},
                {"id": 4, "date": "2022-01-02", "item": "Product A",
                    "quantity": 12, "price": 15.99},
                {"id": 5, "date": "2022-01-03", "item": "Product D",
                    "quantity": 3, "price": 5.99},
                {"id": 6, "date": "2022-01-03", "item": "Product B",
                    "quantity": 8, "price": 9.99},
                {"id": 7, "date": "2022-01-03", "item": "Product A",
                    "quantity": 4, "price": 15.99},
                {"id": 8, "date": "2022-01-04", "item": "Product E",
                    "quantity": 6, "price": 7.99},
                {"id": 9, "date": "2022-01-05", "item": "Product A",
                    "quantity": 2, "price": 15.99},
                {"id": 10, "date": "2022-01-05", "item": "Product B",
                    "quantity": 9, "price": 9.99}
            ]
        },
        "objectives": [
            {
                "id": "01",
                "description": "Select all sales from January 1, 2022."
            },
            {
                "id": "02",
                "description": "Select the total quantity and price of all sales of Product A."
            },
            {
                "id": "03",
                "description": "Select all sales with a quantity of 10 or more."
            },
            {
                "id": "04",
                "description": "Select all sales of products that have 'Product' in the name."
            },
            {
                "id": "05",
                "description": "Select the total revenue (quantity x price) of all sales."
            }
        ],
        "module": scenario_005_module,
    }
]
