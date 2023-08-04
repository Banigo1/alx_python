#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("This is a custom type exception.")
    
    except TypeError as te:
        
        print("Exception raised:", te)