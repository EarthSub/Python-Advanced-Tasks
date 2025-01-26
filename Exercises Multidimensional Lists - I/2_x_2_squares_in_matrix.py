# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# In the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.


#                     Examples

# Input               Output              Comments

# 3 4                 2                   Two 2x2 squares of equal cells:
# A B B D                                 A B B D      A B B D
# E B B B                                 E B B B      E B B B
# I J B B                                 I J B B      I J B B

# Input               Output              Comments

# 2 2                 0                   No 2x2 squares of equal cells exist.
# a b
# c d

# Input               Output              Comments

# 5 4                 3                   Three 2x2 squares of equal cells:
# A A B D                                 A A B D     A A B D     A A B D
# A A B B                                 A A B B     A A B B     A A B B
# I J B B                                 I J B B     I J B B     I J B B
# C C C G                                 C C C G     C C C G     C C C G
# C C K P                                 C C K P     C C K P     C C K P


rows, columns = [int(n) for n in input().split()]

matrix = [input().split() for _ in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)

