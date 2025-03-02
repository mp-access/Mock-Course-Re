#!/usr/bin/env python3

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

class Square:
    pass

class Rect:
    pass

# when you've implemented all three, this function should work:
def do():
    shapes = [Square(10), Square(5), Rect(5, 100), Circle(25)]
    print([shape.area() for shape in shapes])
    print([type(shape) for shape in shapes])
    for shape in shapes:
        shape.scale(3)
    print(shapes)            # uses __repr__
    for shape in shapes:
        print(shape)         # uses __str__

# uncomment to try the function:
#do()
