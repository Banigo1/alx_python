#Python - Almost a circle 1 - 8
# models/rectangle.py file
# 1. First Rectangle
"""
A class to represent a rectangle.

This class has the following public methods:

* width: Gets the width of the rectangle.
* width: Sets the width of the rectangle.
* height: Gets the height of the rectangle.
* height: Sets the height of the rectangle.
* x: Gets the x-coordinate of the rectangle.
* x: Sets the x-coordinate of the rectangle.
* y: Gets the y-coordinate of the rectangle.
* y: Sets the y-coordinate of the rectangle.

"""

from models.base import Base


class Rectangle(Base):
    """A class to represent a rectangle."""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle."""
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        if width < 0:
            raise ValueError("Width must be non-negative.")
        self._width = width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        if height < 0:
            raise ValueError("Height must be non-negative.")
        self._height = height

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x-coordinate of the rectangle."""
        if x < 0:
            raise ValueError("X-coordinate must be non-negative.")
        self._x = x

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y-coordinate of the rectangle."""
        if y < 0:
            raise ValueError("Y-coordinate must be non-negative.")
        self._y = y





    #  2. Validate attributes
    
        from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
            

#3. Area first

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
            
        # 4. Display #0
        
        from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.height):
          print('#' * self.width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
            
            
            
    # 5. __str__
    
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'[Rectangle] ({id(self)}) {self.width}/{self.height}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Width must be positive')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('Height must be positive')
        self.__height = value
       
        """
        
        Triangle Display
        
        """
        
        # 6. Display #1

class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        elif value <= 0:
            raise ValueError('Width must be positive')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        elif value <= 0:
            raise ValueError('Height must be positive')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('X must be an integer')
        elif value < 0:
            raise ValueError('X must be non-negative')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('Y must be an integer')
        elif value < 0:
            raise ValueError('Y must be non-negative')
        self.__y = value

    def display(self):
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return f"Rectangle ({self.width}, {self.height})"

    # 7. Update #0
    class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id(self)

    def __str__(self):
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        result = ""
        for i in range(self.__y):
            result += "\n"
        for i in range(self.__height):
            result += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(result)

    def update(self, *args):
        if len(args) > 0:
            self.__id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]


    # 8. Update #1
    
    class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id(self)

    def __str__(self):
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        result = ""
        for i in range(self.__y):
            result += "\n"
        for i in range(self.__height):
            result += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(result)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            self.__id = args[0]
        for idx, value in enumerate(args):
            if idx == 1:
                self.__width = value
            if idx == 2:
                self.__height = value
            if idx == 3:
                self.__x = value
            if idx == 4:
                self.__y = value
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.__id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value