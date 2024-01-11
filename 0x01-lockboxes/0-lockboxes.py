#!/usr/bin/python3
def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)
