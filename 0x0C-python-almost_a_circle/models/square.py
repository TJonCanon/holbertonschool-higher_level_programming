#!/usr/bin/python3
""" class that defines a square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a square from class rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ place holder """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ defines size of square """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """ updates """
        if args is not None and len(args) != 0:
            a_list = ['id', 'size', 'x', 'y']
            for number in range(len(args)):
                setattr(self, a_list[number], args[number])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary rep of square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
