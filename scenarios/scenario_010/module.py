import os
import tempfile
import subprocess

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def run_scenario(scenario):
    print("Welcome to the Polymorphism scenario!")
    print("This scenario provides a task where you need to demonstrate the use of 'Polymorphism'.")
    print("")
    print("Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass.")
    print("In this scenario, you will create a superclass 'Shape' with an abstract method 'area', and two subclasses 'Rectangle' and 'Circle' that inherit from 'Shape'.")
    print("Each subclass will override the 'area' method to calculate and return the area of the shape.")

    # Example 1
    print("\nExample 1:")
    print("class Shape:")
    print("    def area(self):")
    print("        pass")
    print("")
    print("Explanation:")
    print("In this example, we define a superclass 'Shape' with an abstract method 'area' that does nothing.")
    print("The 'Rectangle' and 'Circle' classes will inherit from this superclass and provide their own implementations of the 'area' method.")

    # Example 2
    print("\nExample 2:")
    print("class Rectangle(Shape):")
    print("    def __init__(self, length, width):")
    print("        self.length = length")
    print("        self.width = width")
    print("    def area(self):")
    print("        return self.length * self.width")
    print("")
    print("Explanation:")
    print("In this example, we create a subclass 'Rectangle' that inherits from the 'Shape' superclass.")
    print("The 'Rectangle' class overrides the 'area' method to calculate and return the area of a rectangle based on its length and width.")

    # Example 3
    print("\nExample 3:")
    print("class Circle(Shape):")
    print("    def __init__(self, radius):")
    print("        self.radius = radius")
    print("    def area(self):")
    print("        return 3.14 * self.radius * self.radius")
    print("")
    print("Explanation:")
    print("In this example, we create another subclass 'Circle' that also inherits from the 'Shape' superclass.")
    print("The 'Circle' class overrides the 'area' method to calculate and return the area of a circle based on its radius.")

    # Prompt user to start coding
    input("Press Enter to start coding...")

    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp_file:
        file_path = tmp_file.name

        # Write task instructions to the file
        task_instructions = """\
        # Task Instructions:
        # Create a class named 'Shape' with a method 'area' that does nothing.
        # Then create two subclasses 'Rectangle' and 'Circle' that inherit from 'Shape'.
        # Override the 'area' method in each subclass to calculate and return the area of the shape.

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
    if "Shape" not in locals() or not callable(Shape):
        print("Oops! The class 'Shape' is not defined correctly.")
        return

    if "Rectangle" not in locals() or not callable(Rectangle):
        print("Oops! The class 'Rectangle' is not defined correctly.")
        return

    if "Circle" not in locals() or not callable(Circle):
        print("Oops! The class 'Circle' is not defined correctly.")
        return

    rectangle = Rectangle(4, 6)
    circle = Circle(5)

    if not hasattr(rectangle, "area") or not callable(rectangle.area):
        print("Oops! The 'area' method is missing or not defined correctly in the 'Rectangle' class.")
        return

    if not hasattr(circle, "area") or not callable(circle.area):
        print("Oops! The 'area' method is missing or not defined correctly in the 'Circle' class.")
        return

    # Calculate and display the areas
    print("Now let's calculate the areas of the shapes.")
    print(f"The area of the rectangle is: {rectangle.area()}")
    print(f"The area of the circle is: {circle.area()}")

    print("Scenario completed.")
    print("Now, let's test your understanding of the concepts.")

    # Quiz
    print("\nQuiz:")
    print("What is 'Polymorphism' in object-oriented programming?")
    print("a) The process of creating objects from classes.")
    print("b) The ability to create multiple objects from a single class.")
    print("c) The process of deriving new classes from existing classes.")
    print("d) The ability of objects of different classes to respond to the same method name.")

    # Get user's answer
    answer = input("Enter your answer (a, b, c, or d): ")

    # Check the answer
    if answer.lower() == "d":
        print("Congratulations! You answered correctly.")
    else:
        print("Oops! That's incorrect. The correct answer is 'd) The ability of objects of different classes to respond to the same method name.'")

    # Explanation of polymorphism
    print("\nPolymorphism is demonstrated in this scenario through the use of the 'area' method.")
    print("Both the 'Rectangle' and 'Circle' classes inherit from the 'Shape' class.")
    print("Each subclass overrides the 'area' method to provide its own implementation.")
    print("Even though the method has the same name, it behaves differently for each shape.")
    print("This allows for code reuse and flexibility in handling objects of different classes.")

