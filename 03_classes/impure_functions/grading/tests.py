#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
import inspect

implementation = grading_import("task", "script")


class GradingTests(AccessTestCase):
    def test_sort_and_even_no_side_effects(self):
        numbers = [1, 10, 5, -4, 100, 0]
        numbers_backup = numbers[:]
        result = implementation.sort_and_even(numbers)
        self.hint("sort_and_even appears to have side effects")
        self.assertEqual(numbers, numbers_backup)

TestRunner().run(AccessTestSuite(2, [GradingTests]))
