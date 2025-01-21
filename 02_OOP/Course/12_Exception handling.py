# exception = An event that interrupts the flow of a program
#           (zeroDivisionError, TypeError, ValueError)
#           1.try, 2.except, 3.finally

def divide_numbers(a, b):
    """Divides two numbers and handles division by zero."""
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError as e:
        print("Error: Both inputs must be numbers!")
        return None
    else:
        # Executes if no exception occurs
        print("Division successful!")
        return result
    finally:
        # Executes no matter what (exception or no exception)
        print("Execution completed.")

# Example usage
print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "a"))  # Invalid input


# Output: 
# Division successful!
# Execution completed.
# 5.0
# Error: Cannot divide by zero!
# Execution completed.
# None
# Error: Both inputs must be numbers!
# Execution completed.
# None
