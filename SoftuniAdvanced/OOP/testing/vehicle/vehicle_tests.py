import unittest
from SoftuniAdvanced.OOP.testing.vehicle.vehicle import Car, Truck


class VehicleTest(unittest.TestCase):

    def test_car_fuel_after_drive_should_decrease(self):
        fuel_quantity = 30
        fuel_cons = 5
        car = Car(fuel_quantity, fuel_cons)
        distance = 5
        car.drive(distance)
        expected_fuel = fuel_quantity - (distance * (fuel_cons + 0.9))

        self.assertEqual(car.fuel_quantity, expected_fuel)

    def test_car_fuel_should_increase_after_refuel(self):
        fuel_quantity = 30
        fuel_cons = 5
        car = Car(fuel_quantity, fuel_cons)
        car.refuel(20)
        expected_fuel = 50

        self.assertEqual(car.fuel_quantity, expected_fuel)

    def test_truck_fuel_after_driving_should_decrease(self):
        fuel_quantity = 50
        fuel_cons = 3
        truck = Truck(fuel_quantity, fuel_cons)
        distance = 10
        truck.drive(distance)
        expected_fuel = fuel_quantity - (distance * (fuel_cons + 1.6))

        self.assertEqual(truck.fuel_quantity, expected_fuel)

    def test_truck_fuel_after_refuel_should_increase(self):
        fuel_quantity = 50
        fuel_cons = 10
        truck = Truck(fuel_quantity, fuel_cons)
        truck.refuel(5)
        expected_fuel = fuel_quantity + (5 * 0.95)

        self.assertEqual(truck.fuel_quantity, expected_fuel)

    def test_car_refuel_is_none(self):
        fuel_quantity = 30
        fuel_cons = 5
        car = Car(fuel_quantity, fuel_cons)
        with self.assertRaises(Exception) as ex:
            car.refuel(None)

        self.assertRaises(Exception, ex)

    def test_abc_modul_in_vehicle(self):
        abc_to_check = Car.mro()[2].__class__.__name__[:3]
        expected_result = 'ABC'

        self.assertEqual(abc_to_check, expected_result)


if __name__ == '__main__':
    unittest.main()


