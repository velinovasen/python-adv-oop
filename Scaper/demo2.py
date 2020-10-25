class ChocolateFactory:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type not in ['white chocolate', 'dark chocolate', 'milk chocolate', 'sugar']:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed'
                            f' in {self.__class__.__name__}')
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')
        if ingredient_type in self.ingredients:
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def can_add(self, value):
        return sum([quantity for quantity in self.ingredients.values()]) + value <= self.capacity


import unittest


class ChocoFactoryTests(unittest.TestCase):
    def test_add_ingredient_invalid_input_should_raise_value(self):
        self.ch_f = ChocolateFactory('Paris', 30)
        self.ch_f.add_ingredient('sugar', 20)
        print(self.ch_f.__dict__)
        with self.assertRaises(ValueError):
            self.ch_f.add_ingredient('sugar', 20)

