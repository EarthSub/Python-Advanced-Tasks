# Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.

# Hints

# In short, if we have a sorted collection of comparable elements, instead of doing a linear search (which takes linear time),
# we can eliminate half the elements at each step and finish in logarithmic time.
# Binary search is a divide-and-conquer algorithm; we start at the middle of the collection,
# if we haven’t found the element there, there are three possibilities:

#     · The element we’re looking for is smaller – then look to the left of the current element, we know all elements to the right are larger
#     · The element we’re looking for is larger – look to the right of the current element
#     · The element is not present, traditionally, return -1 in that case


#                         Examples

# Input                   Output                  Comments

# 1 2 3 4 5               0                       An index of 1 is 0
# 1

# Input                   Output                  Comments

# -1 0 1 2 4              2                       An index of 1 is 2
# 1



def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2

        mid_el = numbers[mid_idx]
        if mid_el == target:
            return mid_idx
        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


numbers = list(map(int, input().split()))
target = int(input())
result = binary_search(numbers, target)

print(result)
