from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}
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

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type in self.ingredients:
            if self.ingredients[ingredient_type] - quantity < 0:
                raise ValueError('Ingredient quantity cannot be less than zero')
            else:
                self.ingredients[ingredient_type] -= quantity
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def add_recipe(self, recipe_name, recipe):
        self.recipes[recipe_name] = recipe[recipe_name]

    def make_chocolate(self, recipe_name):
        be_able_to_cook = True
        if recipe_name in self.recipes:
            for item, quantity in self.recipes[recipe_name].items():
                if item in self.ingredients:
                    if self.ingredients[item] - quantity < 0:
                        be_able_to_cook = False
        else:
            raise TypeError("No such recipe")
        if be_able_to_cook:
            for ingr, quantity in self.recipes[recipe_name].items():
                self.ingredients[ingr] -= quantity
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1


'''ch_f = ChocolateFactory('Paris', 30)
ch_f.add_ingredient('white chocolate', 3)
ch_f.add_ingredient('white chocolate', 2)
ch_f.add_ingredient('sugar', 5)
ch_f.remove_ingredient('white chocolate', 1)
ch_f.add_recipe('bonboni', {'bonboni': {'sugar': 2, 'white chocolate': 3}})
ch_f.add_recipe('cake', {'cake': {'sugar': 2, 'white chocolate': 3}})
ch_f.make_chocolate('cake')
print(ch_f.__dict__)'''

