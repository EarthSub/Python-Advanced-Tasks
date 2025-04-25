# Create a class called Glass. Upon initialization, it will not receive any parameters.
# You must create an instance attribute called content which should be equal to 0.
# You should also create a class attribute called capacity which should be 250 ml.
# Create 3 instance methods:

#     - fill(ml) - fills the glass with the given milliliters if there is enough space in it and returns "Glass filled with {ml} ml",
#       otherwise returns "Cannot add {ml} ml"
#     - empty() - empties the glass and returns "Glass is now empty"
#     - info() - returns info about the glass in the format "{space_left} ml left"


#                             Examples

# Test Code                                               Output

# glass = Glass()                                         Glass filled with 100 ml
# print(glass.fill(100))                                  Cannot add 200 ml
# print(glass.fill(200))                                  Glass is now empty
# print(glass.empty())                                    Glass filled with 200 ml
# print(glass.fill(200))                                  50 ml left
# print(glass.info())



class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if self.content + ml <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return f"Glass is now empty"

    def info(self) -> str:
        return f"{Glass.capacity - self.content} ml left"



glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())