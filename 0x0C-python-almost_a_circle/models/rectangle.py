#!/usr/bin/python3
"module for rectangular model"
from models.base import Base


class Rectangle(Base):
    """ defining rectangle class """
    def __init__(self, width, height, x=0,
 y=0, id=None):
        """ initializing rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
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

    @property
    def x(self):
        """ ph """
        return self.__x

    @x.setter
    def x(self, x):
        """ ph """
        self.__x = x

    @property
    def y(self):
        """ph """
        return self.__y

    @y.setter
    def y(self, y):
        """ ph """
        self.__y = y

    def __str__(self):
        """ ph """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ ph """
        return self.__width * self.__height
