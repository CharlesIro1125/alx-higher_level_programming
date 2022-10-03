#!/usr/bin/python3

""" Defines a Rectangle."""

class Rectangle:

    """represent a rectangle"""

    number_of_instances = 0
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if not isinstance(value, int):
                raise(TypeError)
            elif value < 0:
                raise(ValueError)
            self.__width = value
        except (TypeError):
            print("width must be an integer")
        except (ValueError):
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if not isinstance(value, int):
                raise(TypeError)
            elif value < 0:
                raise(ValueError)
            self.__height = value
        except (TypeError):
            print("height must be an integer")
        except (ValueError):
            print("height must be >= 0")
    
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return ((self.__width)*2) + ((self.__height)*2)
    def __str__(self):
        if (self.__width == 0) or (self.__height == 0):
           return ""
        for i in range(self.__height):
            if i == (self.__height - 1):
                print("#" * self.__width, end = '')
                return ""
            print("#" * self.__width)
    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
