#!/usr/bin/python3
"""This module defines a class BaseGeometry
with a public instance method:
def area(self): that raises an Exception.
"""
class BaseGeometry():
    """Class BaseGeometry.
    It has a method, area, which is
    not implemented yet.

    """
    def __init__(self):
         pass

    def area(self):
        """
        Calculate the area of the geometric shape (not implemented).

        Raises:
            Exception: This method is not implemented in the base class.
        
        """
        raise Exception("area() is not implemented")