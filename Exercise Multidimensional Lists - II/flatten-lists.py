# Write a program to flatten several lists of numbers received in the following format:

#     § String with numbers or empty strings separated by "|"
#     § Values are separated by spaces (" ", one or several)
#     § Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below


#                 Examples

# Input                           Output

# 1 2 3 |4 5 6 | 7 88             7 88 4 5 6 1 2 3
#
# 7 | 4 5|1 0| 2 5 |3             3 2 5 1 0 4 5 7
#
# 1| 4 5 6 7 | 8 9                8 9 4 5 6 7 1


initial_data = input().split("|")

integer_lists = [[int(n) for n in char.split()] for char in initial_data]

integer_lists.reverse()

flattened_list = [n for num in integer_lists for n in num]

print(*flattened_list)