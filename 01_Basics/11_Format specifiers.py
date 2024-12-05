# format specifiers = {:flags} format a value based on what 
#                     flags are inserted 

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces 
# :< = left justify 
# :> = right justify 
# :~ = center align 
# :+ = use a plus sign to indicate positive value 
# := = place sign to leftmost position 
# : = insert a space before positive numbers 
# :, = comma separator 

# Using the format() method
name = "Alice"
age = 30
pi = 3.14159

# Basic placeholders
print("My name is {} and I am {} years old.".format(name, age))

# Specifying width and alignment
print("Left-aligned: '{:<10}'".format("Hello"))  # Left-aligned, 10 characters wide
print("Right-aligned: '{:>10}'".format("Hello"))  # Right-aligned, 10 characters wide
print("Center-aligned: '{:^10}'".format("Hello"))  # Center-aligned, 10 characters wide

# Formatting numbers
print("Pi to 2 decimal places: {:.2f}".format(pi))  # 2 decimal places
print("Number with zero-padding: {:04d}".format(42))  # Zero-padded to 4 digits

# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")  # Inline variables
print(f"The value of pi is {pi:.3f}.")  # Format with 3 decimal places
print(f"Center-aligned: {'Python':^10}")  # Center-aligned

# Using the % operator (Old Style)
print("Name: %s, Age: %d" % (name, age))  # Basic placeholders
print("Pi: %.2f" % pi)  # Format float to 2 decimal places
print("Number: %04d" % 42)  # Zero-padded number
