#!/usr/bin/python3
"""Find if all boxes can be unlocked"""
from collections import deque

"""def canUnlockAll(boxes):
    visited_boxes = []
    keys = deque([])
    for key in boxes[0]:
        visited_boxes.append(0)
        keys.append(key)
    while len(keys) != 0:
        for i in boxes[keys[0]]:
            if i not in visited_boxes and i not in keys:
                keys.append(i)
            visited_boxes.append(keys.popleft())
            deque(sorted(keys))
    return len(boxes) == len(visited_boxes)
"""


def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    visited[0] = True

    keys = deque(boxes[0])
    while keys:
        key = keys.popleft()
        if 0 <= key < len(boxes) and not visited[key]:
            visited[key] = True
            for new_key in boxes[key]:
                if not visited[new_key]:
                    keys.append(new_key)

    return all(visited)
