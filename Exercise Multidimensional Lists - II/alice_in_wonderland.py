# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.

# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:

#     · Alice will be placed in a random position, marked with the letter "A".
#     · On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position,
#         she collects the tea bags and increases the quantity with the corresponding number.
#     · There will always be one rabbit hole on the territory marked with the letter "R".
#     · All of the empty positions will be marked with ".".

# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".

# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting.
# Otherwise, if she steps into the rabbit hole or goes out of the territory, she can't return, and the program ends.

# In the end, the path she walked had to be marked with '*'.

# For more clarifications, see the examples below.

# Input

#     · On the first line, you will be given the integer n – the size of the square matrix
#     · On the following n lines - matrix representing the field (each position separated by a single space)
#     · On each of the following lines, you will be given a move command

# Output

#     · On the first line:
#         o If Alice steps into the rabbit hole or goes out of the territory, print:

# "Alice didn't make it to the tea party."

#         o If she collected at least 10 bags of tea, print:

# "She did it! She went to the party."

#     · On the following lines, print the matrix.

# Constraints

#     · Alice will always either go outside Wonderland or collect 10 bags of tea
#     · All the commands will be valid
#     · All of the given numbers will be valid integers in the range [0, 10]


#                     Examples

# Input                                       Output

# 5                                           Alice didn't make it to the tea party.
# . A . . 1                                   . * . . 1
# R . 2 . .                                   * * * . .
# 4 7 . 1 .                                   4 * . 1 .
# . . . 2 .                                   . . . 2 .
# . 3 . . .                                   . 3 . . .
# down
# right
# left
# down
# up
# left

# Input                                       Output

# 7                                           She did it! She went to the party.
# . A . 1 1 . .                               * * . 1 1 . .
# 9 . . . 6 . 5                               * . . . 6 . 5
# . 6 . R . . .                               * * . R . . .
# . 3 . . 1 . .                               . 3 . . 1 . .
# . . . 2 . . 2                               . . . 2 . . 2
# . 3 . . 1 . .                               . 3 . . 1 . .
# . 8 3 . . . 2                               . 8 3 . . . 2
# left
# down
# down
# right


size = int(input())
matrix = [input().split() for _ in range(size)]

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

alice_position = None
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "A":
            alice_position = (row, col)
            matrix[row][col] = "*"

bags_of_tea = 0

while bags_of_tea < 10:
    alice_current_move = input()
    rd, cd = possible_moves[alice_current_move]
    a_row, a_col = alice_position[0] + rd, alice_position[1] + cd

    if a_row < 0 or a_row >= size or a_col < 0 or a_col >= size:
        break

    cell = matrix[a_row][a_col]
    if cell == "R":
        matrix[a_row][a_col] = "*"
        break

    if cell.isdigit():
        bags_of_tea += int(cell)
        matrix[a_row][a_col] = "*"

    if cell == ".":
        matrix[a_row][a_col] = "*"
    alice_position = [a_row, a_col]


if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
