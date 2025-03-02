from unittest import TestCase

from script import x

class PublicTestSuite(TestCase):

    def test_x_is_number(self):
        self.assertGreater(x, 0)

