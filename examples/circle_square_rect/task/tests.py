#!/usr/bin/env python3

from unittest import TestCase
from task.script import Square


class TestCars(TestCase):

    def test_square_init(self):
        s = Square(100)
        self.assertEqual(s.side, 100)

