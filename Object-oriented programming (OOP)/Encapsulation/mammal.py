# Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound.
# Create a class attribute called kingdom which should not be accessed outside the class and set it to "animals".
# Create three more instance methods:

#     · make_sound() - returns a string in the format "{name} makes {sound}"
#     · get_kingdom() - returns the private kingdom attribute
#     · info() - returns a string in the format "{name} is of type {type}"


#                                 Examples

# Test Code                                                       Output

# mammal = Mammal("Dog", "Domestic", "Bark")                      Dog makes Bark
# print(mammal.make_sound())                                      animals
# print(mammal.get_kingdom())                                     Dog is of type Domestic
# print(mammal.info())



class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, _type: str, sound: str):
        self.name = name
        self.type = _type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return self.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())