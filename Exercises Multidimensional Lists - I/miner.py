# You are going to create a game called "Miner".

# First, you will receive the size of a square field in which the miner should move.

# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down".

# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:

#     · * - a regular position on the field
#     · e - the end of the route
#     · c - coal
#     · s - miner

# The miner starts moving from the position "s". He should perform the given commands successively,
# moving with only one position in the given direction. If the miner has reached the edge of the field and
# the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.

# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal.
# In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:

#     · If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
#     · If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
#     · If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".

# Input

#     · Field size - an integer number
#     · Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
#     · The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")


# Output

#     · There are three types of output as mentioned above.

# Constraints

#     · The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
#     · The field will always have only one "s"


#                         Examples

# Input                                               Output

# 5                                                   Game over! (1, 3)
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# Input                                               Output

# 4                                                   You collected all
# up right right right down                           coal! (2, 3)
# * * * e
# * * c *
# * s * c
# * * * *

# Input                                               Output

# 6                                                   3 pieces of coal left.
# left left down right up left left down              (5, 0)
# down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *


size = int(input())
directions = input().split()

matrix = [input().split() for _ in range(size)]

possible_moves = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

total_coal = 0
collected_coal = 0
miner_position = None
no_more_commands = True

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "s":
            miner_position = (row, col)
        elif matrix[row][col] == "c":
            total_coal += 1

for direction in directions:
    new_row = miner_position[0] + possible_moves[direction][0]
    new_col = miner_position[1] + possible_moves[direction][1]

    if 0 <= new_row < size and 0 <= new_col < size:
        miner_position = (new_row, new_col)

        if matrix[new_row][new_col] == "c":
            collected_coal += 1
            matrix[new_row][new_col] = "*"
            if collected_coal == total_coal:
                print(f"You collected all coal! ({new_row}, {new_col})")
                no_more_commands = False
                break
        elif matrix[new_row][new_col] == "e":
            print(f"Game over! ({new_row}, {new_col})")
            no_more_commands = False
            break

if no_more_commands:
    remaining_coal = total_coal - collected_coal
    print(f"{remaining_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")


