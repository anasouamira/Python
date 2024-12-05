# for loops = execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc.


# Iterating over a list
print("Iterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Iterating over a range of numbers
print("\nIterating over a range:")
for number in range(5):  # 0 to 4
    print(f"Number: {number}")

# Iterating over a string
print("\nIterating over a string:")
for char in "Python":
    print(f"Character: {char}")

# Using break in a for loop
print("\nFor loop with break:")
for number in range(10):
    if number == 5:
        print("Breaking the loop at 5.")
        break
    print(f"Number: {number}")

# Using continue in a for loop
print("\nFor loop with continue:")
for number in range(5):
    if number == 2:
        print("Skipping 2")
        continue
    print(f"Number: {number}")

