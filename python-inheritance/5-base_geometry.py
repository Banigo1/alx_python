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
    
    
        """
 Write a class BaseGeometry (based on 4-base_geometry.py).
Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module.
        
        """