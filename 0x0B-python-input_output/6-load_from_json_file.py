#!/usr/bin/python3
""" creates an object from an "JSON" file. """
import json


def load_from_json_file(filename):
    """ load an object from filename """
    with open(filename, 'r') as the_file:
        return(json.load(the_file))
