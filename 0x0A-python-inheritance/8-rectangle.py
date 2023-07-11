#!/usr/bin/python3
"""inherits BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """raises an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
