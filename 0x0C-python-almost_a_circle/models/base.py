#!/usr/bin/python3
"""Defines a base model class."""
import jsosn



class Base:
    """ the main class called Base
    Attributes:
        __nb_objects (int): to count
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """'intializes
        Args:
            id (int): identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 

    @statimethod
    def to_json_string(list_dictionaries):
        """ change to json repr"""
        list_dictionaries[]
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethos
    def save_to_file(cls, list_objs):
    """change to file
    
    Args:
        list_objs (list): A list of inherited.
    """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialization

        Args:
            json_string (str): A JSON str.
        Returns:
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied.

        Args:
            **dictionary (dict): pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    def load_from_file(cls):
        """to instantiate list
        Returns:
            list os instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []



        
        




