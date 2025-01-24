# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
# separated by a comma and a space ", ". You should find the matrix's diagonals, print them, and their sum in the format:

# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".


#             Examples

# Input                       Output

# 3                           Primary diagonal: 1, 5, 9. Sum: 15
# 1, 2, 3                     Secondary diagonal: 3, 5, 7. Sum: 15
# 4, 5, 6
# 7, 8, 9


n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

