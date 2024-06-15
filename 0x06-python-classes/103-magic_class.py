#!/usr/bin/python3
"""This module contains the class MagicClass"""
import dis
import math

""" MagicClass: function that works as the """
class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0  # Corresponds to setting __radius to 0 initially
        
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        
        self.__radius = radius  # Set the radius if it's a valid number

    def area(self):
        return self.__radius ** 2 * math.pi  # Calculate area: pi * r^2

    def circumference(self):
        return 2 * math.pi * self.__radius  # Calculate circumference: 2 * pi * r

# Example usage:
# magic = MagicClass(5)
# print(magic.area())  # Should print the area of the circle
# print(magic.circumference())  # Should print the circumference of the circle

