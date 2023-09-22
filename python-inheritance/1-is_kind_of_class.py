"""
This function uses the built-in isinstance() function in Python,
which checks if an object (obj) is an instance of a class (a_class)
or an instance of a subclass thereof.
If obj is an instance of a_class or any class derived from a_class,
the function will return True. Otherwise, it will return False.

"""
def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to compare with the object's class.

    Returns:
    bool: True if the object is exactly an instance of the specified class, otherwise False.
    """
    return isinstance(obj, a_class)
