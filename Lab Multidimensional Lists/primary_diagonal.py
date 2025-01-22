# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix.
# The next N lines hold the values for each column - N numbers, separated by a single space.


#                         Examples

# Input           Output            Input             Output

# 3               4                 3                 15
# 11 2 4                            1 2 3
# 4 5 6                             4 5 6
# 10 8 -12                          7 8 9


n = int(input())

matrix = []

for _ in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

sum_diagonal = 0

for index in range(len(matrix)):
    sum_diagonal += matrix[index][index]

print(sum_diagonal)

