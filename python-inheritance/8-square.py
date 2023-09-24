''' An empty class representing the base geometry.'''


class BaseMetaClass(type):
    """
    overrides.
    """

    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]


class BaseGeometry(metaclass=BaseMetaClass):
    """
    Do nothing: By passing pass.
    """

    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]

    def area(self):
        '''
        Public instance method that raises an Exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Public instance method that validate a value
        Attr:
            name(string): the name string.
            value(int): must be an integer greater than 0.
        '''
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


'''Rectangle class that inherit from BaseGeometry'''


class Rectangle(BaseGeometry):

    '''Initializing with and height'''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


'''Square class'''


class Square(Rectangle):
    '''Initializing size'''

    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

