# Example of collections in Python

# List: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print("List:", fruits)

# Tuple: Ordered, immutable, allows duplicates
coordinates = (10.5, 20.3, 30.6)
print("Tuple:", coordinates)

# Set: Unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 2, 1}
print("Set:", unique_numbers)

# Dictionary: Unordered, mutable, stores key-value pairs
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", person)

# Specialized collections (example from collections module)
from collections import Counter

# Counter: Counts occurrences of elements in a collection
word_counts = Counter(["apple", "banana", "apple", "cherry", "banana", "banana"])
print("Counter:", word_counts)

#Output : 

# List: ['apple', 'banana', 'cherry', 'apple']
# Tuple: (10.5, 20.3, 30.6)
# Set: {1, 2, 3}
# Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Counter: Counter({'banana': 3, 'apple': 2, 'cherry': 1})

