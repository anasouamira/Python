# Creating a 2D list (a 3x3 grid)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print("Element at row 1, column 2:", matrix[0][1])  # Output: 2 (row 0, column 1)
print("Entire second row:", matrix[1])  # Output: [4, 5, 6]

# Modifying elements
matrix[2][0] = 10  # Change the first element in the third row to 10
print("Modified Matrix:", matrix)

# Adding a new row
matrix.append([10, 11, 12])
print("Matrix after adding a row:", matrix)

# Adding a new column to all rows
for row in matrix:
    row.append(13)
print("Matrix after adding a column:", matrix)

# Iterating through a 2D list
print("Iterating through the 2D list:")
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()

# Using list comprehension to flatten a 2D list
flattened = [elem for row in matrix for elem in row]
print("Flattened List:", flattened)

# Output ==========================================================

"""
Element at row 1, column 2: 2
Entire second row: [4, 5, 6]
Modified Matrix: [[1, 2, 3], [4, 5, 6], [10, 8, 9]]
Matrix after adding a row: [[1, 2, 3], [4, 5, 6], [10, 8, 9], [10, 11, 12]]
Matrix after adding a column: [[1, 2, 3, 13], [4, 5, 6, 13], [10, 8, 9, 13], [10, 11, 12, 13]]
Iterating through the 2D list:
1 2 3 13 
4 5 6 13 
10 8 9 13 
10 11 12 13 
Flattened List: [1, 2, 3, 13, 4, 5, 6, 13, 10, 8, 9, 13, 10, 11, 12, 13]

"""