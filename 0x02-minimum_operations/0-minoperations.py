#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to produce exactly n 'H' characters.
    """
    # outputs should be at least 2 char: (min, Copy All => Paste)
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        # If n is evenly divisible by root
        if n % root == 0:
            # Total even divisions by root equal total operations
            ops += root
            # Set n to the remainder
            n = n / root
            # Reduce root to find remaining smaller values that evenly divide n
            root -= 1
        # Increment root until it evenly divides n
        root += 1
    return ops
