# Create a generator function called possible_permutations() which should receive a
# list and return lists with all possible permutations between its elements.


#                                     Examples

# Test Code                                                                   Output

# [print(n) for n in possible_permutations([1, 2, 3])]                        [1, 2, 3]
#                                                                             [1, 3, 2]
#                                                                             [2, 1, 3]
#                                                                             [2, 3, 1]
#                                                                             [3, 1, 2]
#                                                                             [3, 2, 1]

# Test Code                                                                   Output

# [print(n) for n in possible_permutations([1])]                              [1]





#           variant 1
# def possible_permutations(lst):
#     if len(lst) <= 1:
#         yield lst
#
#     else:
#         for i in range(len(lst)):
#             current_element = lst[i]
#             remaining_elements = lst[:i] + lst[i + 1:]
#             permutations = possible_permutations(remaining_elements)
#             for permutation in permutations:
#                 yield [current_element, *permutation]



#           variant 2
from itertools import permutations

def possible_permutations(lst):
    for perm in permutations(lst):
        yield list(perm)



[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]
