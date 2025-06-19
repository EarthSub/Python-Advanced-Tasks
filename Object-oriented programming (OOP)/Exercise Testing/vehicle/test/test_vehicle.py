

from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 55.5
    horse_power = 155.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(20)
        self.assertEqual(30.5, self.vehicle.fuel)

    def test_drive_error_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(20.5)

        self.assertEqual(21.5, self.vehicle.fuel)

    def test_refuel_error_raises_exception(self):
        self.vehicle.fuel = 50.5

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    main()
