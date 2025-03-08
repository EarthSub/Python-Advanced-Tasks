# You are given the following code:


# def rotate_matrix(matrix):
#     matrix_length = len(matrix)
#         for i in range(matrix_length):
#             for j in range(i, matrix_length):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#         for i in range(matrix_length):
#             matrix[i].reverse()


# mtrx = []

# while True:
#     line = input().split()

#     if not line:
#         break
#     mtrx.append(line)


# rotate_matrix(mtrx)

# for row in mtrx:
#     print(*row, sep=' ')


# On the following lines, until there is an empty line, you receive numbers, divided by space, representing each matrix row.

# The rotate_matrix function accepts the matrix as a parameter and rotates it 90 degrees clockwise (to the right).

#     · The provided code contains errors that must be fixed. You should refactor the existing code without reconstructing the entire algorithm.

# Implement error handling during the following stages:

#     · Verify the matrix contains only integers, otherwise, MatrixContentError should be raised.
#     · Ensure the input is an N x N (2D matrix), otherwise, MatrixSizeError should be raised.

# When an error is encountered, raise it with an appropriate message:

#     · MatrixContentError - "The matrix must consist of only integers"
#     · MatrixSizeError - "The size of the matrix is not a perfect square"


#             Examples

# Input                       Output

# 1 2 3                       7 4 1
# 4 5 6                       8 5 2
# 7 8 9                       9 6 3

# Input                       Output

# 1 2 3 4                     Traceback (most recent call last):
# 5 6 7 8                         File ".\rotate_matrix.py", line 34, in <module>
#                                     raise MatrixSizeError("The size of the matrix is not a perfect
#                             square")
#                             MatrixSizeError: The size of the matrix is not a perfect square

# Input                       Output

# 7 8                         Traceback (most recent call last):
# 9 k                             File ".\rotate_matrix.py", line 39, in <module>
#                                     raise MatrixContentError("The matrix must consist of only
#                             integers")
#                             MatrixContentError: The matrix must consist of only integers


class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().split()

    if not line:
        break

    for element in line:
        if not element.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")
    mtrx.append(line)

for row in mtrx:
    if len(row) != len(mtrx):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=" ")
