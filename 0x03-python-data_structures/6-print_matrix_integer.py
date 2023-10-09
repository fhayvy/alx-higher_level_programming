#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        length = len(matrix[row])
        for col in range(len(matrix[row])):
            if col != (length - 1):
                ending_char = " "
            else:
                ending_char = ""
            print("{:d}".format(matrix[row][col]), end=ending_char)
        print("")
