import sys
from unittest import TestCase

from task import script

class PublicTests(TestCase):

    def test_contains_Hello(self):
        # This only checks whether the string "Hello" appears in the script
        import inspect
        self.assertIn("Hello", inspect.getsource(script))

