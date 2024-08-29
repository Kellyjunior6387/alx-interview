#!/usr/bin/python3
"""Module to solve the perimeter of an island"""
from typing import List

def search_neighbours(i, j, grid) -> int:
    """Helper function to find if neighbour is land"""
    if i < 0 or i > len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = 2
    search_neighbours(i, j - 1, grid)
    search_neighbours(i - 1, j, grid) 
    search_neighbours(i, j + 1, grid)
    search_neighbours(i + 1, j, grid)
    



def island_perimeter(grid) -> int:
    """Return the number of island in a grid"""
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islands += 1
                search_neighbours(i, j, grid)
    return islands

grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(island_perimeter(grid))
    
