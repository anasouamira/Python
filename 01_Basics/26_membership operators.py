# Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in 

# Demonstration of membership operators

# Define some sequences
fruits = ["apple", "banana", "cherry"]
text = "Hello, world!"

# Using 'in' operator
print("apple" in fruits)   # True: "apple" is in the list 'fruits'
print("grape" in fruits)   # False: "grape" is not in the list 'fruits'
print("world" in text)     # True: "world" is in the string 'text'

# Using 'not in' operator
print("mango" not in fruits)  # True: "mango" is not in the list 'fruits'
print("banana" not in fruits)  # False: "banana" is in the list 'fruits'
print("Python" not in text)   # True: "Python" is not in the string 'text'


