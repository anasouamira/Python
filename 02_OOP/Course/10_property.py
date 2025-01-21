# @ropertyr = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter for the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width."""
        if value <= 0:
            raise ValueError("Width must be greater than zero.")
        self._width = value

    @property
    def height(self):
        """Getter for the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height."""
        if value <= 0:
            raise ValueError("Height must be greater than zero.")
        self._height = value

    @property
    def area(self):
        """Read-only property to calculate the area."""
        return self._width * self._height


# Example usage
rect = Rectangle(5, 10)

# Access attributes using property
print(f"Width: {rect.width}, Height: {rect.height}")  # Width: 5, Height: 10

# Modify attributes using property setters
rect.width = 7
rect.height = 14
print(f"Updated Width: {rect.width}, Height: {rect.height}")  # Updated Width: 7, Height: 14

# Access computed property
print(f"Area: {rect.area}")  # Area: 98

# Attempting to set invalid values
try:
    rect.width = -3
except ValueError as e:
    print(e)  # Width must be greater than zero.
