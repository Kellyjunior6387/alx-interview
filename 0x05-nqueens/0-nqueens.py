#!/usr/bin/python3
"""Module to solve the nqueens problem"""
import sys
from typing import List


def nqueens(n: int) -> None:
    """
    Function to initailise the board and print the solutions
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_queens(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


def solve_queens(board: List, col: int, n: int, solutions: List) -> bool:
    """
    Function that backtracks and look for possible solutions on the board
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    result = False
    for i in range(n):
        if safe_to_place(board, i, col):
            board[i][col] = 1
            result = solve_queens(board, col+1, n, solutions) or result
            board[i][col] = 0
    return False


def safe_to_place(board: List, row: int, col: int) -> bool:
    """
    Function to check if a board index is safe to place a queen
    """
    for x in range(col):
        if board[row][x] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid input')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except TypeError:
        print("Argument must be an integer")
        sys.exit(1)
    nqueens(n)
