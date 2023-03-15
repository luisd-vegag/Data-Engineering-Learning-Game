from .scenario_001 import module as scenario_001_module
from .scenario_002 import module as scenario_002_module
from .scenario_003 import module as scenario_003_module
import os

'''
# TODO:
    - Add synchronous processing method to compare overhead
'''

scenarios = [
    {
        "id": "001",
        "name": "Calculate big numbers",
        "description": "Demostrate the performance by processing method for a CPU-bound operation using a synthetic example.",
        "numbers": [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_001_module
    },
    {
        "id": "002",
        "name": "Generate 4 files with 100k random records",
        "description": "Demostrate the performance by processing method for a CPU-bound operation using a synthetic example.",
        "functions": ["generate_users_data", "generate_sales_data", "generate_product_date", "generate_customer_data"],
        "num_rows": 100000,
        "output_dir_path": "./system/data_100k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_002_module
    },
    {
        "id": "003",
        "name": "Read CSV files",
        "description": "Demostrate the performance by processing method to read multiple csv files.",
        "input_dir_path": "./system/data_100k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool", "dask", "pyspark"],
        "module": scenario_003_module
    },
]
