# keyword arguments = an argument preceded by an identifier 
#                     helps with readability 
#                     order of arguments doesn't matter 
#                     1. positional 2. default 3. KEYWORD 4. arbitrary 

def describe_person(name, age, city="Unknown", hobby="None"):
    """Function to describe a person with keyword arguments."""
    return f"{name} is {age} years old, lives in {city}, and enjoys {hobby}."

# Calling the function with positional arguments
result1 = describe_person("Alice", 25)
print(result1)  # Output: Alice is 25 years old, lives in Unknown, and enjoys None.

# Calling the function with a mix of positional and keyword arguments
result2 = describe_person("Bob", 30, hobby="Cycling")
print(result2)  # Output: Bob is 30 years old, lives in Unknown, and enjoys Cycling.

# Calling the function with only keyword arguments
result3 = describe_person(name="Charlie", age=40, city="New York", hobby="Painting")
print(result3)  # Output: Charlie is 40 years old, lives in New York, and enjoys Painting.
