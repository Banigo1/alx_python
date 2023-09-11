#!/usr/bin/python3
def common_elements(set_1, set_2):

    result = []  # empty list
    for element in set_1:  # checks all chars of set 1
        for element in set_2:  # checks all chars of set 2
            result.append(element)  # add matching chars (C) and
    return result                   # adds/appends to result which is returned

#  Below also works in 1 line of code: not positive which and operator works
#  return set_1 && set_2 OR return set_1 and set_2
#  Below also works in 1 line of code
#  return set_1.intersection(set_2)