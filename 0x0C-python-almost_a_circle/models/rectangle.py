#!/usr/bin/python3
"define a class rectangle"
from models.base import Base


class Rectangle(Base):
    "define some attributes and Getter/Setter"

    def __init__(self, width, height, x=0, y=0, id=None):
        "initializing the attributes required"
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        " Getter / Setter method for the property"

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        " Getter / Setter method for the property"

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        " Getter / Setter method for the property"

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        " Getter / Setter method for the property"

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "calculate the area of the rectangle"
        return (self.__width * self.__height)

    def display(self):
        "display the figure of the rectangle"
        for j in range(self.__y):
            print("")
        if (self.__width == 0) or (self.__height == 0):
            print(" " * self.__x, end='')
            return ""
        for i in range(self.__height):
            if i == (self.__height - 1):
                print(" " * self.__x, end='')
                print('#' * self.__width, end='')
                return ""
            print(" " * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    @classmethod
    def rebase(cls, *args):
        cls(*args)

    def update(self, *args, **kwargs):
        "Update method for the instance"
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for i , j in kwargs.items():
                if i == 'id':
                    self.id = j
                elif i == 'width':
                    self.width = j
                elif i == 'height':
                    self.height = j
                elif i == 'x':
                    self.x = j
                elif i == 'y':
                    self.y = j
