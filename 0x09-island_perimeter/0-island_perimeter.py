#!/usr/bin/python3
"""Module to solve the perimeter of an island"""


def search_neighbours(i, j, grid) -> int:
    """Helper function to find if neighbour is land"""
    if i < 0 or i > len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    if grid[i][j] == 1:
        return 1
    else:
        return 0


def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                perimeter -= search_neighbours(i, j - 1, grid)
                perimeter -= search_neighbours(i - 1, j, grid)
                perimeter -= search_neighbours(i, j + 1, grid)
                perimeter -= search_neighbours(i + 1, j, grid)
    return perimeter
