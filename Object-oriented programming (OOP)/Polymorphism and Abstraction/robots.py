# Refactor the provided code (download the zip file from your course resources), so you would not need any type-checking.
# The classes should implement the method to return the number of sensors for each type of robot.

#                                 Examples

# Test Code                                                       Output

# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')

# number_of_robot_sensors(basic_robot)                              1
# number_of_robot_sensors(da_vinci)                                 6
# number_of_robot_sensors(moley)                                    4
# number_of_robot_sensors(griffin)                                  12



class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)