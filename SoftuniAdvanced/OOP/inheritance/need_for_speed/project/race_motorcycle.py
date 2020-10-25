from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8


rm = RaceMotorcycle(50, 300)
print(rm.__dict__)
print(rm.drive(5))
print(rm.fuel)