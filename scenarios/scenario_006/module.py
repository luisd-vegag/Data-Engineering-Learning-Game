from algorithms.quiz_user import quiz_user
def run_scenario(scenario):

    print("Welcome to the Introduction to OOP scenario!")
    print("In this scenario, we will explore the fundamental concepts of Object-Oriented Programming (OOP) in Python.")
    print("OOP is a programming paradigm that allows us to structure code based on the concept of objects.")

    print("\nOOP is based on four main principles:")

    print("- Encapsulation: Encapsulation allows us to bundle data and methods together into objects, hiding the internal implementation details.")
    print("- Inheritance: Inheritance enables us to create new classes based on existing classes, inheriting their attributes and behaviors.")
    print("- Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass, providing a flexible and interchangeable behavior.")
    print("- Abstraction: Abstraction focuses on the essential features of an object and hides the unnecessary details, allowing us to work at a higher level of understanding.")

    print("\nOOP offers numerous benefits, including:")

    print("- Modularity: OOP promotes modular code organization, making it easier to understand, maintain, and reuse code.")
    print("- Code Reusability: Inheritance and polymorphism enable code reuse, saving development time and effort.")
    print("- Data Security: Encapsulation allows us to control the access to data, protecting it from unauthorized modifications.")
    print("- Code Flexibility: OOP allows for easy modification and extension of code, making it adaptable to changing requirements.")
    print("- Collaborative Development: OOP facilitates collaborative development by allowing different developers to work on different parts of a program simultaneously.")

    print("Now, let's test your understanding of OOP concepts with a quiz.")

    # Prompt user to start quiz
    input("Press Enter to start quiz...")

    quiz_user(scenario)


