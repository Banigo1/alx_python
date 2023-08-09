
import sys
sys.setrecursionlimit(10000)
def pow(a, b):
    """Calculates the power of a number.

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The power of the number.
    """

    if b < 0:
      return pow(1 / a, -b + 1)

    elif b < 0:
        return 1 / pow(a, -b + 1)
    else:
        return a * pow(a, b - 1)

if __name__ == "__main__":
  print(pow(2, 3))  # 2^3 = 8
  print(pow(3, 4))  # 3^4 = 81
