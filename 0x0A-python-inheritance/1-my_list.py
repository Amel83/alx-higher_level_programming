#!/usr/bin/python3
"""inherit from list"""


class MyList(list):
    """ inherit"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
