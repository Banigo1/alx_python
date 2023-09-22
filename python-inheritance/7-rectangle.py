class BaseGeometry:
    def __init__(self):
        pass
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def __validate_integer(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width and height must be positive integers.")
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__validate_integer(width)
        self.__validate_integer(height)
        self.__width = width
        self.__height = height
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__validate_integer(width)
        self.__validate_integer(height)
        self.__width = width
        self.__height = height
class BaseGeometry:
    def __init__(self):
        pass


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__validate_integer(width)
        self.__validate_integer(height)
        self.__width = width
        self.__height = height

    def __validate_integer(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width and height must be positive integers.")
