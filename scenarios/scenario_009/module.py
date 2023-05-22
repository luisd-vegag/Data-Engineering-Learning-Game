import os
import tempfile
import subprocess

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Driving the {self.brand} vehicle!")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def honk(self):
        print(f"The {self.brand} {self.model} is honking!")

def run_scenario(scenario):
    print("Welcome to the Introduction to OOP scenario!")
    print("This scenario provides a task where you need to demonstrate how to use 'Inheritance'.")
    print("")
    print("Inheritance is a fundamental concept in object-oriented programming that allows creating a new class (derived class) from an existing class (base class).")
    print("The derived class inherits the attributes and methods from the base class, and it can add its own attributes and methods or override the ones inherited.")
    print("In this scenario, you will create a derived class 'Car' that inherits from the base class 'Vehicle'.")

    # Example 1
    print("\nExample 1:")
    print("class Vehicle:")
    print("    def __init__(self, brand):")
    print("        self.brand = brand")
    print("    def drive(self):")
    print("        print(f\"Driving the {self.brand} vehicle!\")")
    print("")
    print("Explanation:")
    print("In this example, we define a base class 'Vehicle' with an instance variable 'brand' and a method 'drive'.")
    print("The 'Car' class will inherit these attributes and methods from the 'Vehicle' class.")

    # Example 2
    print("\nExample 2:")
    print("class Car(Vehicle):")
    print("    def __init__(self, brand, model):")
    print("        super().__init__(brand)")
    print("        self.model = model")
    print("    def honk(self):")
    print("        print(f\"The {self.brand} {self.model} is honking!\")")
    print("")
    print("Explanation:")
    print("In this example, we create a derived class 'Car' that inherits from the 'Vehicle' class.")
    print("The 'Car' class adds its own attribute 'model' and method 'honk', in addition to inheriting the 'brand' attribute and 'drive' method from the 'Vehicle' class.")

    # Prompt user to start coding
    input("Press Enter to start coding...")

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp_file:
        file_path = tmp_file.name

        # Write task instructions to the file
        task_instructions = """\
        # Task Instructions:
        # Create a class named 'Car' that inherits from the 'Vehicle' class.
        # The 'Car' class should have a constructor method '__init__' that takes 'brand' and 'model' parameters.
        # The constructor should call the base class constructor using 'super()' and assign the 'model' parameter to an instance variable 'self.model'.
        # The 'Car' class should also have a method named 'honk' that prints a honking message using the 'brand' and 'model' instance variables.

        # ** Be aware that one 'tab' is equal to four spaces in most configurations. **
        # Your code:
        """
        tmp_file.write(task_instructions.encode("utf-8"))
        tmp_file.close()

    # Open the file using nano
    subprocess.call(["nano", file_path])

    # Read the contents of the file
    with open(file_path) as f:
        code = f.read()


    # Evaluate the code in a try-except block
    try:
        exec(code)
    except Exception as e:
        print("Oops! An error occurred while executing the code.")
        print("Please ensure that the code is valid and follows the given structure.")
        print(f"Error details: {str(e)}")
        return

    # Check if the class and object are created correctly
    if "Car" not in locals() or not callable(Car):
        print("Oops! The class 'Car' is not defined correctly.")
        return

    obj = Car("Toyota", "Camry")
    if not hasattr(obj, "honk") or not callable(obj.honk):
        print("Oops! The 'honk' method is missing or not defined correctly.")
        return

    # Create object and test inheritance
    print("Now let's create an object of the Car class and test the inheritance.")
    obj.drive()
    obj.honk()

    print("Scenario completed.")
    print("Now, let's test your understanding of the concepts.")

    # Quiz
    print("\nQuiz:")
    print("What is the purpose of inheritance?")
    print("a) To create an instance of an object.")
    print("b) To define the behavior and attributes of an object.")
    print("c) To perform operations on an object.")
    print("d) To reuse and extend the attributes and methods of an existing class.")

    # Get user's answer
    answer = input("Enter your answer (a, b, c, or d): ")

    # Check the answer
    if answer.lower() == "d":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'd) To reuse and extend the attributes and methods of an existing class.'")

    # Explanation of inheritance
    print("\nInheritance is a powerful mechanism in object-oriented programming that promotes code reuse and extensibility.")
    print("By inheriting from a base class, derived classes can reuse the attributes and methods of the base class.")
    print("Additionally, derived classes can add their own attributes and methods or override the ones inherited, allowing for customization and specialization.")
    print("This promotes code organization, modularity, and maintainability.")
