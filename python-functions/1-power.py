
import math
def pow(a, b):
    """Calculates the power of a number.

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The power of the number.
    """

    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b + 1)
    else:
        return a * pow(a, b - 1)
      
# Test the pow() function
if __name__ == "__main__":
  print(pow(2, 3))  # 2^3 = 8
  print(pow(3, 4))  # 3^4 = 81
  print(pow(10, -3))  # 10^-3 = 0.01
