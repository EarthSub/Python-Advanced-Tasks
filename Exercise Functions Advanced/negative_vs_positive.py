# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:

#     · On the first line, print the sum of the negatives
#     · On the second line, print the sum of the positives
#     · On the third line:
#         o If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
#         o If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"

# Note: you will not receive any zeroes in the input.


#                         Example

# Input                                               Output

# 1 2 -3 -4 65 -98 12 57 -84                          -189
#                                                     137
#                                                     The negatives are stronger than the positives

# Input                                               Output

# 1 2 3                                               0
#                                                     6
#                                                     The positives are stronger than the negatives



def negative_and_positive(*args):
    positive_sum = sum(num for num in args if num > 0)
    negative_sum = sum(num for num in args if num < 0)


    if positive_sum > abs(negative_sum):
        positive_or_negative = "The positives are stronger than the negatives"
    else:
        positive_or_negative = "The negatives are stronger than the positives"
    return f"{negative_sum}\n{positive_sum}\n{positive_or_negative}"


print(negative_and_positive(*[int(n) for n in input().split()]))
