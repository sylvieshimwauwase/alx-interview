#!/usr/bin/python3
"""performing lock box documentation"""
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list represents a box.
                               Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Note:
        - A key with the same number as a box opens that box.
        - The first box (boxes[0]) is unlocked.
        - All keys are positive integers.
        - There can be keys that do not have boxes.
    """

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)

    if len(keys) == len(boxes):
        return True
    else:
        return False
