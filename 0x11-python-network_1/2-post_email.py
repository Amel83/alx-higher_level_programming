#!/usr/bin/python3
"""A script that takes in a URL
"""
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", email)
        print(body)
except Exception as e:
    print("Error:", e)
-
