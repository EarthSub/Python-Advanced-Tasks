# Create an abstract class called Vehicle that should have abstract methods drive and refuel.
# Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulate driving and refueling them.
# Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization.
# They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel).
# It is summer, so both vehicles use air conditioners, and their fuel consumption per km when
# driving is increased by 0.9 liters for the car and 1.6 liters for the truck.
# Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel.
# The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.


#                                 Examples

# Test Code                                                       Output

# car = Car(20, 5)                                                2.299999999999997
# car.drive(3)                                                    12.299999999999997
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

# Test Code                                                       Output

# truck = Truck(100, 15)                                          17.0
# truck.drive(5)                                                  64.5
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)



from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption


    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass



class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_LEAK = 0.95

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_LEAK








car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
