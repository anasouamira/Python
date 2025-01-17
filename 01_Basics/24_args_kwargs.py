# *args = allows you to pass multiple non-key arguments

# **kwargs = allows you to pass multiple keyword-arguments

#          * unpacking operator

#          1. positional 2. default 3. keyword 4. ARBITRARY

# Function to demonstrate *args (variable number of positional arguments)
def demo_args(*args):
    print("Positional arguments (*args):")
    # Iterate over each positional argument passed
    for arg in args:
        print(arg)

# Function to demonstrate **kwargs (variable number of keyword arguments)
def demo_kwargs(**kwargs):
    print("\nKeyword arguments (**kwargs):")
    # Iterate over each key-value pair in the keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Main function to call the demo functions
def main():
    # Call demo_args with several positional arguments
    demo_args(1, 2, 3, "Hello", [4, 5, 6])

    # Call demo_kwargs with several keyword arguments
    demo_kwargs(name="Alice", age=25, location="Wonderland")

# Check if this script is run directly (not imported as a module)
if __name__ == "__main__":
    main()
