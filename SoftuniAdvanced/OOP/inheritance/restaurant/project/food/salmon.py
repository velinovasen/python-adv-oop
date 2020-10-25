from project.food.main_dish import MainDish


class Salmon(MainDish):

    def __init__(self, name, price):
        self.SALMON_GRAMS = 22
        super().__init__(name, price, self.SALMON_GRAMS)


