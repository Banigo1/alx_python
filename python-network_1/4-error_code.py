#!/usr/bin/python3
"""
This is a Python script that takes in a URL, 
sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, 
print: Error code: followed by the value of the HTTP status code
Uses the packages requests and sys
"""
import requests
import sys

def check_status_code(url):
    """
    Fetches the status from the given URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        context = response.text

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(context)

    except requests.exceptions.RequestException as e:
        print("Error occured:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    check_status_code(url)