#!/usr/bin/python3
"module for rectangular model"
class Rectangle:
    """ defining rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None)
        """ initializing rectangle class """
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ ph """
        return self.__width

    @width.setter
    def width(self, width):
        """ ph """
        self.__width = width

    @property
    def height(self):
        """ ph """
        return self.__height

    @height.setter
    def height(self, height):
        """ ph """
        self.__height = height
