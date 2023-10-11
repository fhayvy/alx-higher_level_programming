#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared_row = [value * value for value in row]
        new_matrix.append(squared_row)
    return new_matrix
