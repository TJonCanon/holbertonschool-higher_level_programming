#!/usr/bin/python3
""" module for rectangular model """
from models.base import Base


class Rectangle(Base):
    """ defining rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing rectangle class """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x <= 0:
            raise ValueError("x must be >= 0")
        if y <= 0:
            raise ValueError("y must be >= 0")
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ place holder """
        return self.__width * self.__height
