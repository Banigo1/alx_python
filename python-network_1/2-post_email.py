#!/usr/bin/python3
"""
This is a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response.

The email must be sent in the variable email
Uses the packages requests and sys
"""
import requests
import sys

def check_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter
    and displays the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the request.
    """
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        response.raise_for_status()

        context = response.text

        print(context)

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    check_email(url, email)


        