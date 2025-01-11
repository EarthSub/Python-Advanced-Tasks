# Write a program that reads a string with N integers from the console, separated by a single space,
# and reverses them using a stack. Print the reversed integers on one line, separated by a single space.


#             Examples

# Input                       Output

# 1 2 3 4 5                   5 4 3 2 1

# 1                           1



stack = input().split()
reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(" ".join(reversed_stack))