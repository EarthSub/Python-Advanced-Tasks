from typing import List, Type

from project.animals.animal import Mammal
from project.food import Food, Meat, Fruit, Vegetable


class Mouse(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Fruit, Vegetable]

    @property
    def gaining_weight(self) -> float:
        return 0.1

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def gaining_weight(self) -> float:
        return 0.4

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def gaining_weight(self) -> float:
        return 0.3

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def gaining_weight(self) -> float:
        return 1.0

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
