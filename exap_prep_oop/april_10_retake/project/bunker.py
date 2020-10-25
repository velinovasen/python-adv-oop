from project.medicine.medicine import Medicine
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = [x for x in self.supplies if x.__class__.__name__ == 'FoodSupply']
        if len(food) > 0:
            return food
        else:
            raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water = [x for x in self.supplies if x.__class__.__name__ == 'WaterSupply']
        if len(water) > 0:
            return water
        else:
            raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkillers = [x for x in self.medicine if x.__class__.__name__ == "Painkiller"]
        if len(painkillers) > 0:
            return painkillers
        else:
            raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salves = [x for x in self.medicine if x.__class__.__name__ == 'Salve']
        if len(salves) > 1:
            return salves
        else:
            raise IndexError("There are no salves left!")

    def add_survivor(self, survivor: Survivor):
        # 2 options we should check either by name or by object!!!
        if survivor.name in [x.name for x in self.survivors]:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        medicines_from_same_type = [x for x in self.medicine if x.__class__.__name__ == medicine_type][-1]
        self.medicine.remove(medicines_from_same_type)
        if survivor.needs_healing:
            survivor.health += medicines_from_same_type.health_increase
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            last_supply = self.supplies.pop()
            survivor.needs += last_supply.needs_increase
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        food_supp = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        water_supp = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, food_supp.pop())
            self.sustain(survivor, water_supp.pop())

# bunker = Bunker()
# bunker.add_survivor(Survivor('test', 20))
# bunker.add_supply(FoodSupply())
# bunker.add_supply(FoodSupply())
# bunker.add_supply(FoodSupply())
# bunker.add_supply(WaterSupply())
# bunker.add_supply(WaterSupply())
# print(bunker.food)
# print(bunker.next_day())
# print(bunker.survivors[0].needs)
# print(bunker.survivors[0].needs)
