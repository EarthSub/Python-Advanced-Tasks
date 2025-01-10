# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.

# On the first line, you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the following lines, you will be given the names of some people who want to get water
# (each on a separate line) until you receive the command "Start". Add those people to a queue.
# Finally, you will receive some commands until the command "End":

#     - "{liters}" - litters (integer) that the current person in the queue wants to get.
#     Check if there is enough water in the dispenser for that person.
#         o If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#         o Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
#     - "refill {liters}" - add the given litters in the dispenser.

# In the end, print how many liters of water have left in the format: "{left_liters} liters left".


#                         Examples

# Input                   Output                      Comment

# 2                       Peter got water             We create a queue with Peter and Amy. After the start
# Peter                   Amy got water               command, we see that Peter wants 2 liters of water (and
# Amy                     0 liters left               he gets them). The water dispenser is left with 0 liters.
# Start                                               After refilling, there is 1 liter in the dispenser. So when
# 2                                                   Amy wants 1 liter, she gets it, and there are 0 liters left in
# refill 1                                            the dispenser.
# 1
# End

# 10                      Peter got water
# Peter                   George got water
# George                  Amy got water
# Amy                     Alice must wait
# Alice                   2 liters left
# Start
# 2


from collections import deque

queue = deque()
quantity_of_water = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input()
    if command == "End":
        break

    action = command.split()
    if action[0].isdigit():
        if quantity_of_water >= int(action[0]):
            print(f"{queue.popleft()} got water")
            quantity_of_water -= int(action[0])
        else:
            print(f"{queue.popleft()} must wait")
    elif action[0] == "refill":
        quantity_of_water += int(action[1])

print(f"{quantity_of_water} liters left")
