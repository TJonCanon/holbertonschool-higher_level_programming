#!/usr/bin/python3
""" appends text to the end of a file """


def append_write(filename="", text=""):
    """ reads file and prints it """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return(my_file.write(text))
