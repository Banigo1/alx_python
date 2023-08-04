#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
 def print_args(arg):
  """Prints the number of and the list of its arguments."""
  args = arg.argv
  num_args = len(args)

  print("Number of arguments:", num_args)
  print("List of arguments:")
  for arg in args:
    print("  ", arg)
  print_args()