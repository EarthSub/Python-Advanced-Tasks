# Write an implementation of Bubble Sort. You should read an array of integers and sort them.

# Input

#      · Input should be on single line.

# Output

#     · You should print out the sorted list in the format described below.


#                           Examples

# Input                                                   Output

# 5 4 3 2 1                                               1 2 3 4 5

# Input                                                   Output

# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89              0 1 5 7 7 9 10 12 12 13 14 15 15 16
# 65 16 38 42 15 86 21 93 10 31 28 36 14 65               17 17 18 19 20 20 21 21 21 22 24 25
# 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36              27 27 28 28 29 29 31 31 32 32 33 33
# 33 54 20 40 60 56 51 51 25 77 75 46 47 57               34 34 35 36 36 36 37 37 38 40 41 42
# 18 12 27 28 29 21 22 37 74 78 34 15 71 75               43 44 44 46 47 48 49 51 51 51 52 54
# 20 19 76 48 98 36 76 49 83 21 44 12 85 68               54 55 55 56 57 60 61 64 65 65 65 66
# 24 9 80 41 66 1 54 31 55 33 88 35 32 43                 68 68 70 71 74 74 75 75 75 76 76 77
#                                                         78 80 83 85 86 86 86 88 89 93 93 96
#                                                         97 98


def bubble_sort(nums):
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False
        i += 1


def print_sorted_list(nums):
    print(" ".join(map(str, nums)))


input_numbers = list(map(int, input().split()))
bubble_sort(input_numbers)
print_sorted_list(input_numbers)

