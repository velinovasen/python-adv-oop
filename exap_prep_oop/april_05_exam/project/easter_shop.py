from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory,
                 egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type_c: str, quantity: int):
        self.chocolate_factory.add_ingredient(type_c, quantity)

    def add_egg_ingredient(self, type_e: str, quantity: int):
        self.egg_factory.add_ingredient(type_e, quantity)

    def add_paint_ingredient(self, type_p: str, quantity: int):
        self.paint_factory.add_ingredient(type_p, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        if self.chocolate_factory.products[recipe] <= 0:
            pass
        else:
            self.chocolate_factory.products[recipe] -= 1
            if recipe in self.storage.keys():
                self.storage[recipe] += 1
            else:
                self.storage[recipe] = 1

    def paint_egg(self, color: str, egg_type: str):
        if color in self.paint_factory.ingredients and egg_type in self.egg_factory.ingredients:
            if self.paint_factory.ingredients[color] > 0 and self.egg_factory.ingredients[egg_type] > 0:
                self.paint_factory.ingredients[color] -= 1
                self.egg_factory.ingredients[egg_type] -= 1
                key = f"{color} {egg_type}"
                if key not in self.storage:
                    self.storage[key] = 1
                else:
                    self.storage[key] += 1
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        token = f"Shop name: {self.name}\nShop Storage:\n"
        for key, value in self.storage.items():
            token += f"{key}: {value}\n"
        return token


# ch_f = ChocolateFactory('test_choco', 20)
# egg_f = EggFactory('test_egg', 20)
# paint_f = PaintFactory('test_paint', 20)
# easter_shop = EasterShop('test_easter', ch_f, egg_f, paint_f)
#
# easter_shop.add_egg_ingredient('chicken egg', 10)
# easter_shop.add_paint_ingredient('red', 10)
# easter_shop.paint_egg('red', 'chicken egg')
# print(easter_shop.__repr__())