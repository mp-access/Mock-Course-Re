#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here

class GradingTests(AccessTestCase):

    def test_answer(self):
        import os
        with open("task/answer.txt") as f:
            answer = f.read()
        number_text = "".join(c for c in answer if c.isdigit())
        try:
            number = int(number_text)
        except:
            self.hint("answer.txt should contain a number, but it does not")
            self.fail()
        if number == 2:
            return
        else:
            self.hint("Wrong answer. Hint: x is [y, 1, 2, 3, y] and y is still [4, x, 5]")
            self.fail()

TestRunner().run(AccessTestSuite(1, [GradingTests]))
