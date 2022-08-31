#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for list in matrix:
        new_matrix.append([item * item for item in list])
    return (new_matrix)
