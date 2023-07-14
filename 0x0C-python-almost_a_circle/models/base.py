#!/usr/bin/python3
"""Defines a base model class."""


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


