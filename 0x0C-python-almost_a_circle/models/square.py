#!/usr/bin/python3
"Defining a class called Square"
from models import Rectangle

class Square(Rectangle):
    "creating the class square"

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        return "[Square] ({0}) {1}/{2} - {3}".format(self.id, self.__x, self.__y, self.__height)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        " Getter / Setter method for the property"

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        "Update method for the instance"
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for i , j in kwargs.items():
                if i == 'id':
                    self.id = j
                elif i == 'size':
                    self.width = j
                    self.height = j
                elif i == 'x':
                    self.x = j
                elif i == 'y':
                    self.y = j
