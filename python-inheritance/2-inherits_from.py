"""
    This function checks if an object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.
    
"""
def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if obj is an instance of a class that inherited from a_class, 
          False otherwise.
    """
    
    # Check if the object is not an instance of the specified class
    if type(obj) is a_class:
        return False

    # Check if the object is an instance of a subclass of the specified class
    return isinstance(obj, a_class)
