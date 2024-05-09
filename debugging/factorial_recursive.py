#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculate the factorial of a given integer.

    Parameters:
        n (int): The integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the integer for which factorial is to be calculated from command-line arguments
# and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)