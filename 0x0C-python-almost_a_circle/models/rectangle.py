#!/usr/bin/python3
""" module for rectangular model """
from models.base import Base


class Rectangle(Base):
    """ defining rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing rectangle class """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """ returns id, x, y width, height """
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def area(self):
        """ place holder """
        return self.__width * self.__height

    def display(self):
        """ prints out hash shape """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def update(self, *args, **kwargs):
        """ updates rectangle attributes """
        if args is not None and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for number in range(len(args)):
                setattr(self, attr[number], args[number])
