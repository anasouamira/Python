# Initializing variables
A = 10
B = A  # B takes the value of A
A += 1  # A is incremented by 1 (post-increment equivalent)

print(f"A = {A}")
print(f"B = {B}")

A += 1  # A is incremented by 1 (pre-increment equivalent)
B = A  # B takes the updated value of A

print(f"A = {A}")
print(f"B = {B}")
