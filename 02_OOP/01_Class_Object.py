# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phon, cup, book 
#          You need a "class" to create many objects 

# class = (blueprint) used to design the structure and layout of an object


# Creating Classes and Objects ========================================================================

# Defining a class
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method to display a greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances) of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Calling object methods
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.
person2.greet()  # Output: Hello, my name is Bob and I am 30 years old.

# Example of Class with Methods and Attributes =========================================================

class Car:
    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car information
    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")

    # Method to start the car
    def start(self):
        print(f"The {self.brand} {self.model} is starting...")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(my_car.brand)  # Output: Toyota

# Calling methods
my_car.display_info()  # Output: This car is a 2020 Toyota Corolla.
my_car.start()         # Output: The Toyota Corolla is starting...
