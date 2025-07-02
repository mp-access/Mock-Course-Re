#!/usr/bin/env python3

# Boilerplate necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
import inspect

# Instead of doing the usual
# import task.script as implementation
# use grading_import which will take care of catching and reporting import errors
implementation = grading_import("task", "script")

# Make sure to inherit from AccessTestCase
class GradingTests(AccessTestCase):

    def test_a_is_1(self):
        self.hint("a should equal 1")
        self.assertEqual(implementation.a, 1)

    def test_b_is_2(self):
        self.hint("b should equal 2")
        self.assertEqual(implementation.b, 2)

    def test_c_is_3(self):
        self.hint("c should equal 3")
        self.assertEqual(implementation.c, 3)

    def test_d_is_4(self):
        self.hint("d should equal 4")
        self.assertEqual(implementation.d, 4)

TestRunner().run(AccessTestSuite(4, [GradingTests]))

