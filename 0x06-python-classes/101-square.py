#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represents a square.
    
    Attributes:
        __size (int): side of the square
        --position (tuple): position of the object
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data.
        

        Args:
            size (int): The side length of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position
    def __str__(self):
        """Str method for print from main module.


        Returns:
            str: The string representation of the square.
        """
        my_str = ""
        if self.__size == 0:
            return ''
        else:
            my_str += '\n' * self.__position[1]
            for i in range(0, self.__size):
                my_str += ' ' * self.__position[0]
                my_str += '#' * self.__size
                my_str += '\n'
            return my_str[:-1]

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """reset the position to the square
        

        Args:
            value (tuple): The position of the square as a tuple of 2 positive integers.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of the square.


        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square object

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
            return ''
