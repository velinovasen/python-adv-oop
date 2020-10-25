from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in ["white chocolate", "dark chocolate",
                                   "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} "
                            f"not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type in self.ingredients.keys():
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if ingredient_type in self.ingredients.keys() and self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        good_to_go = True
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")
        for ingr in self.recipes[recipe_name]:
            if self.recipes[recipe_name][ingr] <= self.ingredients[ingr]:
                pass
            else:
                good_to_go = False
        if good_to_go:
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
            for ingr in self.recipes[recipe_name]:
                self.ingredients[ingr] -= self.recipes[recipe_name][ingr]


# ch_f = ChocolateFactory('ChocoFac', 20)
# ch_f.add_ingredient('white chocolate', 2)
# ch_f.add_ingredient('sugar', 2)
# ch_f.add_ingredient('white chocolate', 3)
# ch_f.add_ingredient('sugar', 8)
# ch_f.remove_ingredient('sugar', 10)
# print(ch_f.ingredients)
# ch_f.add_recipe('test_recipe', {"sugar": 2, "white_chocolate": 1})
# ch_f.add_recipe('test_2', {"sugar": 1, "milk chocolate": 1})
# ch_f.add_recipe('test_recipe', {"sugar": 1})
# ch_f.make_chocolate('test_recipe')
# print(ch_f.products)