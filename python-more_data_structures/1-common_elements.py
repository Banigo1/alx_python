#!/usr/bin/python3
def common_elements(set_1, set_2):

    result = []  # empty list
    
    for element in set_1:  # checks for all elements in set 1 to see if it is also present in set_2.
        
        if element in set_2:  # checks if the current element from set_1 (element)
        # is also present in set_2. If it is, it means that the element is common to both sets.
        
            result.append(element)  # adds matching elements to result.
            
        return result   # returns the result list, which contains all the common 
                        # elements found between set_1 and set_2.

    # return set_1 && set_2 OR return set_1 and set_2 will also work.
    # return set_1.intersection(set_2) can also works in the statement above
