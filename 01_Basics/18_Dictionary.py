# Create an empty dictionary
data = {}

# 1. Add key-value pairs
data["name"] = "Alice"
data["age"] = 25

# 2. Access a value by key
print(data["name"])  # Output: Alice

# 3. Use `get()` to retrieve a value safely
value = data.get("age", "Default Value")
print(value)  # Output: 25

# 4. Remove a key-value pair with `pop()`
age = data.pop("age")
print(age)          # Output: 25
print(data)         # Output: {'name': 'Alice'}

# 5. Remove the last inserted item with `popitem()`
last_item = data.popitem()
print(last_item)    # Output: ('name', 'Alice')
print(data)         # Output: {}

# 6. Update the dictionary with new key-value pairs
data.update({"name": "Bob", "age": 30})
print(data)         # Output: {'name': 'Bob', 'age': 30}

# 7. Retrieve all keys with `keys()`
keys = data.keys()
print(keys)         # Output: dict_keys(['name', 'age'])

# 8. Retrieve all values with `values()`
values = data.values()
print(values)       # Output: dict_values(['Bob', 30])

# 9. Retrieve all key-value pairs with `items()`
items = data.items()
print(items)        # Output: dict_items([('name', 'Bob'), ('age', 30)])

# 10. Check if a key exists with `in`
print("name" in data)  # Output: True

# 11. Clear the dictionary with `clear()`
data.clear()
print(data)         # Output: {}

# 12. Create a dictionary with default values using `fromkeys()`
defaults = dict.fromkeys(["key1", "key2"], "default")
print(defaults)     # Output: {'key1': 'default', 'key2': 'default'}

# 13. Copy a dictionary with `copy()`
data = {"name": "Alice", "age": 25}
copy_data = data.copy()
print(copy_data)    # Output: {'name': 'Alice', 'age': 25}

