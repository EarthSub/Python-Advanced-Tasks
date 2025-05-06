from project.animal import Animal


class Dog(Animal):

    @staticmethod
    def bark() -> str:
        return "barking..."
