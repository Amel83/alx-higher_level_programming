#!/usr/bin/python3
"""public instance method"""


class BaseGeometry:
    """public instance method"""
    def area(self):
        """raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """cheque value"""
        x = type(value)
        if x != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle inherits BaseGeometry"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implementing"""
        return self.__width * self.__height

    def __str__(self):
        """return a str representation"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
