#!/usr/bin/python3
""" class that defines a square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a square from class rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ place holder """
        super().__init__(size, size, x, y, id)
