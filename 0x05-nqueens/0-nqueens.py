#!/usr/bin/python3
"""N-queens problems"""

import sys


def is_safe(board, row, col, n):
    """checking if placing a queen is safe
    Args:
    board: current state of the chessboard
    row: row to check
    col: column to check
    n: size of the board
    """

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col,  -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    """Recursive utility functions
    Args:
    board: current state of the chessboard
    row: row to check
    solutions: solutions to check
    n: size of the board
    """

    if row == n:
        solutions.append(["".join(["Q" if cell == 1 else "." for cell in row])
                          for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def solve_n_queens(n):
    """solving N queens
    Args:
    n(str): size of the board
    """
    if not n.isdigit():
        raise ValueError("N must be a number")

    n = int(n)
    if n < 4:
        raise ValueError("N must be at least 4")

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)

    for sol in solutions:
        for row in sol:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        solve_n_queens(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)
