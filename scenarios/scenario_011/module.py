import os
import tempfile
import subprocess
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

class Bike(Vehicle):
    def start(self):
        print("Starting the bike")

    def stop(self):
        print("Stopping the bike")

def run_scenario(scenario):
    print("Welcome to the Abstraction scenario!")
    print("This scenario provides a task where you need to demonstrate the use of 'Abstraction'.")
    print("")
    print("Abstraction is a key principle in object-oriented programming that involves hiding the internal details of an object and showing only the essential features and behavior.")
    print("In this scenario, you will create an abstract class 'Vehicle' with abstract methods 'start' and 'stop'.")
    print("Two subclasses 'Car' and 'Bike' will inherit from 'Vehicle' and provide specific implementations of the abstract methods.")

    # Example 1
    print("\nExample 1:")
    print("from abc import ABC, abstractmethod")
    print("")
    print("class Vehicle(ABC):")
    print("    @abstractmethod")
    print("    def start(self):")
    print("        pass")
    print("    @abstractmethod")
    print("    def stop(self):")
    print("        pass")
    print("")
    print("Explanation:")
    print("In this example, we define an abstract class 'Vehicle' using the ABC (Abstract Base Class) module.")
    print("The class contains abstract methods 'start' and 'stop' that have no implementation.")
    print("By defining these methods as abstract, we enforce their implementation in the subclasses.")

    # Example 2
    print("\nExample 2:")
    print("class Car(Vehicle):")
    print("    def start(self):")
    print("        print('Starting the car')")
    print("    def stop(self):")
    print("        print('Stopping the car')")
    print("")
    print("Explanation:")
    print("In this example, we create a subclass 'Car' that inherits from the 'Vehicle' class.")
    print("The 'Car' class provides concrete implementations of the 'start' and 'stop' methods specific to a car.")

    # Example 3
    print("\nExample 3:")
    print("class Bike(Vehicle):")
    print("    def start(self):")
    print("        print('Starting the bike')")
    print("    def stop(self):")
    print("        print('Stopping the bike')")
    print("")
    print("Explanation:")
    print("In this example, we create another subclass 'Bike' that also inherits from the 'Vehicle' class.")
    print("The 'Bike' class provides its own implementations of the 'start' and 'stop' methods for a bike.")

    # Prompt user to start coding
    input("Press Enter to start coding...")

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp_file:
        file_path = tmp_file.name

        # Write task instructions to the file
        task_instructions = """\
        # Task Instructions:
        # Create an abstract class named 'Vehicle' with abstract methods 'start' and 'stop'.
        # Then create two subclasses 'Car' and 'Bike' that inherit from 'Vehicle'.
        # Override the 'start' and 'stop' methods in each subclass with specific implementations.

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

    # Check if the classes and objects are created correctly
    if "Vehicle" not in locals() or not isinstance(Vehicle, ABC):
        print("Oops! The class 'Vehicle' is not defined correctly or does not inherit from ABC.")
        return

    if "Car" not in locals() or not issubclass(Car, Vehicle):
        print("Oops! The class 'Car' is not defined correctly or does not inherit from 'Vehicle'.")
        return

    if "Bike" not in locals() or not issubclass(Bike, Vehicle):
        print("Oops! The class 'Bike' is not defined correctly or does not inherit from 'Vehicle'.")
        return

    car = Car()
    bike = Bike()

    if not hasattr(car, "start") or not callable(car.start):
        print("Oops! The 'start' method is missing or not defined correctly in the 'Car' class.")
        return

    if not hasattr(car, "stop") or not callable(car.stop):
        print("Oops! The 'stop' method is missing or not defined correctly in the 'Car' class.")
        return

    if not hasattr(bike, "start") or not callable(bike.start):
        print("Oops! The 'start' method is missing or not defined correctly in the 'Bike' class.")
        return

    if not hasattr(bike, "stop") or not callable(bike.stop):
        print("Oops! The 'stop' method is missing or not defined correctly in the 'Bike' class.")
        return

    # Start and stop the car and bike
    print("\nNow let's create objects of the 'Car' and 'Bike' classes and perform the 'start' and 'stop' operations.")
    car.start()
    car.stop()
    bike.start()
    bike.stop()

    print("Scenario completed.")
    print("Now, let's test your understanding of the concepts.")

    # Quiz
    print("\nQuiz:")
    print("What is 'Abstraction' in object-oriented programming?")
    print("a) The ability of objects of different classes to respond to the same method name.")
    print("b) The process of creating objects from classes.")
    print("c) The process of deriving new classes from existing classes.")
    print("d) The process of hiding internal details and showing only the essential features of an object.")

    # Get user's answer
    answer = input("Enter your answer (a, b, c, or d): ")

    # Check the answer
    if answer.lower() == "d":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'd) The process of hiding internal details and showing only the essential features of an object.'")

    # Explanation of abstraction
    print("\nAbstraction is demonstrated in this scenario through the use of an abstract class 'Vehicle'.")
    print("The abstract class defines the common interface with abstract methods 'start' and 'stop'.")
    print("The subclasses 'Car' and 'Bike' inherit from the 'Vehicle' class and provide concrete implementations of the abstract methods.")
    print("By using abstraction, we can define a common behavior in the abstract class and enforce its implementation in the subclasses.")
    print("This allows us to hide the internal details of each specific vehicle type and work with them at a higher level of abstraction.")

