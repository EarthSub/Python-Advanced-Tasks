# We are going to create an AbstractFactory class that will have methods for creating chairs, sofas, and tables:
# Then we are going to create the Chair, Sofa, and Table classes:
# Finally, we are going to create three different factories that will inherit from the AbstractFactiory class:
# VictorianFactory, ModernFactory, FuturisticFactory



from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_chair(self):
        raise NotImplementedError

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError


class Chair:

    def __init__(self, style):
        self.style = style


class Sofa:

    def __init__(self, style):
        self.style = style


class Table:

    def __init__(self, style):
        self.style = style + " dada"


class VictorianFactory(AbstractFactory):
    style = "victorian"

    def create_chair(self):
        return Chair(self.style)

    def create_sofa(self):
        return Sofa(self.style)

    def create_table(self):
        return Table(self.style)


class ModernFactory(AbstractFactory):
    style = "modern"

    def create_chair(self):
        return Chair(self.style)

    def create_sofa(self):
        return Sofa(self.style)

    def create_table(self):
        return Table(self.style)


class FuturisticFactory(AbstractFactory):
    style = "futuristic"

    def create_chair(self):
        return Chair(self.style)

    def create_sofa(self):
        return Sofa(self.style)

    def create_table(self):
        return Table(self.style)
