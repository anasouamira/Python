# List comprehension = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# Using list comprehensions in various scenarios

# Example 1: Create a list of squares
squares = [x**2 for x in range(10)]
print("Squares:", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 2: Filter even numbers from a range
evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Example 3: Convert a list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase Fruits:", uppercase_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# Example 4: Create a list of tuples (number, square)
number_square_pairs = [(x, x**2) for x in range(5)]
print("Number-Square Pairs:", number_square_pairs)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Example 5: Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [num for sublist in nested_list for num in sublist]
print("Flattened List:", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
