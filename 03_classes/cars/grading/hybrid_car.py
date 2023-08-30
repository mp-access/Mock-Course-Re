#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here
HybridCar = grading_import("task.hybrid_car", "HybridCar")

class TestHybridCar(AccessTestCase):

    def _assert_resources(self, sut, gas_cur, gas_max, bat_cur, bat_max, m_part):
        try:
            actual_gcur, actual_gmax = sut.get_gas_tank_status()
            actual_bcur, actual_bmax = sut.get_battery_status()
        except:
            m = "Unexpected error when checking gas tank and battery of a Hybrid car after {}."
            m.format(m_part)
            self.fail(m)

        tmp = "Incorrect {} when checking the gas tank of a Hybrid car after {}."
        m = tmp.format("current level", m_part)
        self.assertAlmostEqual(gas_cur, actual_gcur, delta=0.001, msg=m)
        m = tmp.format("maximum level", m_part)
        self.assertAlmostEqual(gas_max, actual_gmax, delta=0.001, msg=m)

        tmp = "Incorrect {} when checking the battery of a Hybrid car after {}."
        m = tmp.format("current level", m_part)
        self.assertAlmostEqual(bat_cur, actual_bcur, delta=0.001, msg=m)
        m = tmp.format("maximum level", m_part)
        self.assertAlmostEqual(bat_max, actual_bmax, delta=0.001, msg=m)


    @marks(1)
    def test00_battery_and_gas_init(self):
        try:
            sut = HybridCar(1.0, 2.0, 3.0, 4.0)
        except:
            m = "Unexpected error when initializing a HybridCar."
            self.fail(m)
        self._assert_resources(sut, 1.0, 1.0, 3.0, 3.0, "initialization")

    @marks(1)
    def test01_remaining_range(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            actual = sut.get_remaining_range()
            expected = 500.0
        except:
            m = "Unexpected error when checking the range of a HybridCar directly after initialization."
            self.fail(m)
        m = "Incorrect result when checking the range of a HybridCar directly after initialization."
        self.assertAlmostEqual(expected, actual, delta=0.001, msg=m)

    @marks(1)
    def test02_drive_battery_implicit(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.drive(100.0)
        except:
            m = "Unexpected error when driving a HybridCar for a short distance (without selecting the mode)."
            self.fail(m)
        self._assert_resources(sut, 24.0, 24.0, 15.0, 30.0, "driving a short distance (without selecting the mode)")

    @marks(1)
    def test03_drive_battery_explicit(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.switch_to_electric()
            sut.drive(100.0)
        except:
            m = "Unexpected error when driving a HybridCar for a short distance in electric mode."
            self.fail(m)
        self._assert_resources(sut, 24.0, 24.0, 15.0, 30.0, "driving a short distance in electric mode")

    @marks(1)
    def test04_drive_combustion(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(100.0)
        except:
            m = "Unexpected error when driving a HybridCar for a short distance in combustion mode."
            self.fail(m)
        self._assert_resources(sut, 16.0, 24.0, 30.0, 30.0, "driving a short distance in combustion mode")

    @marks(1)
    def test05_drive_auto_switch_to_combustion(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(250.0)
        except:
            m = "Unexpected error when driving a HybridCar for a distance on electric that requires a switch to combustion."
            self.fail(m)
        m = "driving a distance on electric that requires a switch to combustion"
        self._assert_resources(sut, 20.0, 24.0, 0.0, 30.0, m)

    @marks(1)
    def test06_drive_auto_switch_to_battery(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(350.0)
        except:
            m = "Unexpected error when driving a HybridCar for a distance on combustion that requires a switch to electric."
            self.fail(m)
        m = "driving a distance on combustion that requires a switch to electric"
        self._assert_resources(sut, 0.0, 24.0, 22.5, 30.0, m)

    @marks(1)
    def test07_drive_error_too_far1_e_c(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(250.0)
            sut.drive(250.1)
        except Warning:
            return
        except:
            m = "Unexpected error when fully depleting both battery and gas tank."
            self.fail(m)
        else:
            m = "Fully depleting both battery and gas tank should raise a Warning."
            self.fail(m)

    @marks(1)
    def test08_drive_error_too_far_c_e(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(350.0)
            sut.drive(150.1)
        except Warning:
            return
        except:
            m = "Unexpected error when fully depleting both battery and gas tank."
            self.fail(m)
        else:
            m = "Fully depleting both battery and gas tank should raise a Warning."
            self.fail(m)

    @marks(1)
    def test09_error_drive_too_far_e(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(500.1)
        except Warning:
            return
        except:
            m = "Unexpected error when fully depleting both battery and gas tank."
            self.fail(m)
        else:
            m = "Fully depleting both battery and gas tank should raise a Warning."
            self.fail(m)

    @marks(1)
    def test10_error_drive_too_far_c(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(500.1)
        except Warning:
            return
        except:
            m = "Unexpected error when fully depleting both battery and gas tank."
            self.fail(m)
        else:
            m = "Fully depleting both battery and gas tank should raise a Warning."
            self.fail(m)

    @marks(1)
    def test11_error_drive_too_far_depletes_everything(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(500.1)
        except:
            pass
        else:
            self.fail("Depleting the battery does not raise an exception.")
        try:
            actual_g = sut.get_gas_tank_status()
            actual_b = sut.get_battery_status()
        except:
            self.fail("Failed to get gas tank status or battery status of a HybridCar after depleting all resources.")
        m = "Driving a HybridCar until all resources are depleted should set the levels of the battery charge and the gas tank to 0."
        self.assertEqual((0, 24), actual_g, m)
        self.assertEqual((0, 30), actual_b, m)

    @marks(1)
    def test12_error_drive_combustion_wrong_type(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive("")
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-float distance to 'Hybrid.drive'."
            self.fail(m)
        else:
            m = "Passing a non-float distance to 'Hybrid.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test13_error_drive_combustion_too_small(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(-1.0)
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-positive distance to 'Hybrid.drive'."
            self.fail(m)
        else:
            m = "Passing a non-positive distance to 'Hybrid.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test14_error_drive_electric_wrong_type(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive("")
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-float distance to 'Hybrid.drive'."
            self.fail(m)
        else:
            m = "Passing a non-float distance to 'Hybrid.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test15_error_drive_electric_too_small(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(-1.0)
        except Warning:
            return
        except:
            m = "Unexpected error when passing a non-positive distance to 'Hybrid.drive'."
            self.fail(m)
        else:
            m = "Passing a non-positive distance to 'Hybrid.drive' should raise a Warning."
            self.fail(m)

    @marks(1)
    def test16_fuel(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(150.0)
            sut.fuel(1.0)
        except:
            m = "Unexpected error when refueling a HybridCar after a short drive in combustion mode."
            self.fail(m)
        m = "after driving a short distance in combustion mode and refueling"
        self._assert_resources(sut, 13.0, 24.0, 30.0, 30.0, m)

    @marks(1)
    def test17_fuel_overfill(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_combustion()
            sut.drive(150.0)
            sut.fuel(12.1)
        except Warning:
            return
        except:
            m = "Unexpected error when over-filling the gas tank of a HybridCar after a short drive in combustion mode."
            self.fail(m)
        else:
            m = "Over-filling the gas tank of a HybridCar after a short drive in combustion mode should raise a Warning."
            self.fail(m)

    @marks(1)
    def test18_charge(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(150.0)
            sut.charge(1.0)
        except:
            m = "Unexpected error when recharging a HybridCar after a short drive in electric mode."
            self.fail(m)
        m = "after driving a short distance in electric mode and recharging"
        self._assert_resources(sut, 24.0, 24.0, 8.5, 30.0, m)

    @marks(1)
    def test19_charge_overcharge(self):
        try:
            sut = HybridCar(24.0, 8.0, 30.0, 200.0)
            sut.switch_to_electric()
            sut.drive(150.0)
            sut.charge(22.6)
        except Warning:
            return
        except:
            m = "Unexpected error when over-charging the battery of a HybridCar after a short drive in electric mode."
            self.fail(m)
        else:
            m = "Over-charging the battery of a HybridCar after a short drive in electric mode should raise a Warning."
            self.fail(m)

    @marks(1)
    def test20_error_init_gas_max_type(self):
        try:
            HybridCar("", 8.0, 30.0, 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-float gas tank capacity."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-float gas tank capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test21_error_init_gas_max_value(self):
        try:
            HybridCar(-1.0, 8.0, 30.0, 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-positive gas tank capacity."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-positive gas tank capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test22_error_init_gas_mileage_type(self):
        try:
            HybridCar(24.0, "", 30.0, 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-float gas mileage."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-float gas mileage should raise a Warning."
            self.fail(m)

    @marks(1)
    def test23_error_init_gas_mileage_value(self):
        try:
            HybridCar(24.0, -1.0, 30.0, 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-positive gas mileage."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-positive gas mileage should raise a Warning."
            self.fail(m)

    @marks(1)
    def test24_error_init_battery_capacity_type(self):
        try:
            HybridCar(24.0, 8.0, "", 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-float battery capacity."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-float battery capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test25_error_init_battery_capacity_value(self):
        try:
            HybridCar(24.0, 8.0, -1.0, 200.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-positive battery capacity."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-positive battery capacity should raise a Warning."
            self.fail(m)

    @marks(1)
    def test26_error_init_battery_range_type(self):
        try:
            HybridCar(24.0, 8.0, 30.0, "")
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-float battery range."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-float battery range should raise a Warning."
            self.fail(m)

    @marks(1)
    def test27_error_init_battery_range_value(self):
        try:
            HybridCar(24.0, 8.0, 30.0, -1.0)
        except Warning:
            return
        except:
            m = "Unexpected error initializing a HybridCar with a non-float battery capacity."
            self.fail(m)
        else:
            m = "Initializing a HybridCar with a non-float battery capacity should raise a Warning."
            self.fail(m)