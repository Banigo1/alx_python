class Rectangle:
    """
    A class used to represent a Rectangle

    ...

    Attributes
    ----------
    width : int
        the width of the rectangle
    height : int
        the height of the rectangle

    Methods
    -------
    area():
        Returns the area of the rectangle
    integer_validator(name, value):
        Validates that the value is a positive integer
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    @staticmethod
    def integer_validator(name, value):
        """
        Validates that the value is a positive integer

        Parameters
        ----------
        name : str
            The name of the attribute to be validated
        value : int
            The value of the attribute to be validated

        Raises
        ------
        TypeError
            If value is not an integer
        ValueError
            If value is not greater than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Square(Rectangle):
    """
    A class used to represent a Square, inherits from Rectangle class

    ...

    Attributes
    ----------
    size : int
        the size of the square (both width and height)

    Methods
    -------
    area():
        Returns the area of the square
    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of the square (both width and height)
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
