#!/usr/bin/env python3

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def scale(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def __str__(self):
        return f"A {self.width}x{self.height} rectangle"

    def __repr__(self):
        return f"Rect({self.width}x{self.height})"

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def scale(self, factor):
        self.side *= factor

    def __str__(self):
        return f"A {self.side}-sided square"

    def __repr__(self):
        return f"Square({self.side})"

