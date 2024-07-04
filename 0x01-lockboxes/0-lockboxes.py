#!/usr/bin/python3
"""Function to check if all
boxes can be opened"""
from collections import deque


def canUnlockAll(boxes):
    if not isinstance(boxes, list):
        raise TypeError("Input should be a list of lists")
    n = len(boxes)
    if n == 0:
        return False
    visited = [False] * n
    visited[0] = True
    keys = deque(boxes[0])
    while keys:
        key = keys.popleft()
        if 0 <= key < n and not visited[key]:
            visited[key] = True
            for new_key in boxes[key]:
                if (isinstance(new_key, int) and 0 <= new_key < n and
                        not visited[new_key]):
                    keys.append(new_key)
    return all(visited)
