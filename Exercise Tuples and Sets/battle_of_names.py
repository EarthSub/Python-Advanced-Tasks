# You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.

#     · If the sums of the two sets are equal, print the union of the values, separated by ", ".
#     · If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
#     · If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".

# NOTE: On every operation, the starting set should be the odd set


#                         Examples

# Input           Output                          Comment

# 4               304, 128, 206, 511              First name: Pesho. The sum of the ASCII values is 80 + 101 + 115 + 104 +
# Pesho                                           111 = 511. Integer divides the sum to the current row (1): 511 / 1 = 511.
# Stefan                                          Second name: Stefan. The sum of the ASCII values is 83 + 116 + 101 + 102
# Stamat                                          + 97 + 110 = 609. Integer divides the sum to the current row (2): 609 / 2 =
# Gosho                                           304.
#                                                 Third name: Stamat. The sum of the ASCII values is 83 + 116 + 97 + 109 +
#                                                 97 + 116 = 618. Integer divides the sum to the current row (3): 618 / 3 =
#                                                 206.
#                                                 Fourth name: Gosho. The sum of the ASCII values is 71 + 111 + 115 + 104 +
#                                                 111 = 512. Integer divides the sum to the current row (4): 512 / 4 = 128.
#                                                 The odd set: 511
#                                                 The even set: 304, 206, 128
#                                                 The sum of the even numbers is larger, so we print the symmetric-different
#                                                 values.

# 6                                               733, 101
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan


odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    number = sum(ord(char) for char in input()) // row
    if number % 2 == 0:
        even_set.add(number)
    elif number % 2 == 1:
        odd_set.add(number)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")

