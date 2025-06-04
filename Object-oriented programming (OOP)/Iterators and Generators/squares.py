# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).


#                             Examples

# Test Code                                               Output

# print(list(squares(5)))                                 [1, 4, 9, 16, 25]



def squares(n):

    current_n = 1

    while current_n <= n:
        yield current_n ** 2
        current_n += 1


print(list(squares(5)))