# Create a class called Point. Upon initialization, it should receive x and y (numbers). Create 3 instance methods:

#     - set_x(new_x) - changes the x value of the point
#     - set_y(new_y) - changes the y value of the point
#     - __str__() - returns the coordinates of the point in the format "The point has coordinates ({x},{y})"


#                         Examples

# Test Code                                       Output

# p = Point(2, 4)                                 The point has coordinates (2,4)
# print(p)                                        The point has coordinates (3,5)
# p.set_x(3)
# p.set_y(5)
# print(p)



class Point:

    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self,new_x: int):
        self.x = new_x

    def set_y(self,new_y: int):
        self.y = new_y

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"



p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)