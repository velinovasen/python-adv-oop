from project.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self):
        super().__init__(20)

# fs = FoodSupply()
# print(fs.needs_increase)