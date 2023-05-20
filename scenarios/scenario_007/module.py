import os
import tempfile
import subprocess

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")



def run_scenario(scenario):
    print("Welcome to the Generic OOP Concepts scenario!")
    print("Please demonstrate your knowledge of creating a 'Class' and an 'Object'.")
    print("")
    print("Write code to create a class named 'MyClass'.")
    # Prompt user to start coding
    input("Press Enter to start coding...")

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp_file:
        file_path = tmp_file.name

        # Write task instructions to the file
        task_instructions = """\
        # Task Instructions:
        # The class should have a constructor method '__init__' that takes a 'name' parameter.
        # The constructor should assign the 'name' parameter to an instance variable 'self.name'.
        # The class should also have a method named 'greet' that prints a greeting message using the 'name' instance variable.

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
    if "MyClass" not in locals() or not callable(MyClass):
        print("Oops! The class 'MyClass' is not defined correctly.")
        return

    obj = MyClass("World")
    if not hasattr(obj, "greet") or not callable(obj.greet):
        print("Oops! The 'greet' method is missing or not defined correctly.")
        return

    # Create object and greet the user
    print("Now let's create an object of the MyClass class and greet the user.")
    obj.greet()

    print("Scenario completed.")
    print("Now, let's test your understanding of the concepts.")

    # Quiz
    print("\nQuiz:")
    print("What is the purpose of a class?")
    print("a) To create an instance of an object.")
    print("b) To define the behavior and attributes of an object.")
    print("c) To perform operations on an object.")
    print("d) To represent a single entity in a program.")

    # Get user's answer
    answer = input("Enter your answer (a, b, c, or d): ")

    # Check the answer
    if answer.lower() == "b":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'b) To define the behavior and attributes of an object.'")
