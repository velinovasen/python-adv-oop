from project.vehicle.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value + self.fuel <= self.fuel_tank:
            self.__fuel += value
        else:
            self.__fuel = self.fuel_tank

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.__fuel -= fuel_needed
            return f"We've enjoyed the travel!"

    def refuel(self, liters):
        amount = liters + self.fuel
        capacity = self.fuel_tank
        mixin_result = self.get_capacity(capacity, amount)
        if isinstance(mixin_result, int) or isinstance(mixin_result, float):
            self.__fuel += liters
            return self.fuel
        return mixin_result

