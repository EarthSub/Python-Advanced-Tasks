# You are participating in a Firearm course. It is a training day at the shooting range.

# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:

#     · Your position is marked with the symbol "A"
#     · Targets marked with the symbol "x"
#     · All of the empty positions will be marked with "."

# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:

#     · "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
#         You can only move if the field you want to step on is marked with ".".
#     · "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
#         Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
#         When you have shot a target, the field becomes an empty position (".").

# Validate the positions since they can be outside the field.

# Keep track of all the shot targets:

# You are participating in a Firearm course. It is a training day at the shooting range.

# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:

# · Your position is marked with the symbol "A"

# · Targets marked with the symbol "x"

# · All of the empty positions will be marked with "."

# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:

# · "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".

# · "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes an empty position (".").

# Validate the positions since they can be outside the field.

# Keep track of all the shot targets:

#     · If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
#     · If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".

# Finally, print the index positions of the targets that you hit, as shown in the examples.

# Input

#     · 5 lines representing the field (symbols, separated by a single space)
#     · N - count of commands
#     · On the following N lines - the commands in the format described above

# Output

#     · On the first line, print one of the following:
#         o If all the targets were shot
#         "Training completed! All {count_targets} targets hit."
#         o Otherwise:
#         "Training not completed! {count_left_targets} targets left."
#     · Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.

# Constraints

#     · All the commands will be valid
#     · There will always be at least one target


#                 Examples

# Input                               Output

# . . . . .                           Training not completed! 3 targets left.
# x . . . .                           [4, 1]
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# Input                               Output

# . . . . .                           Training completed! All 2 targets hit.
# . . . . .                           [4, 1]
# . A x . .                           [2, 2]
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right

# Input                               Output

# . . . . .                           Training not completed! 1 targets left.
# . . . . .                           [4, 1]
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left


matrix = [input().split() for _ in range(5)]
count_of_commands = int(input())

starting_position = None
targets = 0
targets_hit = []

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "A":
            starting_position = r, c
        if matrix[r][c] == "x":
            targets += 1

directions = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}


for _ in range(count_of_commands):
    command = input().split()
    if command[0] == "shoot":
        row = starting_position[0] + directions[command[1]][0]
        col = starting_position[1] + directions[command[1]][1]

        while 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets -= 1
                targets_hit.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break
    elif command[0] == "move":
        row = starting_position[0] + directions[command[1]][0] * int(command[2])
        col = starting_position[1] + directions[command[1]][1] * int(command[2])
        if 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] == ".":
            matrix[starting_position[0]][starting_position[1]] = "."
            starting_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
for row in targets_hit:
    print(row)

