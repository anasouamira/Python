# logical operators = evaluate multiple conditions (or, and, not)

#                     Or = at least one condition must be True 

#                     and = both conditions must be True

#                     not = inverts the condition (not False, not True)

# User's details
is_admin = False
has_valid_membership = True
is_account_expired = False
is_banned = False

# Use 'or', 'and', and 'not' to check the conditions for login
if (is_admin or has_valid_membership) and not is_account_expired and not is_banned:
    print("Login successful. Welcome to the system!")
else:
    print("Login failed. Please check your account status.")
