#!/usr/bin/python3
"""Module to validate utf-8"""
from typing import List


def numberOfBytes(byte: int) -> int:
    if byte & 0b10000000 == 0:
        return 1
    elif byte & 0b11100000 == 0b11000000:
        return 2
    elif byte & 0b11110000 == 0b11100000:
        return 3
    elif byte & 0b11111000 == 0b11110000:
        return 4
    else:
        return 0


def continuation(byte: int) -> int:
    return byte & 0b11000000 == 0b10000000


def validUTF8(data: List[int]) -> bool:
    i = 0
    while i < len(data):
        bytes = numberOfBytes(data[i])
        if bytes == 0:
            return False
        for j in range(1, bytes):
            if i + j >= len(data) or not continuation(i + j):
                return False
        i += bytes
    return True
