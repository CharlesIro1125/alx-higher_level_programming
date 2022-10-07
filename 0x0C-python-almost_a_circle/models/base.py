#!/usr/bin/python3
"The base model"


class Base:
    "A base class to define the class"

    __nb_objects = 0

    def __init__(self, id=None):
        " Setting parameters for id"

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
