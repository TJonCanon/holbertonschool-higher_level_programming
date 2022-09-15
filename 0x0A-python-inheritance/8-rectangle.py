#!/usr/bin/python3
""" version of Class BaseGeometry """


class Rectangle(BaseGeometry):
    """ rectangle class inheriting from BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
