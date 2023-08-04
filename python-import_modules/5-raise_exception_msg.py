def raise_exception_msg(message=""):
    raise Exception(message)

try:
    raise_exception_msg("c is fun")
except Exception as e:
    print("Exception:", e)

try:
    raise_exception_msg("python is cool")
except Exception as e:
    print("Exception:", e)
