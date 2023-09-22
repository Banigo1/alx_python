#!/usr/bin/python3
"""This module has a class and a public
instance method Public instance method:
def area(self): that raises an Exception.


BaseGeometry = __import__('4-base_geometry').BaseGeometry

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ python3 4-main.py
[Exception] area() is not implemented
guillaume@ubuntu:~/$ 
"""
class BaseGeometry():
    """Class BaseGeometry.
    It has a method, area, which is
    not implemented yet.

    """
    # def __init__(self):
    #     pass

    def area(self):
        raise Exception("area() is not implemented")