#!/usr/bin/python3
"""inherits"""


class MyInt(int):
    """MyInt class inherit """
    def __eq__(self, other_int):
        """inverted """
        if self is not other_int:
            return False
        return True

    def __ne__(self, other_int):
        """inverted"""
        if self is other_int:
            return False
        return True
