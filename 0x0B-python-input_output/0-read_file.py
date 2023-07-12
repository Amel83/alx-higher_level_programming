#!/usr/bin/python3
"""file-reading function."""


def read_file(filename=""):
    """decode the files"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
