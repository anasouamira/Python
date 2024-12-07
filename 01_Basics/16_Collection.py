# Example of collections in Python with methods

# List: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print("List:", fruits)

# List methods
fruits.append("orange")  # Add an element at the end
fruits.remove("apple")   # Remove the first occurrence of an element
fruits.insert(1, "grape")  # Insert at a specific position
fruits.pop(2)  # Remove element at index 2
fruits.sort()  # Sort the list
print("Modified List:", fruits)

# Tuple: Ordered, immutable, allows duplicates
coordinates = (10.5, 20.3, 30.6)

# Tuple methods
print("Index of 20.3 in tuple:", coordinates.index(20.3))  # Find the index of an element
print("Count of 30.6 in tuple:", coordinates.count(30.6))  # Count occurrences

# Set: Unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 2, 1}
print("Set:", unique_numbers)

# Set methods
unique_numbers.add(4)  # Add an element
unique_numbers.remove(2)  # Remove a specific element
unique_numbers.update({5, 6})  # Add multiple elements
unique_numbers.discard(10)  # Remove an element if it exists (no error if not found)
print("Modified Set:", unique_numbers)

# Dictionary: Unordered, mutable, stores key-value pairs
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", person)

# Dictionary methods
person["country"] = "USA"  # Add a new key-value pair
person.update({"age": 31})  # Update an existing key
del person["city"]  # Remove a key-value pair
keys = person.keys()  # Get all keys
values = person.values()  # Get all values
items = person.items()  # Get all key-value pairs
print("Modified Dictionary:", person)

# Specialized collections (example from collections module)
from collections import Counter

# Counter: Counts occurrences of elements in a collection
word_counts = Counter(["apple", "banana", "apple", "cherry", "banana", "banana"])
print("Counter:", word_counts)

# Counter methods
word_counts.update(["apple", "banana", "cherry"])  # Add more counts
most_common = word_counts.most_common(2)  # Get the two most common elements
print("Updated Counter:", word_counts)
print("Most Common Elements:", most_common)

# Output : =====================================================================

# List: ['apple', 'banana', 'cherry', 'apple']
# Modified List: ['apple', 'banana', 'grape', 'orange']
# Index of 20.3 in tuple: 1
# Count of 30.6 in tuple: 1
# Set: {1, 2, 3}
# Modified Set: {1, 3, 4, 5, 6}
# Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Modified Dictionary: {'name': 'Alice', 'age': 31, 'country': 'USA'}
# Counter: Counter({'banana': 3, 'apple': 2, 'cherry': 1})
# Updated Counter: Counter({'banana': 4, 'apple': 3, 'cherry': 2})
# Most Common Elements: [('banana', 4), ('apple', 3)]

