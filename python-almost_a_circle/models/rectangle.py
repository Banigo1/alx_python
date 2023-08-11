#!/usr/bin/python3
""" module contains the class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class represents a rectangle and inherits from Base

    attributes:
        width: the width of the rectangle
        height: the height of the rectangle
        x: the x coordinate of the rectangle
        y: the y coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ method to define de area of rectangle """
        return self.width * self.height

    def display(self):
        """ prints the instance in stdout with the character # """
        res_str = ""
        res_str += "\n" * self.__y
        for i in range(self.height):
            res_str += (" " * self.x) + ("#" * self.width) + "\n"
        print(res_str[:-1])

    def __str__(self):
        """ returns the string of the object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}" \
            f" - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ assings an argument toeach attribute

        attribute:
            args: attributes to be update in the following
            order

            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """

    def update(self, *args, **kwargs):
        """ method that assigns an argument to each attribute """

        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ the dictionary representation of a rectangle """
        dict_ = {"id": self.id, "width": self.width, "height": self.height,
                 "x": self.x, "y": self.y}
        return dict_