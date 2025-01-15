# Write a program that:

#     · Records a car number for every car that enters the parking lot
#     · Removes a car number when the car leaves the parking lot

# On the first line, you will receive the number of commands - N.
# On the following N lines, you will receive the direction and
# car('s number in the format: "{direction}, {car_number}".
# The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
# Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".)

# Note: The order in which we print the result does not matter.


#                                  Examples

# Input                   Output              Input                       Output

# 10                      CA2844AA            4                           Parking Lot is Empty
# IN, CA2844AA            CA9999TT            IN, CA2844AA
# IN, CA1234TA            CA2822UU            IN, CA1234TA
# OUT, CA2844AA           CA9876HH            OUT, CA2844AA
# IN, CA9999TT                                OUT, CA1234TA
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU


number_of_cars = int(input())

cars_in_the_parking = set()

for _ in range(number_of_cars):
    action, current_car_number = input().split(", ")
    if action == "IN":
        cars_in_the_parking.add(current_car_number)
    elif action == "OUT":
        cars_in_the_parking.remove(current_car_number)

if cars_in_the_parking:
    print("\n".join(cars_in_the_parking))
else:
    print("Parking Lot is Empty")

