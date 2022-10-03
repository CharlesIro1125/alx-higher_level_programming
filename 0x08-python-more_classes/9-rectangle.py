#!/usr/bin/python3
""" Defines a Rectangle."""


class Rectangle:
    """represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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
                print(self.print_symbol * self.__width, end='')
                return ""
            print(self.print_symbol * self.__width)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(obj1, obj2):
        if not isinstance(obj1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(obj2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if obj1.area() > obj2.area():
            return obj1
        elif obj1.area() < obj2.area():
            return obj2
        elif obj1.area() == obj2.area():
            return obj1

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
