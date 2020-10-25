#from SoftuniAdvanced.OOP.inheritance.mix_it.project.parking_mall.parking_mall import ParkingMall
from project.parking_mall.parking_mall import ParkingMall


class Level1(ParkingMall):

    def __init__(self):
        super(Level1, self).__init__(150)
