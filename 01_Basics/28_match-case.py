# Using match-case for different scenarios

# Example 1: Basic pattern matching
command = "start"

match command:
    case "start":
        print("The system is starting...")
    case "stop":
        print("The system is stopping...")
    case "restart":
        print("The system is restarting...")
    case _:
        print("Unknown command!")

# Example 2: Matching numeric ranges using conditions
number = 15

match number:
    case n if n < 10:
        print("The number is less than 10.")
    case n if 10 <= n <= 20:
        print("The number is between 10 and 20.")
    case _:
        print("The number is greater than 20.")

# Example 3: Decomposing a tuple
point = (1, 2)

match point:
    case (0, 0):
        print("Point is at the origin.")
    case (x, 0):
        print(f"Point is on the x-axis at {x}.")
    case (0, y):
        print(f"Point is on the y-axis at {y}.")
    case (x, y):
        print(f"Point is at coordinates ({x}, {y}).")

# Example 4: Matching lists
data = [1, 2, 3]

match data:
    case [1, 2, 3]:
        print("Matched the list [1, 2, 3].")
    case [1, *rest]:
        print(f"List starts with 1 and has the rest: {rest}")
    case _:
        print("No match found.")
