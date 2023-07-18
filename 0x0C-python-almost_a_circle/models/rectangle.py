#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represent a rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None): 
        """intializes
        Args:
            width (int): side of rec
            height (int): side of re
            x (int): we will sse
            y (int): alright
            id (int): identity
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @propertiy
    def width(self):
        """width setter"""
        return self.__width

    @width.setter
    def width(self, value):
    if type(value) != int:
        raise TypeError("width must be an jnteger")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.width = value
    
    @propertiy
    def height(self):
        """height of rec"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("height must be an int")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = height
    @propertiy
    def x(self):
        """int"""
        return self.__x

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("x must be an int")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @propertiy
    def y(self):
        """int"""
        return self.__y

    @height.setter
    def y(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("y must be an int")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """area"""
        return self.height * self.width
    
    def display(self):
        """ print rec in # symbol"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range(0, height):
            for j in range(0, width):
                print("#", end="")
                width += 1
            print()

        def __str__(self):
        """Return the print() and str() representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x, self.y, self.width, self.height)

    def to_dictionary(self):
    """ repr in __dict__"""

    def to_dictionary(self):
        """Return the __dict__ repr Rec."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }


