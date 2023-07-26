for a in range(9):
    for b in range(a+1, 10):
        if a==8 and b==9:
            print("{}{}".format(a,b))
        else:
            print("{}{}".format(a,b), end=", ")