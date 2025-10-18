#!/usr/bin/env python3
from unittest import TestCase
from copy import deepcopy
from task.script import sort_and_even
from task.script import Seed, pseudorandom_float
from task.script import Car, drive


class PublicTestSuite(TestCase):
    def test_sort_and_even_rt(self):
        numbers = [1, 10, 5, -4, 100, 0]
        expected = sort_and_even(numbers)
        for tries in range(10):
            result = sort_and_even(numbers)
            self.assertEqual(result, expected)

    def test_sort_and_even_no_side_effects(self):
        numbers = [1, 10, 5, -4, 100, 0]
        numbers_backup = numbers[:]
        result = sort_and_even(numbers)
        self.assertEqual(numbers, numbers_backup)

    def test_pseudorandom_float_rt(self):
        seed = Seed(12345)
        seed_backup = deepcopy(seed)
        expected = pseudorandom_float(seed)
        for tries in range(3):
            result = pseudorandom_float(seed)
            self.assertEqual(result, expected)

    def test_pseudorandom_no_side_effects(self):
        seed = Seed(12345)
        seed_backup = deepcopy(seed)
        expected = pseudorandom_float(seed)
        self.assertEqual(seed, seed_backup)

    def test_drive_rt(self):
        car = Car("Citroen", "BX", 170000)
        car_backup = deepcopy(car)
        expected = drive(car, 999)
        for tries in range(3):
            result = drive(car, 999)
            self.assertEqual(result, expected)

    def test_drive_no_side_effects(self):
        car = Car("Citroen", "BX", 170000)
        car_backup = deepcopy(car)
        expected = drive(car, 999)
        self.assertEqual(car, car_backup)

