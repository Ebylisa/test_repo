"""Creating a Car class with methods and instances"""
import
# Define the Car class
class Car:
    """Creating a Car class with 6 parameters and instances"""
    def __init__(self, make, model, body, engine, year, and color):
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = year
        self.color = color

# Prompt the user to enter the information for the car for each parameter.
 make = input("Enter the make of your car:")
 model = input("Enter the model of your car:")
 
# Hint: Make sure the year is an integer.

# Create an instance of the `Car` class and pass in the variables from the user.
car = Car()

# Print the details of the car
print('Here is the information you enter for the car.')
