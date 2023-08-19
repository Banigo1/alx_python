#!/usr/bin/python3

from add_0 import add

    """My addition function
         Args:
         a is the first integer
         b is the second integer

    Returns:
        The return value. a + b
    """
 if __name__ == "__main__":
        a = 1
        b = 2
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))