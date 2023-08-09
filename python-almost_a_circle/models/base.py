#!/usr/bin/python3
""" 0-main """
import uuid
class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

        Args:
            id (int, optional): The id of the object. If not provided, an id will be generated.
        """
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int
            Base.__nb_objects += 1
            

from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
    
    
    """
# Create instances of Base
obj1 = Base()
obj2 = Base()
obj3 = Base(id=10)

# Print the ids of the objects
print(obj1.id)  # Output: 1
print(obj2.id)  # Output: 2
print(obj3.id)  # Output: 10

    """