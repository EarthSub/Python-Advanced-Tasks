# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its values.

# On the first line, you will get matrix sizes in the format "{rows}, {columns}". On the next rows,
# you will get elements for each column, separated with a comma and a space ", ".

# You should print the found submatrix and the sum of its elements, as shown in the examples.


#                                          Examples

# Input                           Output              Input                           Output

# 3, 6                            9 8                 2, 4                            12 13
# 7, 1, 3, 3, 2, 1                7 9                 10, 11, 12, 13                  16 17
# 1, 3, 9, 8, 5, 6                33                  14, 15, 16, 17                  58
# 4, 6, 7, 9, 1, 0


# Hints

#   · Be aware of IndexError
#   · If you find more than one max square, print the top-left one


rows, columns = [int(n) for n in input().split(", ")]

matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

sum_sub_matrix = float("-inf")
sub_matrix = []

for row in range(len(matrix)-1):
    for col in range(len(matrix[row])-1):
        element = matrix[row][col]
        element_next_to = matrix[row][col+1]
        element_below = matrix[row+1][col]
        element_diagonal = matrix[row+1][col+1]

        current_sum = element + element_next_to + element_below +element_diagonal

        if current_sum > sum_sub_matrix:
            sum_sub_matrix = current_sum
            sub_matrix = [
                [element, element_next_to],
                [element_below, element_diagonal]
            ]

for element in sub_matrix:
    print(*element)
print(sum_sub_matrix)


