#!/usr/bin/python3
"""
This module defines several classes for geometry calculations.

class TypeMetaClass(type):
    This is a metaclass used to represent the class type in order to eliminate
    the inherited method __init_subclass__ from BaseGeometry.

    Methods:
    __dir__(cls) -> None:
        Exclude attribute __init_subclass__ in dir().

class BaseGeometry(metaclass=TypeMetaClass):
    This is a base class for geometric shapes.

    Methods:
    __dir__(cls) -> None:
        Exclude attribute __init_subclass__ in dir().
    area(self):
        Raises an exception with an error message. This method should be overridden
        in subclasses to provide the area calculation.
    integer_validator(self, name, value):
        Validates whether the value is an integer and greater than 0, otherwise it raises an error.

class Rectangle(BaseGeometry):
    This class represents a rectangle, a subclass of BaseGeometry.

    Methods:
    __init__(self, width, height):
        Initializes the Rectangle object with given width and height.
    area(self):
        Returns the area of the rectangle.
    __str__(self):
        Returns a formatted string representation of the Rectangle's dimensions.
"""

class TypeMetaClass(type):
    """
    This is a metaclass used to represent the class type inorder to eliminate
    the inherited method init subclass
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']


class BaseGeometry(metaclass=TypeMetaClass):
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

    def integer_validator(self, name, value):
        """
        Function validates whether the value is an integer and
        is greater than 0, otherwise it raises an error
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value


class Rectangle(BaseGeometry):
    """
    This is a sub-class of the baseclass
    """
    def __init__(self, width, height):
        """
        function sets the values width and height and ensures
        """
        super().integer_validator("width", width)
        self._Rectangle__width = width
        super().integer_validator("height", height)
        self._Rectangle__height = height

    def __str__(self):
        """
        Returns a formatted string representation of the Rectangle's dimensions.
        """
        return f"Rectangle(width={self._Rectangle__width}, height={self._Rectangle__height})"