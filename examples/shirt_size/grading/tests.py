#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
from unittest import TestCase

script = grading_import("task", "script")

DELTA = 0.0001

class GradingTests(AccessTestCase):

    def _test(self, circumference, expected):
        self.hint(f"Solution crashes when called with {circumference}")
        actual = script.get_size(circumference)
        self.hint(f"Your determined size {actual} for a circumference of {circumference} is not correct! The correct size is: {expected}.")
        self.assertEqual(expected, actual)

    def test_XS_lower(self):
        self._test(80 - DELTA, "N/A")

    def test_XS(self):
        self._test(80, "XS")

    def test_XS_higher(self):
        self._test(80 + DELTA, "XS")

    def test_S_lower(self):
        self._test(90 - DELTA, "XS")

    def test_S(self):
        self._test(90, "XS")

    def test_S_higher(self):
        self._test(90 + DELTA, "S")

    def test_M_lower(self):
        self._test(98 - DELTA, "S")

    def test_M(self):
        self._test(98, "S")

    def test_M_higher(self):
        self._test(98 + DELTA, "M")

    def test_L_lower(self):
        self._test(104 - DELTA, "M")

    def test_L(self):
        self._test(104, "M")

    def test_L_higher(self):
        self._test(104 + DELTA, "L")

    def test_XL_lower(self):
        self._test(111 - DELTA, "L")

    def test_XL(self):
        self._test(111, "L")

    def test_XL_higher(self):
        self._test(111 + DELTA, "XL")

    def test_XXL_lower(self):
        self._test(124 - DELTA, "XL")

    def test_XXL(self):
        self._test(124, "XL")

    def test_XXL_higher(self):
        self._test(124 + DELTA, "N/A")

TestRunner().run(AccessTestSuite(1, [GradingTests]))
