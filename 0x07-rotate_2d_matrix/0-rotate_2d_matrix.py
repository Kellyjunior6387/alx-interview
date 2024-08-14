#!/usr/bin/python3
"""Module to implement a function that rotate a matrix"""


def transpose(matrix):
    """A helper function to transpose a matrix"""
    visited = []
    rows = len(matrix)
    for i in range(rows):
        for j in range(rows):
            if (i, j) not in visited:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                visited.append((i, j))
                visited.append((j, i))
    return matrix


def rotate_2d_matrix(matrix):
    """A function to rotate a matrix"""
    transposed_matrix = transpose(matrix)
    for row in transposed_matrix:
        row.reverse()
    return transposed_matrix
