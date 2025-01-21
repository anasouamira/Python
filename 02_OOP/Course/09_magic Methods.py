# Magic methods = Dunder methods (double underscore) _ init _, _ str, eq _ 
#                They are automatically called by many of Python's built-in operations.
#                They allow developers to define or customize the behavior of objects 


class MagicDemo:
    def __init__(self, value):
        """Initialize the object with a value."""
        self.value = value

    def __str__(self):
        """Define the string representation of the object."""
        return f"MagicDemo({self.value})"

    def __add__(self, other):
        """Define the behavior of the + operator."""
        if isinstance(other, MagicDemo):
            return MagicDemo(self.value + other.value)
        return NotImplemented

    def __eq__(self, other):
        """Define the behavior of the == operator."""
        if isinstance(other, MagicDemo):
            return self.value == other.value
        return NotImplemented

    def __len__(self):
        """Define behavior for len() function."""
        return len(str(self.value))


# Example usage
obj1 = MagicDemo(5)
obj2 = MagicDemo(10)

print(obj1)            # MagicDemo(5)
print(obj2)            # MagicDemo(10)

# Add two objects
obj3 = obj1 + obj2
print(obj3)            # MagicDemo(15)

# Compare two objects
print(obj1 == obj2)    # False
print(obj1 == MagicDemo(5))  # True

# Use len() on an object
print(len(obj1))       # Length of the string representation of the value, e.g., 1
