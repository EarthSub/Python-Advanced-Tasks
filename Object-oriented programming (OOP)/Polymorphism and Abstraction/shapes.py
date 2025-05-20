# Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter.
# Create classes Circle (receives radius upon initialization) and Rectangle
# (receives height and width upon initialization) that implement those methods (returning the result).
# The fields of Circle and Rectangle should be private.

#                                 Examples

# Test Code                                                       Output

# circle = Circle(5)                                              78.53981633974483
# print(circle.calculate_area())                                  31.41592653589793
# print(circle.calculate_perimeter())

# Test Code                                                       Output

# rectangle = Rectangle(10, 20)                                   200
# print(rectangle.calculate_area())                               60
# print(rectangle.calculate_perimeter())


import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass



class Circle(Shape):

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi  * self.__radius

    def __init__(self, radius):
        self.__radius = radius




class Rectangle(Shape):

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __init__(self, height, width):
        self.__height = height
        self.__width = width



circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
