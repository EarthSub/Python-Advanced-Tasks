# Your task is to collect as many eggs as possible.

# On the first line, you will be given a number representing the size of the field.
# In the following few lines, you will be given a field with:

#     · One bunny - randomly placed in it and marked with the symbol "B"
#     · Number of eggs placed at different positions of the field and traps marked with "X"

# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction.
# The bunny can move within the field and cannot go outside its boundaries.
# Do not consider negative indices as valid ones. For more clarifications, see the examples below.

# Note: In some directions, the collected eggs can happen to be zero or a negative number.

# Input

#     · A number representing the size of the field
#     · The matrix representing the field (each position separated by a single space)

# Output

#     · The direction which should be considered as best (lowercase)
#     · The field positions from which we are collecting eggs as lists
#     · The total number of eggs collected

# Constraints

#     · There will NOT be two or more paths consisting of the same total amount of eggs.


#                             Examples

# Input                       Output                  Comment

# 5                           right                   The number of eggs, if the bunny goes up, is equal to 7. If it goes
# 1 3 7 9 11                  [3, 1]                  down = 9, there are no eggs on the left and 87 on the right. That's
# X 5 4 X 63                  [3, 2]                  why the bunny should follow this direction (right) and collect the
# 7 3 21 95 1                 [3, 3]                  eggs provided there.
# B 1 73 4 9                  [3, 4]
# 9 2 33 2 0                  87

# Input                       Output

# 8                           down
# 4 18 9 7 24 41 52 11        [6, 2]
# 54 21 19 X 6 34 75 57       [7, 2]
# 76 67 7 44 76 27 56 37      113
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22


rows = int(input())

matrix = []
bunny = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

the_direction = ""
path = []
eggs_score = float("-inf")

for direction, move in possible_moves.items():
    current_eggs_score = 0
    current_path = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < rows and 0 <= col < rows and matrix[row][col] != "X":
        current_eggs_score += int(matrix[row][col])
        current_path.append([row, col])
        row += move[0]
        col += move[1]

    if current_eggs_score > eggs_score and current_path:
        eggs_score = current_eggs_score
        path = current_path
        the_direction = direction

print(the_direction)
[print(row) for row in path]
print(eggs_score)


