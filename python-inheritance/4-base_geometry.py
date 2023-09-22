#!/usr/bin/python3
"""
    This is a base class
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
    def __dir__(BaseGeometry) -> None:
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