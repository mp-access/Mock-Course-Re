#!/usr/bin/env python3

from copy import deepcopy
from dataclasses import dataclass

# Example 1
def sort_and_even(numbers, even=True):
    numbers.sort()
    return [n for n in numbers if (n % 2 == 0) == even]

# Example 2
@dataclass
class Seed:
    number: int

def pseudorandom_float(seed):
    import random
    random.seed()
    return random.random()

# Example 3
@dataclass
class Car:
    make: str
    model: str
    km: float

def drive(car, km):
    car.km += km
    return car

# The following code is executed when you click "Run"
if __name__ == "__main__":
    # Checking example 1
    numbers = [1, 10, 5, -4, 100, 0]
    numbers_backup = numbers[:]
    expected = sort_and_even(numbers)
    for tries in range(3):
        result = sort_and_even(numbers)
        print(f"sort_and_even referentially transparent: {result == expected}")
    print(f"sort_and_even no side effects: {numbers == numbers_backup}")

    # Checking example 2
    seed = Seed(12345)
    seed_backup = deepcopy(seed)
    expected = pseudorandom_float(seed)
    for tries in range(3):
        result = pseudorandom_float(seed)
        print(f"random_float referentially transparent: {result == expected}")
    print(f"random_float no side effects: {seed == seed_backup}")

    # Checking example 3
    car = Car("Citroen", "BX", 170000)
    car_backup = deepcopy(car)
    expected = drive(car, 999)
    for tries in range(3):
        result = drive(car, 999)
        print(f"drive referentially transparent: {result == expected}")
    print(f"drive no side effects: {car == car_backup}")

