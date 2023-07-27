def pow(a, b):
  """Computes a to the power of b and returns the value."""
  if b == 0:
    return 1
  elif b == 1:
    return a
  else:
    return a * pow(a, b - 1)


if __name__ == "__main__":
  print(pow(2, 3))  # 2^3 = 8
  print(pow(3, 4))  # 3^4 = 81
