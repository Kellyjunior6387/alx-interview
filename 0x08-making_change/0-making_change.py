#!/usr/bin/python3
"""Module to implement the make change problem"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Function that determine fewest number of coins
    to make change
    """
    table = [total+1 for _ in range(total+1)]
    table[0] = 0
    for i in range(1, total+1):
        for coin in coins:
            if (i - coin) > -1:
                table[i] = min(table[i], table[i-coin] + 1)
    return table[total] if table[total] != total+1 else -1
