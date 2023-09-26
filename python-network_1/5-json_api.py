#!/usr/bin/python3
"""
This is a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter is sent in the variable q
If no argument is given, q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
"""
import requests
import sys

def main():
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    parameter = {'q':letter}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=parameter)

    try:
        if response.json():
                print("[{}] {}".format(response.json()['id'], response.json()['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()