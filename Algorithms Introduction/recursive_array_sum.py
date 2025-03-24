# Write a program that finds the sum of all elements in an integer array. Use recursion.

# Note: In practice, this recursion should not be used here (instead use an iterative solution), this is just an exercise.


#             Examples

# Input                       Output

# 1 2 3 4                     10

# Input                       Output

# -1 0 1                      0



def calc_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + calc_sum(numbers, idx + 1)


nums = [int(x) for x in input().split()]

print(calc_sum(nums, 0))
