#!/usr/bin/python3

def add_integer(a, b=98):
    """
    adds integers
    Args:
    a (int, float): 1st arg
    b (int, gloat): 2nd arg. = 98

    Return:
        sum of 2 integers

    Raise:
    TypeError: if args are not in or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
