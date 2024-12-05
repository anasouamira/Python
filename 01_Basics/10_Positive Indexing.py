#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

# Positive Indexing
text = "Python"
print(text[0])  # Output: 'P'
print(text[3])  # Output: 'h'

# Negative Indexing
print(text[-1])  # Output: 'n'
print(text[-4])  # Output: 't'

# Slicing
print(text[0:4])  # Output: 'Pyth'
print(text[2:])   # Output: 'thon'
print(text[:4])   # Output: 'Pyth'
print(text[::2])  # Output: 'Pto' (step of 2)
