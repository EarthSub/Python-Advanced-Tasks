# You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.

# It is given a sequence of numbers, separated by a ", ". Iterate through each number by its index,
# and if the number is smaller or equal to 5, make a multiplication.
# If the number is larger than 5 and smaller or equal to 10, divide the result by the number. In the end, print the final result.


# numbers_list = int(input()).split(", ")
# result = 1

# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number <= 5
#         result *= number
#     elif 5 < number <= 10:
#         result /= number

# print(total)


#                             Examples

# Input                                                   Output

# 2, 5, 10                                                1.0

# Input                                                   Output

# 4, 5, 6, 1, 3                                           10.0

# Input                                                   Output

# 1, 4, 5                                                 20.0

# Input                                                   Output

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11                       0.003968253968253968


numbers_list = [int(n) for n in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)