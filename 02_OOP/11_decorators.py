# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function 
#             Pass the base function as an argument to the decorator 

#             @add_sprinkles 
#             get_ice_cream("vanilla") 

# Define a decorator
def log_execution(func):
    """A decorator that logs the execution of a function."""
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Apply the decorator to a function
@log_execution
def add(a, b):
    """Adds two numbers."""
    return a + b

@log_execution
def greet(name, message="Hello"):
    """Greets a person with a message."""
    return f"{message}, {name}!"

# Example usage
sum_result = add(10, 20)
print(sum_result)  # This will include log messages

greeting = greet("Alice")
print(greeting)  # This will include log messages

greeting_custom = greet("Bob", message="Welcome")
print(greeting_custom)  # This will include log messages



# Calling function 'add' with arguments (10, 20) and {}
# Function 'add' returned: 30
# 30
# Calling function 'greet' with arguments ('Alice',) and {}
# Function 'greet' returned: Hello, Alice!
# Hello, Alice!
# Calling function 'greet' with arguments ('Bob',) and {'message': 'Welcome'}
# Function 'greet' returned: Welcome, Bob!
# Welcome, Bob!
