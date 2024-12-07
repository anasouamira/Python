# Nested loop example: printing a multiplication table

# Outer loop iterates over rows
for i in range(1, 6):  # Rows 1 to 5
    # Inner loop iterates over columns
    for j in range(1, 6):  # Columns 1 to 5
        # Print the product of the current row and column
        print(f"{i * j:2}", end=" ")  # Format output with spacing
    print()  # Newline after each row
