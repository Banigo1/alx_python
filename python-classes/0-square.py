#!/usr/bin/python3
""" This module contains an empty class, Square that defines a square by:
Private instance attribute: size
Instantiation with size (no type/value verification)

"""
class Square:
    
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        get_size(): Get the size of the square.
        set_size(size: int): Set the size of the square.
        area(): Calculate the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The new size of the square.
        """
        self.__size = size
