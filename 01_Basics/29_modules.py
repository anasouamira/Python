# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# Example 1: Using a built-in module
import math

# Use math module functions
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("Value of pi:", math.pi)  # Output: 3.141592653589793

# Example 2: Importing specific functions from a module
from random import randint, choice

# Generate a random integer
print("Random integer between 1 and 10:", randint(1, 10))  

# Choose a random item from a list
items = ["apple", "banana", "cherry"]
print("Random fruit:", choice(items))

# Example 3: Creating and using a custom module
# Let's assume you have a file named `my_module.py` with the following content:
# def greet(name):
#     return f"Hello, {name}!"

# Import the custom module
import my_module

# Use the greet function from the custom module
print(my_module.greet("Alice"))  # Output: Hello, Alice!

# Example 4: Renaming a module
import datetime as dt

# Use the datetime module with its alias
current_time = dt.datetime.now()
print("Current time:", current_time)

# Example 5: Listing all functions and attributes in a module
import os

print("Functions in 'os' module:", dir(os))
