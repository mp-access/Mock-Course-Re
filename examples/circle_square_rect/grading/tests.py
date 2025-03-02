#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here

script = grading_import("task", "script")

class GradingTests(AccessTestCase):

    def test_rect_init(self):
        self.hint("Could not instantiate Rect(100, 200)")
        r = script.Rect(100, 200)

    def test_square_init(self):
        self.hint("Could not instantiate Square(200)")
        r = script.Square(200)

    def test_rect_attributes(self):
        r = script.Rect(100, 200)
        self.hint("A Rect(100, 200) instance should have attributes width = 100 and height = 200")
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 200)

    def test_square_attributes(self):
        r = script.Square(200)
        self.hint("A Square(200) instance should have an attribute side = 200")
        self.assertEqual(r.side, 200)

    def test_rect_area(self):
        r = script.Rect(100, 200)
        self.hint("Could not determine area by calling .area() on a Rect(100, 200) instance")
        actual = r.area()
        expected = 100*200
        self.hint(f"Calling .area() on a Rect(100, 200) instance returned {actual} instead of {expected}")
        self.assertEqual(actual, expected)

    def test_square_area(self):
        r = script.Square(200)
        self.hint("Could not determine area by calling .area() on a Square(200) instance")
        actual = r.area()
        expected = 200**2
        self.hint(f"Calling .area() on a Square(200) instance returned {actual} instead of {expected}")
        self.assertEqual(actual, expected)

    def test_rect_scale(self):
        r = script.Rect(100, 200)
        self.hint("Could not scale Rect(100, 200) by calling .scale(5)")
        r.scale(5)
        self.hint("After scaling a Rect(100, 200) instance by calling .scale(5), width should be 500")
        self.assertEqual(r.width, 500)
        self.hint("After scaling a Rect(100, 200) instance by calling .scale(5), height should be 1000")
        self.assertEqual(r.height, 1000)

    def test_square_scale(self):
        r = script.Square(200)
        self.hint("Could not scale Square(200) by calling .scale(5)")
        r.scale(5)
        self.hint("After scaling a Square(200) instance by calling .scale(5), side should be 1000")
        self.assertEqual(r.side, 1000)

    def test_rect_str(self):
        r = script.Rect(100, 200)
        actual = str(r)
        expected = "A 100x200 rectangle"
        self.hint(f"str(Rect(100, 200)) should return: {expected} but returned: {actual}")
        self.assertEqual(actual, expected)

    def test_square_str(self):
        r = script.Square(200)
        actual = str(r)
        expected = "A 200-sided square"
        self.hint(f"str(Square(200)) should return: {expected} but returned: {actual}")
        self.assertEqual(actual, expected)

    def test_rect_repr(self):
        r = script.Rect(100, 200)
        actual = repr(r)
        expected = "Rect(100x200)"
        self.hint(f"repr(Rect(100, 200)) should return: {expected} but returned: {actual}")
        self.assertEqual(actual, expected)

    def test_square_repr(self):
        r = script.Square(200)
        actual = repr(r)
        expected = "Square(200)"
        self.hint(f"repr(Square(200)) should return: {expected} but returned: {actual}")
        self.assertEqual(actual, expected)

TestRunner().run(AccessTestSuite(1, [GradingTests]))
