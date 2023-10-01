#!/usr/bin/python3
"""A script that  takes in a URL
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    u = sys.argv[1]
    v = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(v).encode("ascii")

request = urllib.request.Request(u, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
