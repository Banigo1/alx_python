# models/rectangle.py
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the constructor of the Base class
        
        # Validate and assign the attributes using setters
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    # Width getter and setter
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive value")
        self.__width = value
    
    # Height getter and setter
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive value")
        self.__height = value
    
    # X getter and setter
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("X must be a non-negative value")
        self.__x = value
    
    # Y getter and setter
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Y must be a non-negative value")
        self.__y = value
