#!/usr/bin/python3
raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
    raise_exception_msg("Python is cool")
    raise_exception_msg("")
except NameError as ne:
    print(ne)