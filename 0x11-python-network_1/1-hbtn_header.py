#!/usr/bin/python3
"""A script that displays the value of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
