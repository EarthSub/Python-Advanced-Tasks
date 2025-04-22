# Create a class called Vehicle. Upon initialization, it should receive max_speed (integer, optional; 150 by default) and
# mileage (number). Create an instance variable called gadgets - an empty list by default.


#                                 Examples

# Test Code                                                       Output
#
# car = Vehicle(20)                                               150
# print(car.max_speed)                                            20
# print(car.mileage)                                              []
# print(car.gadgets)                                              ['Hudly Wireless']
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)



class Vehicle:

    def __init__(self, mileage: int, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
