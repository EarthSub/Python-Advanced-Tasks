# Chess is the oldest game, but it is still popular these days.
# You will use only one chess piece for this task - the Knight.

# A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column,
# or diagonal. (e.g., it can move two squares horizontally, then one square vertically,
# or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)

# The knight game is played on a board with dimensions N x N.

# You will receive a board with a "K" for knights and a "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.

# Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.

# Input

#     · On the first line, you will receive integer N - the size of the board
#     · On the following N lines, you will receive strings with "K" and "0"

# Output

#     · Print a single integer with the number of knights that need to be removed.

# Constraints

#     · The size of the board will be 0 < N < 30
#     · Time limit: 0.3 sec. Memory limit: 16 MB


#                                        Examples

# Input           Output          Input           Output          Input           Ouput

# 5               1               2               0               8               12
# 0K0K0                           KK                              0K0KKK00
# K000K                           KK                              0K00KKKK
# 00K00                                                           00K0000K
# K000K                                                           KKKKKK0K
# 0K0K0                                                           K0K0000K
#                                                                 KK00000K
#                                                                 00K0K000
#                                                                 000K00KK


rows = int(input())

matrix = []
knights = []

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < rows and 0 <= next_col < rows:
                if matrix[next_row][next_col] == "K":
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)

