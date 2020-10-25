from project.food.dessert import Dessert


class Cake(Dessert):

    def __init__(self, name):
        self.CAKE_GRAMS = 250
        self.CAKE_CALORIES = 1000
        self.CAKE_PRICE = 5
        super().__init__(name, self.CAKE_PRICE, self.CAKE_GRAMS, self.CAKE_CALORIES)
