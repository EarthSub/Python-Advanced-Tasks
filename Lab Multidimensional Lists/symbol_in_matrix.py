# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that,
# you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format:
# "({row}, {col})". It would help if you started searching from the top left.
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".


#                               Examples

# Input                  Output          Input                    Output

# 3                      (2, 1)          4                        4 does not occur in the matrix
# ABC                                    asdd
# DEF                                    xczc
# X!@                                    qwee
# !                                      qefw
#                                        4


n = int(input())

matrix = []

for _ in range(n):
    row_data = list(input())
    matrix.append(row_data)

searching_symbol = input()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searching_symbol:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searching_symbol} does not occur in the matrix")

