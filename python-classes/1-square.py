"""
This module defines a Square class and a Private instance attribute: size,
Instantiation with optional size: def __init__(self, size=0).
size must be an integer, otherwise raise a TypeError exception with the
message size must be an integer. If size is less than 0, raise a
ValueError exception with the message size must be >= 0

"""

class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
       
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
 