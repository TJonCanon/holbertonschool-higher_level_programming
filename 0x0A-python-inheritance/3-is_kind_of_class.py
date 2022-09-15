#!/usr/bin/python3
""" object """


def is_kind_of_class(obj, a_class):
    """ is kind of class """
    return(issubclass(type(obj), a_class))
