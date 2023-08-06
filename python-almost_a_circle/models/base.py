class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

from models.base import Base

# Create instances of Base
obj1 = Base()
obj2 = Base()
obj3 = Base(id=10)

# Print the ids of the objects
print(obj1.id)  # Output: 1
print(obj2.id)  # Output: 2
print(obj3.id)  # Output: 10
