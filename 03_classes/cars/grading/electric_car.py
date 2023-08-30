#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
ElectricCar = grading_import("task.electric_car", "ElectricCar")

class TestElectricCar(AccessTestCase):

    @marks(1)
    def test00_gas_init(self):
        try:
            sut = ElectricCar(123.4, 3.45)
            actual_cur, actual_max = sut.get_battery_status()
        except:
            m = "Unexpected error when checking the battery of an ElectricCar directly after initialization."
            self.fail(m)
        m = "Incorrect result when checking the battery of an ElectricCar directly after initialization."
        self.assertAlmostEqual(123.4, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(123.4, actual_max, delta=0.001, msg=m)

    @marks(1)
    def test01_remaining_range(self):
        try:
            sut = ElectricCar(12.0, 24.0)
            actual = sut.get_remaining_range()
            expected = 24.0
        except:
            m = "Unexpected error when checking the remaining range of an ElectricCar with a full battery."
            self.fail(m)
        m = "Incorrect result when checking the remaining range of an ElectricCar with a full battery."
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    @marks(1)
    def test02_drive(self):
        try:
            sut = ElectricCar(10.0, 500.0)
            sut.drive(100.0)
            actual_cur, actual_max = sut.get_battery_status()
        except:
            m = "Unexpected error when checking the battery of an ElectricCar after a short drive."
            self.fail(m)
        m = "Incorrect result when checking the battery of an ElectricCar after a short drive."
        self.assertAlmostEqual(8.0, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(10.0, actual_max, delta=0.001, msg=m)

    @marks(1)
    def test03_error_drive_wrong_type(self):
        try:
            sut = ElectricCar(1.0, 2.0)
            sut.drive("")
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-float to 'ElectricCar.drive'."
            self.fail(m)
        else:
            m = "Passing a non-float to 'ElectricCar.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test04_error_drive_too_small(self):
        try:
            sut = ElectricCar(1.0, 2.0)
            sut.drive(-1.0)
        except Warning:
            return
        except:
            m = "Unexpected error when passing a negative distance to 'ElectricCar.drive'."
            self.fail(m)
        else:
            m = "Passing a negative distance to 'ElectricCar.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test05_error_drive_too_far(self):
        try:
            sut = ElectricCar(10.0, 100.0)
            sut.drive(100.1)
        except Warning:
            return
        except:
            m = "Unexpected error when driving an ElectricCar until the battery is depleted."
            self.fail(m)
        else:
            m = "Driving an ElectricCar until the battery is depleted should raise a Warning."
            self.fail(m)

    @marks(1)
    def test06_error_drive_too_far_depletes_gas_tank(self):
        try:
            sut = ElectricCar(10.0, 100.0)
            sut.drive(100.1)
        except:
            pass
        else:
            self.fail("Depleting the battery in an ElectricCar does not raise an exception.")
        try:
            actual = sut.get_battery_status()
        except:
            self.fail("Failed to get battery status of an ElectricCar after fully depleting the battery.")
        m = "Driving a ElectricCar until the battery is depleted should set the battery charge level to 0."
        self.assertEqual((0, 10), actual, m)

    @marks(1)
    def test07_charge(self):
        try:
            sut = ElectricCar(10.0, 1000.0)
            sut.drive(150.0)
            sut.charge(1.0)
            actual_cur, actual_max = sut.get_battery_status()
        except:
            m = "Unexpected error when checking the battery of an ElectricCar after driving and charging."
            self.fail(m)
        m = "Incorrect result when checking the battery of an ElectricCar after driving and charging."
        self.assertAlmostEqual(9.5, actual_cur, delta=0.001, msg=m)
        self.assertAlmostEqual(10.0, actual_max, delta=0.001, msg=m)

    @marks(1)
    def test08_error_battery_overcharge(self):
        try:
            sut = ElectricCar(10.0, 200.0)
            sut.drive(100.0)
            sut.charge(5.1)
        except Warning:
            return
        except:
            m = "Unexpected error when overcharging the battery of an ElectricCar after a drive."
            self.fail(m)
        else:
            m = "Overcharging the battery of an ElectricCar after a drive should raise a Warning."
            self.fail(m)

    @marks(1)
    def test09_error_init_capacity_type(self):
        try:
            ElectricCar("", 3.45)
        except Warning:
            return
        except:
            m = "Unexpected error initializing an ElectricCar with a non-float battery capacity."
            self.fail(m)
        else:
            m = "Initializing an ElectricCar with a non-float battery capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test10_error_init_capacity_value(self):
        try:
            ElectricCar(-1.0, 3.45)
        except Warning:
            return
        except:
            m = "Unexpected error initializing an ElectricCar with a non-positive battery capacity."
            self.fail(m)
        else:
            m = "Initializing an ElectricCar with a non-positive battery capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test11_error_init_range_type(self):
        try:
            ElectricCar(123.4, "")
        except Warning:
            return
        except:
            m = "Unexpected error initializing an ElectricCar with a non-float range."
            self.fail(m)
        else:
            m = "Initializing an ElectricCar with a non-float range should raise a Warning."
            self.fail(m)

    @marks(1)
    def test12_error_init_range_value(self):
        try:
            ElectricCar(123.4, -1.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing an ElectricCar with a non-positive range."
            self.fail(m)
        else:
            m = "Initializing an ElectricCar with a non-positive range should raise a Warning."
            self.fail(m)