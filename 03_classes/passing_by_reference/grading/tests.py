#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
from io import StringIO
import inspect, ast
script = grading_import("task", "script")


class GradingTests(AccessTestCase):

    def safe_function_call(self, *args, **kwargs):
        try:
            return script.add_suffix(*args, **kwargs)
        except Exception as e:
            self.hint(f"Tried to call 'add_suffix', but your implementation crashed: {e}")
            self.fail()

    def capture_output(self):
        capture = StringIO()
        sys.stdout = capture
        try:
            self.safe_function_call()
        finally:
            sys.stdout = sys.__stdout__
        return capture.getvalue().strip().splitlines()

    def _implemented(self, funcname):
        func_obj = getattr(script, funcname, None)
        if func_obj is None:
            return False

        import inspect, ast
        source = inspect.getsource(func_obj)
        tree = ast.parse(source)
        func_node = tree.body[0] 

        if not func_node.body:
            return False

        if len(func_node.body) == 1:
            stmt = func_node.body[0]

            if isinstance(stmt, ast.Pass):
                return False

            if isinstance(stmt, ast.Return) and stmt.value is None:
                return False

        return True
    
    def _get_function_params(self, funcname):
        func_obj = getattr(script, funcname, None)
        if func_obj is None:
            return []
        source = inspect.getsource(func_obj)
        tree = ast.parse(source)
        func_node = tree.body[0]
        return [arg.arg for arg in func_node.args.args]

    def test_function_parameters(self):
        self.hint("Your function should take exactly two parameters: a list 'words' and a string 'suffix'.")
        params = self._get_function_params("add_suffix")
        self.assertEqual(len(params), 2)
    
    def test_basic(self):
        self.hint("Your function should modify the list in place by appending the suffix to each word.")
        words = ["cat", "dog"]
        self.safe_function_call(words, "_pet")
        self.assertEqual(words, ["cat_pet", "dog_pet"])

    def test_empty_list(self):
        self.hint("An empty list should remain empty.")
        words = []
        self.safe_function_call(words, "_x")
        self.assertEqual(words, [])

    
    def test_multiple(self):
        self.hint("Each element in the list should have the suffix added.")
        words = ["one", "two", "three", "four", "five", "six"]
        self.safe_function_call(words, "!")
        self.assertEqual(len(words), 6)
        self.assertEqual(words, ["one!", "two!", "three!", "four!", "five!", "six!"])

    def test_no_return_value(self):
        self.hint("Your function should not return anything (should return None).")
        words = ["hello"]
        result = self.safe_function_call(words, "_x")
        self.assertTrue(self._implemented("add_suffix"))
        self.assertIsNone(result)

    def test_in_place(self):
        self.hint("Make sure you modify the list in place, don't reassign a new list.")
        words = ["a", "b"]
        original_id = id(words)
        self.safe_function_call(words, "_z")
        self.assertEqual(id(words), original_id)
        self.assertEqual(words, ["a_z", "b_z"])




TestRunner().run(AccessTestSuite(1, [GradingTests]))
