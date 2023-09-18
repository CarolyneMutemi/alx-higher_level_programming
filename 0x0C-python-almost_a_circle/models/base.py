#!/usr/bin/python3

"""
Has the Base class.
"""
import json
import os


class Base:
    """
    The base of all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries - a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs - a list of instances who inherit from Base.
        """
        with open(f"{cls.__name__}.json", 'w') as file:
            if list_objs is None:
                file.write(Base.to_json_string([]))
            else:
                dic = []
                for i in list_objs:
                    dic.append(i.to_dictionary())
                file.write(Base.to_json_string(dic))

    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        Args:
            json_string - a string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        Args:
            **dictionary - keyword arguments with attributes.
        """
        if cls.__name__ == 'Square':
            dummy = cls(1)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a json file.
        """
        if not os.path.isfile(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", 'r') as file:
            lis = Base.from_json_string(file.read())
            lis1 = []
            for i in lis:
                lis1.append(cls.create(**i))
            return lis1
