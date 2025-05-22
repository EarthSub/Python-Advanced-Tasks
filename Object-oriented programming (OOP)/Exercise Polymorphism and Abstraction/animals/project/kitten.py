from abc import ABC

from project.cat import Cat


class Kitten(Cat, ABC):

    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")


    def make_sound(self):
        return "Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
