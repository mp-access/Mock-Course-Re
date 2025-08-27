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

    def _call(self, circumference):
        try:
            return script.get_size(circumference)
        except:
            self.hint(f"Solution crashes when called with {circumference}")
            self.fail()
 
    def _test(self, circumference, expected):
        actual = self._call(circumference)
        self.hint(f"Your determined size {actual} for a circumference of {circumference} is not correct! The correct size is: {expected}.")
        self.assertEqual(expected, actual)
        
    def test_XS(self):
        self._test(80, "XS")
        self._test(80+DELTA, "XS")
        self._test(90 - DELTA, "XS")
        self._test(90, "XS")

    def test_S(self):
        self._test(90 + DELTA, "S")
        self._test(98 - DELTA, "S")
        self._test(98, "S")

    def test_M(self):
        self._test(98 + DELTA, "M")
        self._test(104 - DELTA, "M")
        self._test(104, "M")

    def test_L(self):
        self._test(104 + DELTA, "L")
        self._test(111 - DELTA, "L")
        self._test(111, "L")

    def test_XL(self):
        self._test(111 + DELTA, "XL")
        self._test(124 - DELTA, "XL")
        self._test(124, "XL")

    
    def test_NA(self):
        self._test(80 - DELTA, "N/A")
        self._test(124 + DELTA, "N/A")
    

    @weight(0)
    def test_correct_or_multiple_sizes_wrong(self):
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
            except Exception as e:
                failures.append(f"{test_func.__name__}: crashed ({type(e).__name__}: {e})")

        total_failures = len(failures)
        print(f"TOTAL FAILURE: {total_failures}" )
        self.assertNotEqual(total_failures, 1) 


    @weight(0)
    def test_correct_boundary_handling(self):
        self._test(80 - DELTA, "N/A")

        self._test(80+DELTA, "XS")        
        self._test(90 - DELTA, "XS")

        self._test(90 + DELTA, "S")
        self._test(98 - DELTA, "S")
        
        self._test(98 + DELTA, "M")
        self._test(104 - DELTA, "M")
        
        self._test(104 + DELTA, "L")
        self._test(111 - DELTA, "L")
        
        self._test(111 + DELTA, "XL")
        self._test(124 - DELTA, "XL")

        self._test(124 + DELTA, "N/A")

    def _check_float_as_input(self, circumference, expected):
        actual = self._call(circumference)
        self.hint(f"Your solution doesn't work for floating point numbers. Your determined size {actual} for a circumference of {circumference} is not correct! The correct size is: {expected}. Are you perhaps using the range() function? ")
        self.assertEqual(expected, actual)
    
    @weight(0)
    def test_handles_floats(self):
        # chose floats that for sure fail bc. they are float, not because of wrong boundaries
        self._check_float_as_input(82.5, "XS")
        self._check_float_as_input(92.5, "S")
        self._check_float_as_input(100.5, "M")
        self._check_float_as_input(106.5, "L")
        self._check_float_as_input(113.5, "XL")
        
    @weight(0)
    def test_implementation_runs(self):
        one_circumference_per_size = [81,91,99,105, 112]
        for circumference in one_circumference_per_size:
            self._call(circumference)

TestRunner().run(AccessTestSuite(1, [GradingTests]))
