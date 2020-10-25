#from SoftuniAdvanced.OOP.inheritance.mix_it.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):

    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        mixin_result = self.get_capacity(self.parking_lots, 1)
        if isinstance(mixin_result, int) or isinstance(mixin_result, float):
            self.parking_lots -= 1
            return f"Parking lots available: {self.parking_lots}"
        return f"There are no more parking lots!"

