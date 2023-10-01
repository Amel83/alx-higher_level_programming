#!/usr/bin/python3
"""a script sends POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
