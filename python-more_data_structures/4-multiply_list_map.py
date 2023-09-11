# map is a built-in Python function that applies a specified 
# function to each item in an iterable (like a list) and returns an iterable (like a map object). 
# The map function tha below takes two arguments: my_list, 
# which is a list, and number, which is a number (an integer or float),
# and uses the lambda function to multiply each element in the my_list by the number
# and converts the result back into a list.*/

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda my_list: my_list*number, my_list))