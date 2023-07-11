#!/usr/bin/python3
"""check if object is a class that
inherited """


def inherits_from(obj, a_class):
    """return True if obj is a class that
    inherited """
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
