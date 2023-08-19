def raise_exception_msg(message):
    raise Exception(message)

try:
    message = "C is fun"
    raise_exception_msg(message)
except Exception as e:
    print(e)
