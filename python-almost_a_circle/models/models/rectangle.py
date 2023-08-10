# models/rectangle.py
# 1. First Rectangle
"""
A class to represent a rectangle.

This class has the following public methods:

* width: Gets the width of the rectangle.
* width: Sets the width of the rectangle.
* height: Gets the height of the rectangle.
* height: Sets the height of the rectangle.
* x: Gets the x-coordinate of the rectangle.
* x: Sets the x-coordinate of the rectangle.
* y: Gets the y-coordinate of the rectangle.
* y: Sets the y-coordinate of the rectangle.

To create a new rectangle, you can use the following syntax:

```python
rectangle = Rectangle(width=10, height=20, x=0, y=0)


The `width`, `height`, `x`, and `y` arguments are optional. If they are not specified, the default values will be used.

The `Rectangle` class can be used to represent a rectangle in your code. You can use the public methods of the class to get and set the attributes of the rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """A class to represent a rectangle."""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle."""
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        if width < 0:
            raise ValueError("Width must be non-negative.")
        self._width = width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        if height < 0:
            raise ValueError("Height must be non-negative.")
        self._height = height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle."""
        if x < 0:
            raise ValueError("X-coordinate must be non-negative.")
        self._x = x

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle."""
        if y < 0:
            raise ValueError("Y-coordinate must be non-negative.")
        self._y = y
        