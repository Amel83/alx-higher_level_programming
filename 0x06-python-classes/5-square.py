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

    def area(self):

        """calculates the area of a square
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):

        """returns the current size of the objecy
        Returns:
            size of object
        """
        return self.__size

    @size.setter
    def size(self, value):

        """to reset size of the object with the value passed
        Args:
            value (int): the new size of the square object
        Raises:
            ValueError: value passed < 0
            TypeError: value passed is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):

        """prints the square object
        Returns:
            Nothing
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
