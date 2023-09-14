# Square class that defines a square.
class Square:
    """
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
    def __init__(self, size=0):
       
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # size(self, value): Setter property for setting the size of the square.
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # TypeError: If size is not an integer.
        if value < 0:
            raise ValueError("size must be >= 0")
        # ValueError: If size is less than 0.
        self.__size = value
