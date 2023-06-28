#!/usr/bin/python3
""" Documentation for a square class"""


class Square:
    """Represent a square class of quadrilateral with four equal sides
    Attributes:
        __size (int): side of the square
    """
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): side of a square
        Returns:
            None
        Raises:
            ValueError: value passed < than 0
            TypeError: value passed is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
