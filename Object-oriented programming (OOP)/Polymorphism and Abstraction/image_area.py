# Create a class called ImageArea which will store the width and the height of an image.
# Create a method called get_area() which will return the area of the image.
# We have also to implement all the magic methods for
# the comparison of two image areas (>, >=, <, <=, ==, !=), which will compare their areas.

#                         Examples

# Test                                                Code Output

# a1 = ImageArea(7, 10)                               True
# a2 = ImageArea(35, 2)                               True
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)

# Test                                                Code Output

# a1 = ImageArea(7, 10)                               False
# a2 = ImageArea(35, 2)                               False
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3

# Test                                                Code Output

# a1 = ImageArea(7, 10)                               True
# a2 = ImageArea(35, 2)                               True
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)


class ImageArea:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()



a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)