import math

x = 41
print(math.sqrt(x))  # prints the square root of 41, approximately 6.40312

print(round(1.7))         # prints 2, as round() rounds to the nearest integer
print(round(math.sqrt(x), 2))  # prints 6.40, as the square root of 41 (6.40312) rounds down to 6

print(math.pow(2, 2))  # prints 4.0, as 2 raised to the power of 2

print(math.ceil(4.1676))    # prints 5, ceiling of 4.1676 is 5
print(math.floor(4.8676))   # prints 4, floor of 4.8676 is 4
print(math.ceil(-4.1676))   # prints -4, ceiling of -4.1676 is -4
print(math.floor(-4.8676))  # prints -5, floor of -4.8676 is -5

print(abs(-4.775))  # prints 4.775, absolute value of -4.775 is 4.775
