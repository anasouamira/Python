# 1. User-defined function
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

# Call the function
print(greet("anas"))  # Output: Hello, Anas!

# 2. Lambda function
square = lambda x: x ** 2

# Use the lambda function
print(square(4))  # Output: 16

# 3. Recursive function: Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Calculate factorial
print(factorial(5))  # Output: 120

# 4. Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Use the generator function
for num in countdown(5):
    print(num)  # Output: 5 4 3 2 1
