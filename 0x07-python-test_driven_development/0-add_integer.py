#!/usr/bin/python3
"""
This module contains an add_integer function
"""


def add_integer(a, b=98):
    """
    Add two numbers and return the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int: The sum of the two numbers.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
