#!/usr/bin/python3
""" writes an Object to a text file using JSON """
import json


def save_to_json_file(my_obj, filename):
    """ writes my_obj to filenmame using JSON representation """
    with open(filename, 'w', encoding="UTF8") as newFile:
        return json.dump(my_obj, newFile)
