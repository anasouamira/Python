# Example string
s = " hello world "

# 1. capitalize() - Capitalizes the first letter of the string
capitalized_string = s.capitalize()
print("Capitalized:", capitalized_string)  # Output: " Hello world "

# 2. casefold() - Converts the string to lowercase
casefolded_string = s.casefold()
print("Casefolded:", casefolded_string)  # Output: " hello world "

# 3. center(width, fillchar) - Centers the string within a given width and fills with a character
centered_string = s.center(20, '*')
print("Centered:", centered_string)  # Output: "*** hello world ****"

# 4. count(substring, start, end) - Counts the occurrences of a substring in the string
substring_count = s.count("o")
print("Count of 'o':", substring_count)  # Output: 2

# 5. encode(encoding) - Encodes the string using the specified encoding (default is UTF-8)
encoded_string = s.encode("utf-8")
print("Encoded:", encoded_string)  # Output: b' hello world '

# 6. endswith(suffix) - Checks if the string ends with the specified suffix
ends_with_check = s.endswith("world ")
print("Ends with 'world ':", ends_with_check)  # Output: True

# 7. find(substring) - Returns the index of the first occurrence of a substring, or -1 if not found
index_of_o = s.find("o")
print("Index of first 'o':", index_of_o)  # Output: 4

# 8. isalnum() - Checks if all characters in the string are alphanumeric
is_alnum = "hello123".isalnum()
print("Is alphanumeric:", is_alnum)  # Output: True

# 9. isalpha() - Checks if all characters in the string are alphabetic
is_alpha = "hello".isalpha()
print("Is alphabetic:", is_alpha)  # Output: True

# 10. isdigit() - Checks if all characters in the string are digits
is_digit = "12345".isdigit()
print("Is digit:", is_digit)  # Output: True

# 11. join(iterable) - Joins elements of an iterable with the string as the separator
words = ["hello", "world"]
joined_string = " ".join(words)
print("Joined string:", joined_string)  # Output: "hello world"

# 12. lstrip() - Removes leading spaces from the string
stripped_left = s.lstrip()
print("Left stripped:", repr(stripped_left))  # Output: 'hello world '

# 13. rstrip() - Removes trailing spaces from the string
stripped_right = s.rstrip()
print("Right stripped:", repr(stripped_right))  # Output: ' hello world'

# 14. split() - Splits the string into a list based on spaces (or other separator)
split_string = s.split()
print("Split string:", split_string)  # Output: ['hello', 'world']

# 15. replace(old, new) - Replaces all occurrences of 'old' with 'new'
replaced_string = s.replace("world", "everyone")
print("Replaced string:", replaced_string)  # Output: " hello everyone "

# 16. strip() - Removes leading and trailing spaces from the string
stripped_string = s.strip()
print("Stripped:", repr(stripped_string))  # Output: 'hello world'

# 17. upper() - Converts all characters in the string to uppercase
upper_string = s.upper()
print("Uppercase:", upper_string)  # Output: " HELLO WORLD "

# 18. lower() - Converts all characters in the string to lowercase
lower_string = s.lower()
print("Lowercase:", lower_string)  # Output: " hello world "

# 19. swapcase() - Swaps the case of all characters (lowercase to uppercase and vice versa)
swapped_case = s.swapcase()
print("Swapped case:", swapped_case)  # Output: " HELLO WORLD "

# 20. title() - Converts the first character of each word to uppercase
title_string = s.title()
print("Title case:", title_string)  # Output: " Hello World "
