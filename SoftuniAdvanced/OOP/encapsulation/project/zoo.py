from SoftuniAdvanced.OOP.encapsulation.project.keeper import Keeper
from SoftuniAdvanced.OOP.encapsulation.project.caretaker import Caretaker
from SoftuniAdvanced.OOP.encapsulation.project.lion import Lion
from SoftuniAdvanced.OOP.encapsulation.project.tiger import Tiger
from SoftuniAdvanced.OOP.encapsulation.project.vet import Vet
from SoftuniAdvanced.OOP.encapsulation.project.cheetah import Cheetah


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def get_budget(self):
        return self.__budget

    def add_to_budget(self, value):
        self.__budget += value

    def minus_budget(self, value):
        self.__budget -= value

    def get_animal_capacity(self):
        return self.__animal_capacity

    def get_workers_capacity(self):
        return self.__workers_capacity

    def add_animal(self, animal, price):
        if self.get_animal_capacity() > len(self.animals) and self.get_budget() < price:
            return f"Not enough budget"
        if self.get_animal_capacity() > len(self.animals) and self.get_budget() >= price:
            self.animals.append(animal)
            self.minus_budget(price)
            toks = str(type(animal)).split('.')
            tok = toks[-1]
            return f"{animal.name} the {tok[:-2]} added to the zoo"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.get_workers_capacity() > len(self.workers):
            self.workers.append(worker)
            toks = str(type(worker)).split('.')
            tok = toks[-1]
            return f"{worker.name} the {tok[:-2]} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [x for x in self.workers if x.name == worker_name]
        if worker:
            worker = worker[0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([x.salary for x in self.workers])
        if self.get_budget() >= total_salaries:
            self.minus_budget(total_salaries)
            return f"You payed your workers. They are happy. Budget left: {self.get_budget()}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend_sum = sum([x.get_needs() for x in self.animals])
        if self.get_budget() >= total_tend_sum:
            self.minus_budget(total_tend_sum)
            return f"You tended all the animals. They are happy. Budget left: {self.get_budget()}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        return self.add_to_budget(amount)    # POTENTIAL PROBLEM

    def animals_status(self):
        lions = [x for x in self.animals if str(x.__class__).split('.')[-1][:-2] == 'Lion']
        tigers = [x for x in self.animals if str(x.__class__).split('.')[-1][:-2] == 'Tiger']
        cheetahs = [x for x in self.animals if str(x.__class__).split('.')[-1][:-2] == 'Cheetah']
        token = f"You have {len(self.animals)} animals\n" \
                f"----- {len(lions)} Lions:\n"
        lns = [l.__repr__() for l in lions]
        token += '\n'.join(lns)
        token += f"\n----- {len(tigers)} Tigers:\n"
        tgs = [t.__repr__() for t in tigers]
        token += '\n'.join(tgs)
        token += f"\n----- {len(cheetahs)} Cheetahs:\n"
        chts = [c.__repr__() for c in cheetahs]
        token += '\n'.join(chts)
        return token

    def workers_status(self):
        keepers = [x for x in self.workers if str(x.__class__).split('.')[-1][:-2] == 'Keeper']
        caretaker = [x for x in self.workers if str(x.__class__).split('.')[-1][:-2] == 'Caretaker']
        vet = [x for x in self.workers if str(x.__class__).split('.')[-1][:-2] == 'Vet']
        token = f"You have {len(self.workers)} workers\n" \
                f"----- {len(keepers)} Keepers:\n"
        kps = [k.__repr__() for k in keepers]
        token += '\n'.join(kps)
        token += f"\n----- {len(caretaker)} Caretakers:\n"
        cts = [c.__repr__() for c in caretaker]
        token += '\n'.join(cts)
        token += f"\n----- {len(vet)} Vets:\n"
        vts = [v.__repr__() for v in vet]
        token += '\n'.join(vts)
        return token


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
