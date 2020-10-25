from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        super(EggFactory, self).__init__(name, capacity)
        self.ingredients = {}

    def add_ingredient(self, ingr, quantity):
        if ingr not in ['chicken egg', 'quail egg']:
            raise TypeError(f"Ingredient of type {ingr} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')
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

'''ch_f = EggFactory('Paris', 30)
ch_f.add_ingredient('chicken egg', 3)
ch_f.add_ingredient('chicken egg', 2)
ch_f.add_ingredient('quail egg', 25)
ch_f.remove_ingredient('quail egg', 1)
print(ch_f.__dict__)'''