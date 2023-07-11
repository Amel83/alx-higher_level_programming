#!/usr/bin/python3
"""question 2"""


def is_same_class(obj, a_class):
    """True if the object is an instance ; otherwise False"""
    x = type(obj)
    if x == a_class:
        return True
    return False
