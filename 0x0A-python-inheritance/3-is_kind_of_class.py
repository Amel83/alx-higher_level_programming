#!/usr/bin/python3
"""check if object class or subclass"""


def is_kind_of_class(obj, a_class):
    """return true is x is a class or inherited class"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
