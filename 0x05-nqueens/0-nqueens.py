#!/usr/bin/python3
"""N-queens problems"""

import sys


def print_board(board):
    """ print_board
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def is_safe(board, row, col, n):
    """checking if placing a queen is safe
    Args:
    board: current state of the chessboard
    row: row to check
    col: column to check
    n: size of the board
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col,  -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    """Recursive utility functions
    Args:
    board: current state of the chessboard
    row: row to check
    solutions: solutions to check
    n: size of the board
    """

    if (col == n):
        print_board(board)
        return True
    res = False
    for i in range(n):

        if (is_safe(board, i, col, n)):

            board[i][col] = 1

            res = solve_n_queens_util(board, col + 1, n) or res

            board[i][col] = 0  # BACKTRACK

    return res


def solve_n_queens(n):
    """solving N queens
    Args:
    n(str): size of the board
    """
    board = [[0 for i in range(n)]for i in range(n)]

    if not solve_n_queens_util(board, 0, n):
        return False

    return True


def validate(args):
    """ Validate the input data to verify if the size to
        answer is posible
    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Main method to execute the application
    """

    number = validate(sys.argv)
    solve_n_queens(number)
