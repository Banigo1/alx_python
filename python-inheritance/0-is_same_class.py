"""
This module provides a function to check if an object is exactly an instance of a specified class.

The main function in this module is `is_same_class`, which takes an object and a class as parameters,
and returns True if the object is exactly an instance of the specified class, and False otherwise.

This function does not consider inheritance; it checks for the exact class only. If you want to consider
inheritance, you should use the `isinstance()` function instead. Also, this function does not import any
module as per your request. It uses Python's built-in `type()` function to get the exact class of the object.
This function can be used in a variety of scenarios where you need to check the exact type of an object,
such as in debugging or data validation processes. It's simple, efficient, and easy to use.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to compare with the object's class.

    Returns:
    bool: True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class
