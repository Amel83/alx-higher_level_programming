#!/usr/bin/python3
"""script that displays the body of the response.
"""
import sys
import requests

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

try:
    response = requests.post(url, data=data)
    print("Your email is:", email)
except requests.exceptions.RequestException as e:
    print("Error:", e)
