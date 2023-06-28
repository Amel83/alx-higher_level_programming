#!/use/bin/python3
class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the Square object.

        Args:
            size (int): The side length of the square (default is 0).
        """
        self.size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """int: Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Compares if two squares are equal in area.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the squares are equal in area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if two squares are not equal in area.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compares if the area of the first square is greater than the area of the second square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area of the first square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if the area of the first square is greater than or equal to the area of the second square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area of the first square is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compares if the area of the first square is less than the area of the second square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area of the first square is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if the area of the first square is less than or equal to the area of the second square.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area of the first square is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
