
class Subscription:
    s_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        Subscription.s_id += 1
        self.id = Subscription.s_id

    @staticmethod
    def get_next_id():
        return Subscription.s_id + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
