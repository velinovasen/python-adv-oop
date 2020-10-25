
class Store:
    items = {}

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    @classmethod
    def from_size(cls, name, type, size: int):
        return cls(name, type, size // 2)

    def add_item(self, item_name):
        items_total = sum([int(v) for k, v in self.items.items()])
        if items_total:
            if items_total >= self.capacity:
                return f"Not enough capacity in the store"
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            if self.items[item_name] - amount < 0:
                return f"Cannot remove {amount} {item_name}"
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))