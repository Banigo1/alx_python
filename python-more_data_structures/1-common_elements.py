#!/usr/bin/python3
def common_elements(set_1, set_2):

    result = []  # empty list
    for element in set_1:  # checks through all elements of set_1
        if element in set_2:  # checks if the current element from set_1 is also present in set_2
            result.append(element)  # adds matching elements to the result list
    return result  # returns result list, which contains all the common elements found  between set_1 and set_2
