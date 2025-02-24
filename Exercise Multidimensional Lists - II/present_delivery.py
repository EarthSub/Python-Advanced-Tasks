# The presents are ready, and Santa has to deliver them to the kids.

# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape.
# On the following lines, you will receive the matrix, which represents the neighborhood.

# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
# If the cell has an "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked with "V".
# There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".

# Santa can move "up", "down", "left", and "right" with one position each time. These will be the commands that you receive.
# If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid,
# he doesn't drop a present. If the command sends Santa to a cell marked with "C",
# Santa eats cookies and becomes happy and extra generous to all the kids around him*
# (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".

# Note: *around him means on his left, right, upwards, and downwards by one cell.
# In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.

# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.

# Keep in mind that you should check whether all the nice kids received presents.

# Input

#     · On the first line, you are given the integer m - the count of presents
#     · On the second - integer n - the size of the neighborhood
#     · The following n lines hold the values for every row
#     · On each of the following lines you will get a command

# Output

#     · On the first line:
#         o If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
#     · Next, print the matrix.
#     · In the end, print one of these messages:
#         o If he manages to give all the nice kids presents, print: "Good job, Santa! {count_nice_kids} happy nice kid/s."
#         o Otherwise, print: "No presents for {count nice kids} nice kid/s."

# Constraints

#     · The size of the square matrix will be between [2…10].
#     · Santa's position will be marked with an 'S'.
#     · There will always be at least 1 nice kid.
#     · There won't be a case where the cookie is on the border of the matrix.


#                                 Examples


# Input                           Output                                      Comments

# 5                               - - - -                                     Santa has 5 presents. The size of the
# 4                               - - - S                                     matrix is 4. After we receive the matrix,
# - X V -                         - - - -                                     we start reading commands. The first one
# - S - V                         X - - -                                     is "up". The "X" means there is a naughty
# - - - -                         Good job, Santa! 2 happy nice kid/s.        kid, so Santa moves on without dropping
# X - - -                                                                     any presents. Next, he reaches a nice kid
# up                                                                          and drops a present. The "down"
# right                                                                       command moves Santa to an empty cell
# down                                                                        The last command before the "Christmas
# right                                                                       morning" message is "right". Again we
# Christmas morning                                                           have a nice kid. The count of nice kids
#                                                                             reached 2, and we don't have any nice
#                                                                             kids without presents left. So we print the
#                                                                             appropriate message.)

# Input                           Output                                      Comments

# 3                               Santa ran out of presents!                  The commands send Santa to a cell with
# 4                               - - - -                                     a cookie, so all of the kids around him
# - - - -                         V - - -                                     receive presents. He runs out of presents
# V - X -                         - - S -                                     because we have 3 kids there and only 3
# - V C V                         - - - -                                     presents. The program ends, and we
# - - - S                         No presents for 1 nice kid/s.               have 1 nice kid that hasn't received a
# left                                                                        present.
# up


number_of_presents = int(input())
size = int(input())
matrix = [input().split() for _ in range(size)]

nice_kids_gifted = 0
santa_position = 0, 0
nice_kids = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "S":
            santa_position = r, c
        elif matrix[r][c] == "V":
            nice_kids += 1

directions = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}


while number_of_presents:
    command = input()
    if command == "Christmas morning":
        break

    s_row = santa_position[0] + directions[command][0]
    s_col = santa_position[1] + directions[command][1]

    if 0 <= s_row < size and 0 <= s_col < size:
        if matrix[s_row][s_col] == "V":
            nice_kids_gifted += 1
            number_of_presents -= 1
            matrix[s_row][s_col] = "-"
        elif matrix[s_row][s_col] == "C":
            for direction in directions.values():
                n_row = s_row + direction[0]
                n_col = s_col + direction[1]
                if matrix[n_row][n_col] in ["V", "X"] and number_of_presents > 0:
                    number_of_presents -= 1
                    if matrix[n_row][n_col] == "V":
                        nice_kids_gifted += 1
                    matrix[n_row][n_col] = "-"
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = s_row, s_col
        matrix[s_row][s_col] = "S"

nice_kids_not_gifted = nice_kids - nice_kids_gifted
if number_of_presents < 1 and nice_kids_not_gifted > 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)
if nice_kids_not_gifted > 0:
    print(f"No presents for {nice_kids_not_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")
