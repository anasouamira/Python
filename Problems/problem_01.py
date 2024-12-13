"""
    _Plindrome Check
    
    -Ask the user for a string and check if it is a palindrome (reads the same forwards and backwards).
    Use if and a for loop.
    
"""
a = "anas"
print(a[-1])

text = input("Enter a string: ")
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-i-1]:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not a palindrome")



