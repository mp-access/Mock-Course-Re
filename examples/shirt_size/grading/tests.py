#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
import unittest

script = grading_import("task", "script")

DELTA = 0.0001

class GradingTests(AccessTestCase):

    def call(self, circumference, suffix=""):
        try:
            return script.get_size(circumference)
        except Exception as e:
            self.hint(f"Solution crashes with '{type(e).__name__}' when called with {circumference}{suffix}".strip())
            self.fail()

    def assertShirtSize(self, circumference, expected):
        actual = self.call(circumference)
        self.hint(f"Your determined size {actual} for a circumference of {circumference} is not correct! The correct size is: {expected}.")
        self.assertEqual(expected, actual)

    def assertShirtSizeFloat(self, circumference, expected):
        suffix = ", which is a floating point number. Are you perhaps using the range() function?"
        actual = self.call(circumference, suffix)
        self.hint(f"Your solution returns {actual} for a circumference of {circumference}{suffix} The correct size is: {expected}")
        self.assertEqual(expected, actual)
 
    def test_XS(self):
        self.assertShirtSize(80, "XS")
        self.assertShirtSize(90, "XS")

    def test_S(self):
        self.assertShirtSize(98, "S")

    def test_M(self):
        self.assertShirtSize(104, "M")

    def test_L(self):
        self.assertShirtSize(111, "L")

    def test_XL(self):
        self.assertShirtSize(124, "XL")

    def test_NA(self):
        self.assertShirtSize(80 - 1, "N/A")
        self.assertShirtSize(124 + 1, "N/A")

    @weight(2)
    def test_floats(self):
        self.assertShirtSizeFloat(80 + DELTA, "XS")
        self.assertShirtSizeFloat(90 - DELTA, "XS")
        self.assertShirtSizeFloat(90 + DELTA, "S")
        self.assertShirtSizeFloat(98 - DELTA, "S")
        self.assertShirtSizeFloat(98 + DELTA, "M")
        self.assertShirtSizeFloat(104 - DELTA, "M")
        self.assertShirtSizeFloat(104 + DELTA, "L")
        self.assertShirtSizeFloat(111 - DELTA, "L")
        self.assertShirtSizeFloat(111 + DELTA, "XL")
        self.assertShirtSizeFloat(124 - DELTA, "XL")
        self.assertShirtSizeFloat(80 - DELTA, "N/A")
        self.assertShirtSizeFloat(124 + DELTA, "N/A")

    @weight(0)
    def test_symptom_one_edge_case_missing(self):
        # naming hard to get right / intuitive
        failures = []

        tests_to_run = [
            self.test_XS,
            self.test_S,
            self.test_M,
            self.test_L,
            self.test_XL,
            self.test_NA
        ]

        for test_func in tests_to_run:
            try:
                test_func()  
            except AssertionError as e:
                failures.append(f"{test_func.__name__}: {e}")

        total_failures = len(failures)
        print(f"TOTAL FAILURE: {total_failures}" )
        self.assertNotEqual(total_failures, 1)


    @weight(0)
    def test_correct_boundary_handling(self):
        self.assertShirtSize(80 - DELTA, "N/A")

        self.assertShirtSize(80 + DELTA, "XS")
        self.assertShirtSize(90 - DELTA, "XS")

        self.assertShirtSize(90 + DELTA, "S")
        self.assertShirtSize(98 - DELTA, "S")

        self.assertShirtSize(98 + DELTA, "M")
        self.assertShirtSize(104 - DELTA, "M")

        self.assertShirtSize(104 + DELTA, "L")
        self.assertShirtSize(111 - DELTA, "L")

        self.assertShirtSize(111 + DELTA, "XL")
        self.assertShirtSize(124 - DELTA, "XL")

        self.assertShirtSize(124 + DELTA, "N/A")

   
    @weight(0)
    def test_handles_floats(self):
        # choose floats that for sure fail bc. they are float, not because of wrong boundaries
        self.assertShirtSizeFloat(82.5, "XS")
        self.assertShirtSizeFloat(92.5, "S")
        self.assertShirtSizeFloat(100.5, "M")
        self.assertShirtSizeFloat(106.5, "L")
        self.assertShirtSizeFloat(113.5, "XL")
        
    @weight(0)
    def test_implementation_runs(self):
        one_circumference_per_size = [81,91,99,105, 112]
        for circumference in one_circumference_per_size:
            self.call(circumference)

TestRunner().run(AccessTestSuite(1, [GradingTests]))
