#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Recursively calculates the factorial of a given number.

    Parameters:
    n (int): The number for which to compute the factorial.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
