#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of a given size using the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an int or a float < 0.
        ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
            j += 1
        print("")
