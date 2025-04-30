from unittest import TestCase

from script import a

class PublicTestSuite(TestCase):

    def test_a_is_not_zero(self):
        self.assertGreater(a, 0)

