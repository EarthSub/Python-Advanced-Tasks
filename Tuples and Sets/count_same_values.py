# You will be given numbers separated by a space. Write a program that prints the number of
# occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.


#                         Examples

# Input                                               Output

# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3                     -2.5 - 3 times
#                                                     4.0 - 2 times
#                                                     3.0 - 4 times
#                                                     -5.5 - 1 times

# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3             2.0 - 3 times
#                                                     4.0 - 6 times
#                                                     5.0 - 4 times
#                                                     3.0 - 7 times


data = tuple([float(e) for e in input().split()])

count = {}

for el in data:
    count[el] = data.count(el)

for key, value in count.items():
    print(f"{key:.1f} - {value} times")