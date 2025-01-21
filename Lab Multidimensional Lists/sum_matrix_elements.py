# Write a program that reads a matrix from the console and prints:

#     · The sum of all numbers in the matrix
#     · The matrix itself

# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".


#                 Examples

# Input                               Output

# 3, 6                                76
# 7, 1, 3, 3, 2, 1                    [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0


data = input().split(", ")
row_count = int(data[0])
col_count = int(data[1])

matrix = []
sum_elements = 0

for row_index in range(row_count):
    data_row = [int(el) for el in input().split(", ")]
    sum_elements += sum(data_row)
    matrix.append(data_row)

# sum_elements = 0
#
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         sum_elements += matrix[row_index][col_index]

print(sum_elements)
print(matrix)
# print(sum(map(sum, matrix)))
