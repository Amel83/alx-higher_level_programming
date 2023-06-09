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
    @property
    def position(self):
        """Returns the current position of the square objects
        Returns:
            the current position/coordinates of the square object
        """
        return self.__position

    @property
    def position(self):
        """Returns position of the square objects
        Returns:
            the current position square object
        """
        return self.__position
    @position.setter
    def position(self, value):
        """ resets the position of the square object
        Args:
            value (tuple): position defined by tuple of two integers
        Raises:
            ValueError: values passed < 0
            TypeError: passed are not integers or two integers
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def __str__(self):
        """String representationi
        Returns:
            Formatted string representation
        """
        if self.size == 0:
            return ""
        _str = "\n" * self.position[1] + (" " * self.position[0] +
                                          "#" * self.size + "\n") * self.size
        return _str[:-1]
