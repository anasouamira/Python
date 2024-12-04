# conditional expression = A one-line shortcut for the if-else statement (ternary operator).
#                          Print or assign one of two values based on a condition
#                          X if condition else Y


num = 5  
a = 6    
b = 7   
age = 13  
temperature = 20  
user_role = "guest"  

# This line seems to have a small syntax issue with the quote marks. Here's the fixed version:
print("Positive" if num > 0 else "Negative")  # Prints "Positive" since 'num' is 5, which is greater than 0

# Using a conditional expression to check if 'num' is even or odd
result = "EVEN" if num % 2 == 0 else "ODD"  # Since num is 5 (odd), 'result' will be "ODD"

# Conditional expression to find the maximum of 'a' and 'b'
max_num = a if a > b else b  # Since 'a' (6) is less than 'b' (7), 'max_num' will be 7

# Conditional expression to find the minimum of 'a' and 'b'
min_num = a if a < b else b  # Since 'a' (6) is less than 'b' (7), 'min_num' will be 6

# Conditional expression to determine if the person is an Adult or a Child based on age
status = "Adult" if age >= 18 else "Child"  # Since 'age' is 13, 'status' will be "Child"

# Conditional expression to check if the temperature is above 20 degrees (HOT) or not (COLD)
weather = "HOT" if temperature > 20 else "COLD"  # Since 'temperature' is 20, 'weather' will be "COLD"

# Conditional expression to set access level based on the user role
access_level = "Full Access" if user_role == "admin" else "Limited Access"  # Since 'user_role' is "guest", 'access_level' will be "Limited Access"
