# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.


#                 Examples

# Input           Output          Comments

# 3               15              Primary diagonal: sum = 11 + 5 + (-12) = 4
# 11 2 4                          Secondary diagonal: sum = 4 + 5 + 10 = 19
# 4 5 6                           Difference: |4 - 19| = 15
# 10 8 -12


# Input           Output

# 4               34
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

