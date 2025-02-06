# Create a function called rectangle(). It must have two parameters - length and width.

# First, you need to check if the given arguments are integers:

#     · If one/ both of them is/ are NOT integer/s, return the string "Enter valid values!"

# Create two inner functions:

#     · area() - returns the area of the rectangle with the given length and width
#     · perimeter() - returns the perimeter of the rectangle with the given length and width

# In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle in the following format:

# "Rectangle area: {ract_area}

# Rectangle perimeter: {rect_perim}"


#                         Examples

# Test Code                                       Output

# print(rectangle(2, 10))                         Rectangle area: 20
#                                                 Rectangle perimeter: 24

# Test Code                                       Output

# print(rectangle('2', 10))                       "Enter valid values!"


def rectangle(*args):
    length, width = args[0], args[1]
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2*length + 2*width

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"



print(rectangle(2, 10))
print(rectangle('2', 10))