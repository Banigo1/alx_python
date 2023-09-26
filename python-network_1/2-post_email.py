import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    try:
        response = requests.post(url, data=payload)
        print("Response Body:")
        print(response.text)
    except requests.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
#!/usr/bin/python3