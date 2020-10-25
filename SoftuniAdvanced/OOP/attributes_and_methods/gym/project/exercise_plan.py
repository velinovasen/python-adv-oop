
class ExercisePlan:
    ep_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        ExercisePlan.ep_id += 1
        self.id = ExercisePlan.ep_id

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.ep_id + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"