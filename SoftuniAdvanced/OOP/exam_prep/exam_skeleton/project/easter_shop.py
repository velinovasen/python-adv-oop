from project.factory.paint_factory import PaintFactory
from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory


class EasterShop:

    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()

    def add_chocolate_ingredient(self, type: str, quantity: int):
        choc_fac.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        egg_fac.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        paint_fac.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe in self.storage:
            self.storage[recipe] += 1
        else:
            self.storage[recipe] = 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.products() and color in self.paint_factory.products():
            if self.egg_factory.products[egg_type] > 0 and self.paint_factory.products[color] > 0:
                self.egg_factory.products[egg_type] -= 1
                self.paint_factory.products[color] -= 1
                key = f'{color} {egg_type}'
                if key in self.storage:
                    self.storage[key] += 1
                else:
                    self.storage[key] = 1
            else:
                raise ValueError(f'Invalid commands')
        else:
            raise ValueError(f'Invalid commands')

    def __repr__(self):
        token = f"Shop name: {self.name}\nShop Storage:\n"
        for key, value in self.storage.items():
            token += f"{key}: {value}\n"
        return token

'''choc_fac = ChocolateFactory('BLG', 30)
egg_fac = EggFactory('Sofia', 20)
paint_fac = PaintFactory('Athens', 20)
big_fac = EasterShop('BIG_FAC', choc_fac, egg_fac, paint_fac)
choc_fac.add_ingredient('sugar', 5)
choc_fac.add_ingredient('white chocolate', 5)
choc_fac.add_recipe('cake', {'cake': {'sugar': 1, 'white chocolate': 2}})
big_fac.make_chocolate('cake')
print(big_fac)
'''