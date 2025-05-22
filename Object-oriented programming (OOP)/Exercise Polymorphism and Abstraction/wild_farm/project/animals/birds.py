from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def gaining_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gaining_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

