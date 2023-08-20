#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argvlen = len(sys.argv)
    if argvlen == 1:
        print("0 arguments.")
    elif argvlen == 2:
        print("1 argument:")
    elif argvlen > 2:
        print("{} arguments:".format(len(sys.argv) - 1))

    for num, element in enumerate(sys.argv):
        if num > 0:
            print("{}: {}".format(num, element))