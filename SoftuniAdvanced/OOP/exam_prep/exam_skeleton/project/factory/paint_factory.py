from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.ingredients = {}

    def add_ingredient(self, ingr, quantity):
        if ingr not in ['white', 'yellow', 'blue', 'green', 'red']:
            raise TypeError(f"Ingredient of type {ingr} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            return ValueError('Not enough space in factory')
        if ingr in self.ingredients:
            self.ingredients[ingr] += quantity
        else:
            self.ingredients[ingr] = quantity

    def remove_ingredient(self, ingr, quantity):
        if ingr in self.ingredients:
            if self.ingredients[ingr] - quantity < 0:
                raise ValueError('Ingredient quantity cannot be less than zero')
            else:
                self.ingredients[ingr] -= quantity
        else:
            raise KeyError("No such product in the factory")

    @property
    def products(self):
        return self.ingredients


'''ch_f = PaintFactory('Paris', 30)
ch_f.add_ingredient('green', 5)
ch_f.add_ingredient('red', 5)
ch_f.add_ingredient('white', 5)
ch_f.add_ingredient('red', 10)
ch_f.add_ingredient('red', 5)
ch_f.remove_ingredient('red', 10)
ch_f.remove_ingredient('white', 2)
print(ch_f.__dict__)'''