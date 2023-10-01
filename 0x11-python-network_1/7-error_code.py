#!/usr/bin/python3
"""okay know i am understading this things
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    res = requests.get(u)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
