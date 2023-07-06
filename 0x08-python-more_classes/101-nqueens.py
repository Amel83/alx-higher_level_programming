#!/usr/bin/python3
"""

nqueens
"""
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the current position.
    """
    # Check if the current position is under attack by any previously placed queen
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Solve the N Queens problem using backtracking.
    """
    # Base case: All queens have been placed
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Solve the N Queens problem for a given value of N.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
