#!/usr/bin/python3
""" checks if object is an 
instance of a class that inherited """


def inherits_from(obj, a_class):
    """ Return: True if obj is instance of a class """
    if type(obj) == a_class:
        return False
    return(issubclass(type(obj), a_class))
