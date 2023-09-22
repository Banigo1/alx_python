"""
A function that returns True if the object is an instance of a class that inherited from the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
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
