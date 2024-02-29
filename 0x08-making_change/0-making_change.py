#!/usr/bin/python3
"""performing the making change algorithm"""


def makeChange(coins, total):
    """makeChange function"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return count
