#!/usr/bin/python3
"""Defining a Rectangle class."""

class Rectangle:
    """represent a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
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
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__height = value
        except (TypeError):
            print("height must be an integer")
        except (ValueError):
            print("height must be >= 0")
