#!/usr/bin/python3
import sys


def safe(b, r, c):
    for i in range(r):
        if board[i] == c or b[i] - i == c - r or b[i] + i == c + r:
            return False
    return True

def q(b, r, n):


    if r == n:
        print([[i, b[i]] for i in range(n)])
        return
    
    for col in range(n):
        if safe(b, r, c):
            board[r] = c
            q(b, r + 1, n)

def nq(n):


    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    b = [-1] * n
    q(b, 0, n)

if __name__ == "__main__":


    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        q(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
