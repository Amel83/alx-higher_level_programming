#!/usr/bin/python3
"""square"""
from rectangle.py import Rectangle

class Square(Rectangle)
"""square class"""


    def __init__(self, size, x=0, y=0, id=None):
        """initializes
        Attributes:
            size (int): size
            x(int): int
            y (int): int
            id (int): identity """

        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
    """assign value"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return __dict__ repr Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }


