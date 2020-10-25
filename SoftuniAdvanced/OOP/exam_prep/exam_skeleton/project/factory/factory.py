from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    def add_ingredient(self, ingredient_type, quantity):
        pass

    def remove_ingredient(self, ingredient_type, quantity):
        pass

    def can_add(self, value):
        return sum([quantity for quantity in self.ingredients.values()]) + value <= self.capacity




