#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initizing """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area """
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            gives the size in #
        """
        if self.__width == 0 or self.__height == 0:
            return""
        r = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                r += '#'
            r += '\n'
        return r[:-1]

    def __repr__(self):
        """ who knows """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ to delete """
        print("Bye rectangle...")
