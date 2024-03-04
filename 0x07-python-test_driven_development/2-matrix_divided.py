#!/usr/bin/python3
"""A module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix by a div
    Args:
        matrix: The matrix
        div: The divisor
    Raises:
        ZeroDivisionError: If didvisor is 0
        TypeError: If div is not a float or an int or
                    If matrix is not a list of integers or floats
    Returns:
        The new matrix
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (not isinstance(matrix, list) or matrix == []
        or (not all(isinstance(row, list) for row in matrix))
        or (not all(isinstance(element, (int, float))
        for element in [item for row in matrix for item in row]))):
        raise TypeError("matrix must be a matrix (list of lists)\
    of integers/floats")

    new_matrix = []

    for row in matrix:
        if len(row) == len(matrix[0]):
            new_row = []
            for element in row:
                new_row.append(round(element / div, 2))
            new_matrix.append(new_row)
        else:
            raise TypeError("Each row of the matrix must have the same size")

    return (new_matrix)
