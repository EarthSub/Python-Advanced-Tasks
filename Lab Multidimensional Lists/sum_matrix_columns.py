# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.

# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.

#                                  Examples

# Input                   Output              Input                   Output

# 3, 6                    12                  3, 3                    12
# 7 1 3 3 2 1             10                  1 2 3                   15
# 1 3 9 8 5 6             19                  4 5 6                   18
# 4 6 7 9 1 0             20                  7 8 9
#                         8
#                         7

# Hints

#     · Read matrix sizes.
#     · On the next row lines, read the columns.
#     · Traverse the matrix and sum all elements in each column.
#     · Print the sum and continue with the other columns.


rows, columns = [int(n) for n in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(n) for n in input().split()]
    matrix.append(data)

for col in range(columns):
    sum_columns = 0
    for row in range(rows):
        sum_columns += matrix[row][col]
    print(sum_columns)


