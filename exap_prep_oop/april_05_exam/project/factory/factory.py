from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        if sum([x for x in self.ingredients.values()]) + value <= self.capacity:
            return True
        else:
            return False

    def __repr__(self):
        token = f"Factory name: {self.name} with capacity {self.capacity}.\n"
        for key, value in self.ingredients.items():
            token += f"{key}: {value}\n"
        return token

