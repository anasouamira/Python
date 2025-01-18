# Scope resolution example

# Global scope
x = "global"

def outer_function():
    # Enclosing scope
    x = "enclosing"

    def inner_function():
        # Local scope
        x = "local"
        print("Inner function:", x)  # Output: "local"

    inner_function()
    print("Outer function:", x)  # Output: "enclosing"

# Access global variable
print("Global scope:", x)  # Output: "global"

# Call outer function
outer_function()

# Built-in scope
print("Length of 'scope':", len("scope"))  # `len` is in the built-in scope


# what is (if name == 'main') : 

# File: my_module.py

def greet(name):
    return f"Hello, {name}!"

# Code to be executed only when run directly
if __name__ == "__main__":
    print("This code runs only when the script is executed directly.")
    # Example usage
    print(greet("Alice"))
