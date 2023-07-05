#!/use/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists.
        div (int or float): divisor.

    Returns:
        list: A new matrix with elements divided by `div`.

    Raises:
        TypeError: If `matrix` isn't (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if `div` is not a number.
        ZeroDivisionError: If `div` is equal to zero.
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(not all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

