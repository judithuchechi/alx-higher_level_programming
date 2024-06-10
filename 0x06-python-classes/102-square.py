#!/usr/bin/python3
"""This module contains a class Square"""

class Square:
    """This is a geometry class"""
    def __init__(self, size=0):
        """Instantiates an Instance of Square"""
        self.size = size  # This will call the property setter to validate size

    @property
    def size(self):
        """Returns the value for size"""
        return self._size  # Retrieve the private attribute

    @size.setter
    def size(self, value):
        """Validates the valie to be assigned to size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value  # Set the private attribute

    def area(self):
        """Returns the area of the square"""
        return self.size ** 2  # Calculate the square area

    def __eq__(self, other):
        """Defines the == comparison of the square area"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Defines the != comparison of the square area"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """Defines the > comparison of the square area"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Defines the >= comparison of the square area"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """Defines the < comparison of the square area"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Defines the <= comparison of the square area"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

