#!/usr/bin/python3
""" This module contains an empty class named Square,
that defines a square by a
private instance attribute: size
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