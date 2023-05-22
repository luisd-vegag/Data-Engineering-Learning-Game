from .scenario_001 import module as scenario_001_module
from .scenario_002 import module as scenario_002_module
from .scenario_003 import module as scenario_003_module
from .scenario_004 import module as scenario_004_module
from .scenario_005 import module as scenario_005_module
from .scenario_006 import module as scenario_006_module
from .scenario_007 import module as scenario_007_module
from .scenario_008 import module as scenario_008_module
from .scenario_009 import module as scenario_009_module
from .scenario_010 import module as scenario_010_module
from .scenario_011 import module as scenario_011_module
from .scenario_012 import module as scenario_012_module
from .scenario_013 import module as scenario_013_module
from .scenario_014 import module as scenario_014_module


'''
# TODO:
    - Topic Parallel Computing: 
        Add synchronous processing method to compare overhead
    - Topic Introduction to Data Modeling:    
        Scenario: One-to-Many Relationship
        Description: Task the user to model a one-to-many relationship between two entities.
        Concepts: Relationship, primary key, foreign key, cardinality.

        Scenario: Many-to-Many Relationship
        Description: Task the user to model a many-to-many relationship between two entities.
        Concepts: Relationship, primary key, foreign key, junction table, cardinality.

        Scenario: Normalization
        Description: Task the user to normalize a denormalized dataset into multiple tables.
        Concepts: Normalization, functional dependency, normalization forms (1NF, 2NF, 3NF).

        Scenario: Denormalization
        Description: Task the user to denormalize a set of tables into a single denormalized table.
        Concepts: Denormalization, redundancy, performance optimization.

        Scenario: Entity-Relationship Diagram (ERD) Design
        Description: Task the user to create an ERD for a given set of entities and their relationships.
        Concepts: Entities, relationships, attributes, cardinality, ERD notation.        
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
        "name": "SQL table manipulation",
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
        "topic": "SQL",
        "name": "Single table analysis",
        "description": "Analize a single table using basic SQL.",
        "data": {
            "table": "sales",
            "database": "local/scenario_005/sales.db",
            "schema": [
                {"column": "id", "datatype": "INTEGER PRIMARY KEY"},
                {"column": "date", "datatype": "TEXT"},
                {"column": "item", "datatype": "TEXT"},
                {"column": "quantity", "datatype": "INTEGER"},
                {"column": "price", "datatype": "REAL"}
            ],

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
                "id": "1",
                "description": "Select all sales from January 1, 2022."
            },
            {
                "id": "2",
                "description": "Select the total quantity and price of all sales of Product A."
            },
            {
                "id": "3",
                "description": "Select all sales with a quantity of 10 or more."
            },
            {
                "id": "4",
                "description": "Select all sales of products that have 'Product' in the name."
            },
            {
                "id": "5",
                "description": "Select the total revenue (quantity x price) of all sales."
            }
        ],
        "module": scenario_005_module,
    },
    {
        "id": "006",
        "topic": "Introduction to OOP",
        "name": "OOP Concepts",
        "description": "This scenario provides an introduction to Object-Oriented Programming (OOP) concepts in Python.",
        "questions": [
            {
                "question": "What is the main principle of OOP?",
                "options": [
                    "Encapsulation",
                    "Inheritance",
                    "Polymorphism",
                    "Abstraction"
                ],
                "correct_option": "Encapsulation"
            },
            {
                "question": "What is the purpose of inheritance in OOP?",
                "options": [
                    "To allow a class to acquire the properties and behaviors of another class",
                    "To hide the implementation details of a class",
                    "To create multiple instances of a class",
                    "To perform different actions based on the type of object"
                ],
                "correct_option": "To allow a class to acquire the properties and behaviors of another class"
            },
            {
                "question": "What is the process of creating an object from a class called?",
                "options": [
                    "Instantiation",
                    "Inheritance",
                    "Polymorphism",
                    "Abstraction"
                ],
                "correct_option": "Instantiation"
            },
            {
                "question": "What is the purpose of encapsulation in OOP?",
                "options": [
                    "To allow a class to acquire the properties and behaviors of another class",
                    "To hide the implementation details of a class",
                    "To create multiple instances of a class",
                    "To perform different actions based on the type of object"
                ],
                "correct_option": "To hide the implementation details of a class"
            },
            {
                "question": "What is the term used to describe the ability of an object to take many forms?",
                "options": [
                    "Encapsulation",
                    "Inheritance",
                    "Polymorphism",
                    "Abstraction"
                ],
                "correct_option": "Polymorphism"
            }
        ],
        "module": scenario_006_module
    },
    {
        "id": "007",
        "topic": "Introduction to OOP",
        "name": "Class and Objects",
        "description": "This scenario provides a task where you need to demostrate how to write a Class and an Object.",
        "concept": ["Class", "Object"],
        "module": scenario_007_module
    }, 
    {
        "id": "008",
        "topic": "Introduction to OOP",
        "name": "Encapsulation",
        "description": "This scenario provides a task where you need to demostrate how to use 'Encapsulation' principal.",
        "module": scenario_008_module
    },
    {
        "id": "009",
        "topic": "Introduction to OOP",
        "name": "Inheritance",
        "description": "This scenario provides a task where you need to demonstrate the use of 'Inheritance'.",
        "module": scenario_009_module
    },
    {
        "id": "010",
        "topic": "Introduction to OOP",
        "name": "Polymorphism",
        "description": "This scenario provides a task where you need to demonstrate the use of 'Polymorphism'.",
        "module": scenario_010_module
    }, 
    {
        "id": "011",
        "topic": "Introduction to OOP",
        "name": "Abstraction",
        "description": "This scenario provides a task where you need to demonstrate the use of 'Abstraction'.",
        "module": scenario_011_module
    }, 
    {
        "id": "012",
        "topic": "Introduction to Data Modeling",
        "name": "Data Modeling Concepts",
        "description": "This scenario provides an introduction to Data Modeling concepts.",
        "questions": [
            {
                "question": "What is Data Modeling?",
                "options": [
                    "The process of organizing and analyzing data",
                    "The process of creating a conceptual representation of data",
                    "The process of converting data into information",
                    "The process of implementing a database system"
                ],
                "correct_option": "The process of creating a conceptual representation of data"
            },
            {
                "question": "Which of the following areas does Data Modeling play a crucial role in?",
                "options": [
                    "Database Design",
                    "Data Warehousing",
                    "Business Analysis",
                    "All of the above"
                ],
                "correct_option": "All of the above"
            },
            {
                "question": "What is one of the benefits of Data Modeling?",
                "options": [
                    "Improved data organization",
                    "Enhanced system performance",
                    "Ensured data integrity",
                    "All of the above"
                ],
                "correct_option": "All of the above"
            },
            {
                "question": "True or False: Data Modeling helps in maintaining data consistency and following predefined rules and relationships.",
                "options": [
                    "True",
                    "False"
                ],
                "correct_option": "True"
            },
            {
                "question": "Which of the following areas does Data Modeling NOT impact?",
                "options": [
                    "Data organization",
                    "Scalability",
                    "System security",
                    "Performance optimization"
                ],
                "correct_option": "System security"
            }
        ],
        "module": scenario_012_module
    },
    {
        "id": "013",
        "topic": "Introduction to Data Modeling",
        "name": "Star Schema Design",
        "description": "In this scenario, you will design a star schema for a given dataset.",
        "module": scenario_013_module
    }, 
    {
        "id": "014",
        "topic": "Introduction to Data Modeling",
        "name": "Star Schema Design",
        "description": "In this scenario, you will design a snowflake schema for a given dataset.",
        "module": scenario_014_module
    },         

]

