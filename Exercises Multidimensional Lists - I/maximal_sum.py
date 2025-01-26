# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements.
# There will be no case with two or more 3x3 squares with equal maximal sum.

# Input

#     · On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
#     · On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]

# Output

#     · On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
#     · On the following 3 lines, print each element of the found submatrix, separated by a single space


#                                  Examples

# Input                   Output              Input                   Output

# 4 5                     Sum = 75            5 6                     Sum = 34
# 1 5 5 2 4               1 4 14              1 0 4 3 1 1             2 5 6
# 2 1 4 14 3              7 11 2              1 3 1 3 0 4             5 4 1
# 3 7 11 2 8              8 12 16             6 4 1 2 5 6             6 0 5
# 4 8 12 16 4                                 2 2 1 5 4 1
#                                             3 3 3 6 0 5



rows, columns = [int(n) for n in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")

max_sub_matrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]

[print(*row) for row in max_sub_matrix]
