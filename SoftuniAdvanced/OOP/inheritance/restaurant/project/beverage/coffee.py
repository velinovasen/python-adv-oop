from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):

    def __init__(self, name, price, milliliters, caffeine):
        super().__init__(name, price, milliliters)
        self._caffeine = caffeine
        self.COFFEE_MILLILITERS = 50
        self.COFFEE_PRICE = 3.50

    @property
    def caffeine(self):
        return self._caffeine
