from project.technology.technology import Technology


class Laptop(Technology):

    def install_software(self, software, software_memory):
        capacity = self.memory - self.memory_taken
        mixin_result = self.get_capacity(capacity, software_memory)
        if isinstance(mixin_result, int) or isinstance(mixin_result, float):
            self.memory_taken += software_memory
            return self.memory - self.memory_taken
        return f"You don't have enough space for {software}!"


