# The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice,
# and they're going to have a really good time, but first, they have to get there. Even on his holiday trip,
# Sam is still going to run into some problems, and the first one is getting to the airport. Right now,
# he is stuck in a traffic jam at a crossroads where a lot of accidents happen.

# Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely.

# Sam is on a single lane of cars that queue until the light goes green.
# When it does, they start passing one by one on a flashing green light and
# during the free window before the intersecting road's light goes green. For each second,
# only one part of a car (a single character) passes the crossroad.
# If a car is still in the middle of the crossroads when the free window ends,
# it will get hit at the first character that is still in the crossroads.

# Input

#     · On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
#     · On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
#     · On the following lines, until you receive the "END" command, you will receive one of two things:
#         § A car - a string containing the model of the car, or
#         § The command "green" that indicates the start of a green light cycle

# A green light cycle goes as follows:

#     · During the green light, cars will enter and exit the crossroads one by one
#     · During the free window, cars will only exit the crossroads

# Output

#     · If a crash happens, end the program and print: "A crash happened!" "{car} was hit at {character_hit}."
#     · If everything goes smoothly and you receive an "END" command, print: "Everyone is safe." "{total_cars_passed} total cars passed the crossroads."

# Constraints

#     · The input will be within the constraints specified above and will always be valid. There is no need to check


#                             Examples

# Input                       Output                                          Comments

# 10                          Everyone is safe.                               During the first green light (10 seconds),
# 5                           3 total cars passed the crossroads.             the Mercedes (8) passes safely.
# Mercedes                                                                    During the second green light, the
# green                                                                       Mercedes (8) passes safely, and there
# Mercedes                                                                    are 2 seconds left.
# BMW                                                                         The BMW enters the crossroads, and
# Skoda                                                                       when the green light ends, it still has 1
# green                                                                       part inside ('W') but has 5 seconds to
# END                                                                         leave and passes successfully.
#                                                                             The Skoda never entered the crossroads,
#                                                                             so 3 cars passed successfully.

# Input                       Output                                          Comments

# 9                           A crash happened!                               Mercedes (8) passes successfully, and
# 3                           Hummer was hit at e.                            Hummer (6) enters the crossroads, but
# Mercedes                                                                    only the 'H' passes during the green light.
# Hummer                                                                      There are 3 seconds of a free window, so
# green                                                                       "umm" passes, and the Hummer gets hit
# Hummer                                                                      at 'e', and the program ends with a
# Mercedes                                                                    crash.
# green
# END


from collections import deque


green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
passed_cars = 0
crash = False

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        current_green_time = green_light_duration

        while cars and current_green_time > 0:
            car = cars.popleft()
            car_length = len(car)

            if current_green_time >= car_length:
                current_green_time -= car_length
                passed_cars += 1
            else:
                remaining_time = car_length - current_green_time

                if remaining_time <= free_window_duration:
                    passed_cars += 1
                else:
                    hit_char = car[current_green_time + free_window_duration]
                    print("A crash happened!")
                    print(f"{car} was hit at {hit_char}.")
                    crash = True
                    break

                current_green_time = 0

    else:
        cars.append(command)

    if crash:
        break

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")

