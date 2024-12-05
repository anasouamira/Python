# while loop = execute some code WHILE some condition remains true;

# Basic While Loop
count = 0
print("Basic While Loop:")
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment to avoid infinite loop

# Infinite Loop with Break
print("\nInfinite Loop with Break:")
count = 0
while True:  # This loop would run forever without the break statement
    print(f"Count is: {count}")
    count += 1
    if count == 5:
        print("Breaking the loop.")
        break  # Exit the loop when count reaches 5

# While Loop with Continue
print("\nWhile Loop with Continue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping 3")
        continue  # Skip the rest of the loop body when count is 3
    print(f"Count is: {count}")
