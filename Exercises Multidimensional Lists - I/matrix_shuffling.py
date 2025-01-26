# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.

# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where
# ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.

#     · If the command is valid, you should swap the values at the given indexes and print the matrix at each step
#         (thus, you will be able to check if the operation was performed correctly).
#     · If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
#         or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
#         A negative value makes the coordinates not valid.

# Your program should finish when the command "END" is entered.


#             Examples

# Input                       Output

# 2 3                         5 2 3
# 1 2 3                       4 1 6
# 4 5 6                       Invalid input!
# swap 0 0 1 1                5 4 3
# swap 10 9 8 7               2 1 6
# swap 0 1 1 0
# END

# Input                       Output

# 1 2                         Invalid input!
# Hello World                 World Hello
# 0 0 0 1                     Hello World
# swap 0 0 0 1
# swap 0 1 0 0
# END


def is_valid_position(r1, c1, r2, c2, rs, cs):
    return 0 <= r1 < rs and 0 <= r2 < rs and 0 <= c1 < cs and 0 <= c2 < cs


rows, columns = [int(n) for n in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    command = line.split()

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_valid_position(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


