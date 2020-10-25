from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    # Space in front of Ingredient in the typeError!!!
    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in ["chicken egg", "quail egg"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type in self.ingredients.keys():
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such ingredient in the factory")
        if ingredient_type in self.ingredients.keys() and self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients


# eg_f = EggFactory('test_egg', 20)
# eg_f.add_ingredient('chicken egg', 5)
# eg_f.add_ingredient('quail egg', 5)
# print(eg_f.add_ingredient('quail egg', 11))

