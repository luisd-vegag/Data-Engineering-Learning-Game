from .scenario_001 import module as scenario_001_module
from .scenario_002 import module as scenario_002_module
import os


scenarios = [
    {
        "id": "001",
        "name": "Read CSV files",
        "description": "Demostrate the performance by processing method to read multiple csv files.",
        "input_dir_path": "./system/data_100k/",
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool", "dask", "pyspark"],
        "module": scenario_001_module
    },
    {
        "id": "002",
        "name": "Run CPU-bound operation",
        "description": "Demostrate the performance by processing method for a CPU-bound operation using a synthetic example.",
        "numbers": [1000000, 2000000, 3000000, 4000000, 5000000],
        "methods": ["multiprocessing", "threading", "concurrent_futures_process_pool", "concurrent_futures_thread_pool"],
        "module": scenario_002_module
    }
]
