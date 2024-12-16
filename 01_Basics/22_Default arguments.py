# default arguments = A default value for certain parameters 
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def greet(name="Guest", greeting="Hello"):
    """Function to greet a person with a default message."""
    return f"{greeting}, {name}!"

# Calling the function without any arguments
print(greet())  # Output: Hello, Guest!

# Calling the function with one argument
print(greet("Alice"))  # Output: Hello, Alice!

# Calling the function with both arguments
print(greet("Bob", "Hi"))  # Output: Hi, Bob!

def multiply_numbers(a=1, b=1):
    """Function to multiply two numbers with default arguments."""
    return a * b

# Function calls and demonstration of `return`:
# Calling without arguments; uses default values.
result1 = multiply_numbers()  
print(f"Result 1 (default arguments): {result1}")  # Output: 1

# Calling with one argument; overrides the first default.
result2 = multiply_numbers(5)
print(f"Result 2 (one argument): {result2}")  # Output: 5 (5 * 1)

# Calling with both arguments; overrides both defaults.
result3 = multiply_numbers(3, 4)
print(f"Result 3 (both arguments): {result3}")  # Output: 12 (3 * 4)
