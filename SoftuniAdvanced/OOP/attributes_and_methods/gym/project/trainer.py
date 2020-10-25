
class Trainer:
    t_id = 0

    def __init__(self, name):
        self.name = name
        Trainer.t_id += 1
        self.id = Trainer.t_id

    @staticmethod
    def get_next_id():
        return Trainer.t_id + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
