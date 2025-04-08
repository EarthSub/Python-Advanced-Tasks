# With unwavering precision and bravery, our elite counter-terrorist unit faces dangerous threats,
# neutralizing enemies and defusing danger to keep everyone safe.
# Each mission shows our dedication to protecting innocent lives from terrorists!

# You will be given two, comma and space-separated, integer values,
# representing the dimensions (N and M) of a map with a rectangular shape.
# Following this, you will receive the N count lines,
# each containing M count characters describing the map's initial layout. See the Examples section.

# The mission of the counter-terrorist is to defuse the bomb successfully. On the way,
# he might have to face some terrorists. When the bomb is defused the mission is accomplished and the counter-terrorist wins!
# The counter-terrorist must complete his mission in 16 seconds, or the bomb will explode.

# The map will contain randomly positioned elements - a counter-terrorist, terrorists, a bomb, and "empty" spaces:

#     · A counter-terrorist will be placed randomly, marked with the letter 'C'
#     · There will be some terrorists placed somewhere on the map, marked with the letter 'T'
#     · There will be a bomb, marked with the letter 'B'
#     · All of the empty positions will be marked with '*'

# Commands are received until:

#     · the counter-terrorist defuses the bomb
#     · OR is killed by a terrorist
#     · OR the bomb explodes

# You will be given commands for the counter-terrorist's movement.
# The move commands will be "left", "right", "up", and "down". A "defuse" command is also possible.

# The counter-terrorist starts moving only if he has enough time. Be careful,
# for every move command 1 second passes! If the time is over, the bomb explodes,
# no matter where the counter-terrorist is positioned, and the program ends.

#     · If he steps on a '*' nothing happens and the program should continue running.
#     · If he steps on a 'B' the bomb is ready to be defused, only if a proper command ("defuse") is received next.
#       If the next command is different than "defuse", the movement continues.
#     · If he steps on a 'T' the counter-terrorist is killed. Both disappear from the map and the position is marked with '*'. The program ends.
#     · If he receives a command to step outside of the map, the counter-terrorist remains in position without taking a step. Time keeps tickin' away!

# The "defuse" command:

#     · If the counter-terrorist is in a position different from the bomb's position, skip the command. 2 seconds have passed.
#     · If the counter-terrorist is placed at the same coordinates as the bomb he starts defusing. The defuse time is 4 seconds:
#         o If he successfully defuses it (there are 0 or more remaining seconds after defusing),
#           the position is marked with 'D', and the program ends.
#         o Else, counter-terrorist is dead. Both, the bomb and counter-terrorist disappear from the map,
#           and the position is marked with 'X'.

# Do not forget to see the Output section, and build the correct result.

# In the end, print the final state of the map, with the counter-terrorist in his starting position.

# Input

#     · On the first line, you are given two integer values,
#       separated by a comma and space – the dimensions (rows, columns) of a rectangular-shaped matrix.
#     · The next rows count lines contain the values (string format) for every matrix row.
#     · After that, you will get commands (each one on a new line).

# Output

# At the end of the program:

#     · If the bomb has exploded OR the counter-terrorist was defusing and did NOT have enough time,
#       calculate the time needed for successful defuse and print on the console:
#         o "Terrorists win!"
#         o "Bomb was not defused successfully!"
#         o "Time needed: {needed_time_for_bomb_defuse} second/s."
#             § Note: The counter-terrorist defuses the bomb only if the bomb's position is the same as the
#               counter-terrorist position and the command "defuse" is given.
#               The needed time for bomb defuse will be 0 (zero) if the counter-terrorist is not defusing it. See the Examples section.
#     · If the counter-terrorist successfully defused the bomb, track the time left and print on the console:
#         o "Counter-terrorist wins!"
#         o "Bomb has been defused: {remaining_seconds} second/s remaining."
#     · If the counter-terrorist was killed by a terrorist, print on the console:
#         o "Terrorists win!"
#     · Finally, print the matrix in its final state. Remember to put the counter-terrorist in his initial position.

# Constraints

#     · The dimensions of the matrix (map) will be in the range [2…10].
#     · Only the letters 'C', 'T', and 'B' will initially be present on the map.
#     · There will always be enough commands to finish the program.


#                     Examples

# Input                                   Output

# 5, 7                                    Counter-terrorist wins!
# *****T*                                 Bomb has been defused: 2 second/s remaining.
# ****T**                                 *****T*
# **B****                                 ****T**
# ***T**T                                 **D****
# C*****T                                 ***T**T
# up                                      C*****T
# up
# down
# right
# right
# up
# up
# defuse
# down
# defuse

#                     Comment

# The program starts with the counter-terrorist placed at coordinates [4, 0]. The commands are processed as follows:
# up: Moves from [4, 0] to [3, 0], one second passes… 15 seconds left
# up: Moves from [3, 0] to [2, 0], one second passes…14 seconds left
# down: Moves from [2, 0] to [3, 0], one second passes…13 seconds left
# right: Moves from [3, 0] to [3, 1], one second passes…12 seconds left
# right: Moves from [3, 1] to [3, 2], one second passes…11 seconds left
# up: Moves from [3, 2] to [2, 2], one second passes…10 seconds left
# up: Moves from [2, 2] to [1, 2], one second passes…9 seconds left
# defuse: Bomb is not at [1, 2], skip, and 2 seconds pass…7 seconds left
# down: Moves from [1, 2] to [2, 2] -> the bomb's position, one second passes…6 seconds left
# defuse: The counter-terrorist starts defusing the bomb at [2, 2]. The defuse time is 4 seconds. After defusing, 2
# seconds are remaining.
# The bomb is successfully defused, and the final state of the map shows the bomb defused with 'D' at [2, 2].

# Input                                   Output

# 2, 10                                   Terrorists win!
# *TBC*T****                              Bomb was not defused successfully!
# **********                              Time needed: 1 second/s.
# right                                   *TXC*T****
# down                                    *TXC*T**** **********
# right
# right
# right
# right
# left
# left
# left
# left
# left
# left
# up
# defuse

# Input                                   Output

# 5, 5                                    Terrorists win!
# T*C*T                                   T*C*T
# **T**                                   **T**
# T*B*T                                   T*B*T
# **T**                                   **T**
# T***T                                   ****T
# right
# down
# down
# left
# left
# defuse
# down
# down
# down
# down
# left

# Input                                   Output

# 4, 6                                    Terrorists win!
# *C*B**                                  Bomb was not defused successfully!
# ***T**                                  Time needed: 0 second/s.
# *T*TTT                                  *C*B**
# *****T                                  ***T**
# up                                      *T*TTT
# up                                      *****T
# right
# left
# left
# down
# down
# down
# defuse
# defuse
# defuse
# defuse


n, m = [int(x) for x in input().split(", ")]
c_t_position = []
matrix = []
for r in range(n):
    matrix.append(list(input()))
    for c in range(m):
        if matrix[r][c] == "C":
            c_t_position = [r, c]
            break

time = 16
moves = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}

defused = False
killed = False

while time:
    time -= 1
    command = input()

    if command == "defuse":
        if matrix[c_t_position[0]][c_t_position[1]] != "B":
            time -= 1
        else:
            time -= 3
            if time >= 0:
                matrix[c_t_position[0]][c_t_position[1]] = "D"
                defused = True
            else:
                matrix[c_t_position[0]][c_t_position[1]] = "X"
            break

    else:
        new_row = c_t_position[0] + moves[command][0]
        new_col = c_t_position[1] + moves[command][1]

        if 0 <= new_row < n and 0 <= new_col < m:
            if matrix[new_row][new_col] == "T":
                matrix[new_row][new_col] = "*"
                killed = True
                break
            c_t_position = [new_row, new_col]

if defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time} second/s remaining.")
else:
    print("Terrorists win!")
    if not killed:
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(time)} second/s.")

for row in matrix:
    print("".join(row))
