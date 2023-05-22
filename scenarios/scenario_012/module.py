from algorithms.quiz_user import quiz_user

def run_scenario(scenario):
    print("Welcome to the Introduction to Data Modeling scenario!")
    print("In this scenario, we will explore the fundamental concepts of Data Modeling.")
    print("Data Modeling is the process of creating a conceptual representation of data to support the needs of an application or system.")
    print("It involves identifying entities, their attributes, and the relationships between entities.")

    print("\nData Modeling plays a crucial role in various areas, including:")

    print("- Database Design: Data models are used to design and create efficient and well-structured databases.")
    print("- Data Warehousing: Data models help organize and integrate data from different sources into a data warehouse.")
    print("- Business Analysis: Data models facilitate the understanding of business requirements and the translation of those requirements into technical specifications.")
    print("- System Development: Data models provide a blueprint for developers to design and build software systems that interact with data.")

    print("\nData Modeling is important for the following reasons:")

    print("- Data Organization: It helps organize data into meaningful structures, making it easier to store, retrieve, and maintain.")
    print("- Data Consistency: It ensures that data is consistent and follows predefined rules and relationships.")
    print("- Data Integrity: It helps maintain the accuracy, completeness, and reliability of data.")
    print("- Scalability: Well-designed data models can accommodate changes and future growth in data volume and complexity.")
    print("- Performance Optimization: Data models enable efficient data retrieval and processing, leading to improved system performance.")

    print("Let's test your understanding of Data Modeling with a quiz.")

    # Prompt user to start quiz
    input("Press Enter to start quiz...")

    quiz_user(scenario)
