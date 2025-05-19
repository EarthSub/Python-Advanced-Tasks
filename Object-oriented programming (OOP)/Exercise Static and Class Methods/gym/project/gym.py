from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    customers: List[Customer] = []
    trainers: List[Trainer] = []
    equipment: List[Equipment] = []
    plans: List[ExercisePlan] = []
    subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        self.__add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self.__add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)
        return "\n".join([repr(subscription),
                          repr(customer),
                          repr(trainer),
                          repr(equipment),
                          repr(plan)])

    @staticmethod
    def __add_object(obj, collection):
        if obj not in collection:
            collection.append(obj)
