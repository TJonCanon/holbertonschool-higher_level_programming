#!/usr/bin/python3
""" a list that is sorted """


class MyList(list):
    """ produces a list hats sorted """
    def print_sorted(self):
        print(sorted(self))
