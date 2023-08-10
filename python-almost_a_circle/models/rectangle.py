from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from the class Base

    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
        x: The x-coordinate of the rectangle.
        y: The y-coordinate of the rectangle.

    Example:
        >>> rectangle = Rectangle(10, 20, 10, 20)
        >>> print(rectangle)
        [Rectangle] (1) 10/20 - 10/20
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle.__init__() initializes the rectangle.
        def __init__(self, width, height, x=0, y=0, id=None):
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

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
        