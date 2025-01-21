# Write a program that receives a matrix of numbers and prints a new one only with the even numbers.
# Use nested comprehension for that problem.

# On the first line, you will receive the rows of the matrix. On the next rows,
# you will get elements for each column separated with a comma and a space ", ".

#              Examples

# Input                       Output

# 2                           [[2], [4, 6]]
# 1, 2, 3
# 4, 5, 6

# 4                           [[10, 24], [34, 110], [4, 12], []]
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67


rows = int(input())

matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row_data)

print(matrix)
