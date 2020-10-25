from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    pass


mm = Motorcycle(50, 50)
print(mm.__dict__)