def raise_exception_msg(message=""):
    raise Exception(message)

try:
    raise_exception_msg("C is fun")
except Exception as e:
    print(e)
