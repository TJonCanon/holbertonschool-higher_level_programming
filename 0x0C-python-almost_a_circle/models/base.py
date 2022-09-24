#!/usr/bin/python3
""" base class """
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_jason_string(list_dictionaries):
        """ static string rep """
        return (
            "[]" if list_dictionaries is None or list_dictionaries is []
            else json.dumps(list_dictionaries)
        )

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a JSON representation of list_objs to a file"""
        list_of_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_dicts.append(obj.to_dictionary())
        with open(cls.__name__+".json", 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_of_dicts))

    @classmethod
    def load_from_file(cls):
        """Creates instances from file, and returns list of instances"""
        try:
            with open(cls.__name__+".json", 'r', encoding="utf-8") as file:
                list_dict = cls.from_json_string(file.read())
            list_inst = []
            for dict in list_dict:
                list_inst.append(cls.create(**dict))
            return list_inst
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Creates new instances from dictionary representation"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
