#!/usr/bin/python3

class Base:
    """
    initializing the class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing the class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nb_objects

