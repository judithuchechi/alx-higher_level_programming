#!/usr/bin/python3
'''2-square.py: Defines size as an int and also >= 0'''

class Square:
    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Parameters:
        - size (int): The size of the square (default is 0).

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
