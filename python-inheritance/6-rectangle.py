"""
In this class, the area method raises an exception indicating that not  it is not implemented. The integer_validator method checks if the value is an integer and if it is greater than 0. If not, it raises the appropriate exceptions.
The name parameter is assumed to always be a string.
This class does not import any modules.

"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """

        # Validate and assign width and height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
