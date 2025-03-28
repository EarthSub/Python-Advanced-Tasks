# Write a program that finds the smallest subset of sets, which contains all elements from a given sequence.

# In the Set Cover problem, we are given two sets - a set of sets (we'll call it sets) and a universe (a sequence).
# The sets contain all elements from the universe and no others, however,
# some elements are repeated. The task is to find the smallest subset of sets that contains all elements in the universe.

# Input

#     · On the first line, you will receive the universe.
#     · On the second line, you will receive the target number of sets.
#     · On the next lines, you will receive different sets of sets.


#                     Examples

# Input                                       Output

# 1, 2, 3, 4, 5                               Sets to take (4):
# 4                                           { 2, 4 }
# 1                                           { 1 }
# 2, 4                                        { 5 }
# 5                                           { 3 }
# 3

# Input                                       Output

# 1, 2, 3, 4, 5                               Sets to take (1):
# 4                                           { 1, 2, 3, 4, 5 }
# 1, 2, 3, 4, 5
# 2, 3, 4, 5
# 5
# 3

# Input                                       Output

# 1, 3, 5, 7, 9, 11, 20, 30, 40               Sets to take (4):
# 6                                           { 3, 7, 20, 30, 40 }
# 20                                          { 1, 5, 20, 30 }
# 1, 5, 20, 30                                { 9, 30 }
# 3, 7, 20, 30, 40                            { 11, 20, 30, 40 }
# 9, 30
# 11, 20, 30, 40
# 3, 7, 40


# Hints

# Greedy Approach

# Using the greedy approach, at each step, we'll take the set which contains the most elements present in the universe which we haven't yet taken.
# In the first step, we'll always take the set with the largest number of elements, but it gets a bit more complicated afterward.
# To simplify our job (and not check against two sets at the same time), when taking a set,
# we can remove all elements in it from the universe. We can also remove the set from the sets we're considering.



def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []

    while universe_set:
        best_set = max(sets, key=lambda s: len(universe_set.intersection(s)))
        chosen_sets.append(best_set)
        universe_set -= set(best_set)

    return chosen_sets


universe_input = input()
universe = list(map(int, universe_input.split(", ")))

num_sets = int(input())
sets = []

for _ in range(num_sets):
    set_elements = list(map(int, input().split(", ")))
    sets.append(set(set_elements))

result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print("\nSets to take ({}):".format(len(result)))

for s in result:
    print("{", ", ".join(map(str, s)), "}")
