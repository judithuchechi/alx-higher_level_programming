#!/usr/bin/python3
'''
1-square.py: Python script that defines square,
   private instantiation attribute of size
'''


class Square:
    ''' creates Square class '''

    def __init__(self, size):
        ''' initializes Suare witb size '''
        self.__size = size
