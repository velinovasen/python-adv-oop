class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals_inst = []

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            self.animals_inst.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return f"Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            if animal_name in self.animals_inst:
                self.animals_inst.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals_inst)} animals. " \
               f"{Vet.space - len(Vet.animals)} space left in clinic"

peter = Vet('Peter')
george = Vet('George')
print(george.register_animal('Tom'))
print(george.register_animal('Cory'))
print(peter.register_animal('Fishy'))
print(peter.register_animal('Bobby'))
print(george.register_animal('Kay'))
print(george.unregister_animal('Cory'))
print(peter.register_animal('Silky'))
print(peter.unregister_animal('Molly'))
print(peter.unregister_animal('Tom'))
print(peter.info())
print(george.info())