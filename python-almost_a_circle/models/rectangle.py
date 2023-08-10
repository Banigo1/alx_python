from models.base import Base

class Rectangle(Base):
    """A class to represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        if width < 0:
            raise ValueError("Width must be non-negative.")
        self.__width = width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        if height < 0:
            raise ValueError("Height must be non-negative.")
        self.__height = height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle."""
        if x < 0:
            raise ValueError("X-coordinate must be non-negative.")
        self.__x = x

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle."""
        if y < 0:
            raise ValueError("Y-coordinate must be non-negative.")
        self.__y = y
