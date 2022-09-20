#!/usr/bin/python3
""" Reads text file and prints it """


def read_file(filename=""):
    """ reads file and prints it """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
