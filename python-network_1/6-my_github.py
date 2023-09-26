#!/usr/bin/python3
"""
This is a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

Uses Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument is the username
The second argument is the password
(in your case, a personal access token as password)
Uses the package requests and sys
"""
import requests
import sys

def main():
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    parameters = (username, password)

    response = requests.get(url, auth=parameters)
    try:
        print(response.json()['id'])
    except:
        print('None')
if __name__ == "__main__":
    main()