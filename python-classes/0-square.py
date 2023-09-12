"""
A class that defines a square.

Attributes:
    size (int): The size of the square.

Methods:
    __init__(self, size):
        Initialize the square with the given size.
    size(self):
        Get the size of the square.
    size(self, size):
        Set the size of the square.
"""

class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size):
            Initialize the square with the given size.

        This method is called when a new `Square` object is created.
        It takes one argument, the size of the square.
        The size can be of any type, and no type or value verification is done.

        size(self, size):
            Set the size of the square.

        This method sets the value of the `size` attribute.

        This code changes the size of the square object `sq` to 20.
    """

    def __init__(self, size):    # Initialize the square with the given size. 
     
        self._size = size  # Private instance attribute

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            The size of the square.
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The size of the square.
        """
        self._size = size
