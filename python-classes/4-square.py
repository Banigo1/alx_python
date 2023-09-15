"""
This module defines a Square class.

Private instance attribute: size
Property def size(self): to retrieve it
Property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line.

"""
class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance with an optional size.
        area(self): Calculates and returns the current square's area.
        my_print(self): Prints the square using the '#' character.

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        If the size is equal to 0, it prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
