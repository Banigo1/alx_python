#!/usr/bin/python3
def raise_exception_msg(message=""):
  """Raises a name exception with a message.

  Args:
    message: The message to be included in the exception.

  Raises:
    NameError: The exception raised.
  """

  if message == "":
    message = "No message provided."
  raise NameError(message)