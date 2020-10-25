from project.subscription import Subscription
from project.customer import Customer
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer
from project.equipment import Equipment


class Gym:

    def __init__(self, ):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscr = [x for x in self.subscriptions if x.id == subscription_id]
        if subscr:
            subscr = subscr[0]
        customer = [x for x in self.customers if x.id == subscription_id]
        if customer:
            customer = customer[0]
        trainer = [x for x in self.trainers if x.id == subscription_id]
        if trainer:
            trainer = trainer[0]
        plan = [x for x in self.plans if x.trainer_id == trainer.id]
        if plan:
            plan = plan[0]
        equipment = [x for x in self.equipment if x.id == plan.equipment_id]
        if equipment:
            equipment = equipment[0]
        token = f"{repr(subscr)}\n" \
                f"{repr(customer)}\n" \
                f"{repr(trainer)}\n" \
                f"{repr(equipment)}\n" \
                f"{repr(plan)}"
        return token

