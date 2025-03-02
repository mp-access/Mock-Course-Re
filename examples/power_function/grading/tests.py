#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here

script = grading_import("task", "script")

class GradingTests(AccessTestCase):

    def _test(self, x, y):
        try:
            actual = script.power(x, y)
            expected = x**y
            self.hint(f"Tried to call power({x}, {y}), but your implementation returned {actual} instead of {expected}")
            self.assertAlmostEqual(expected, actual, 5)
        except:
            self.hint(f"Tried to call power({x}, {y}), but your implementation crashed!")
            self.fail()

    def test_power1(self):
        self._test(2, 8)

    def test_power2(self):
        self._test(5, 1)

    def test_power3(self):
        self._test(1, 1)

    def test_call(self):
        import inspect
        source = inspect.getsource(script)
        self.hint("At the end of your script, you should be calling the power function with parameters 2 and 8")
        self.assertTrue("".join(source.split()).endswith("power(2,8)"))

TestRunner().run(AccessTestSuite(1, [GradingTests]))
