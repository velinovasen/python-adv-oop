
class Equipment:
    e_id = 0

    def __init__(self, name):
        self.name = name
        Equipment.e_id += 1
        self.id = Equipment.e_id

    @staticmethod
    def get_next_id():
        return Equipment.e_id + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
