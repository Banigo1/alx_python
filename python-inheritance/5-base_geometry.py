#!/usr/bin/python3
"""
    This is a base class
"""

class BaseGeometry:
    """
    This is a base class
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']

    def area(self):
        """
        Function that raise an exception with an error message
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name: str, value: int):
        """
        Function validates whether the value is an integer and
        is greater than 0, otherwise it raises an error
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")