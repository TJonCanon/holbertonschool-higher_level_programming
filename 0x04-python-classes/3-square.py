#!/usr/bin/python3
"Class that makes a square"


class Square:
    "square class with private size"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size * self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
