#!/usr/bin/env python3

from copy import deepcopy
from dataclasses import dataclass

# Example 1
def sort_and_even(numbers, even=True):
    return [n for n in sorted(numbers) if (n % 2 == 0) == even]

# Example 2
@dataclass
class Seed:
    number: int

def pseudorandom_float(seed):
    import random
    random.seed(seed.number)
    return random.random()

# Example 3
@dataclass
class Car:
    make: str
    model: str
    km: float

def drive(car, km):
    return Car(car.make, car.model, car.km + km)

