# You have an empty stack. You will receive an integer – N.
# On the following N lines, you will receive queries. Each query is one of these four types:

#     · '1 {number}' – push the number (integer) into the stack
#     · '2' – delete the number at the top of the stack
#     · '3' – print the maximum number in the stack
#     · '4' – print the minimum number in the stack

# It is guaranteed that each query is valid.

# After you go through all the queries, print the stack from top to bottom in the following format:

# "{n}, {n1}, {n2}, ... {nn}"


#                     Examples

# Input                                       Output

# 9                                           26
# 1 97                                        20
# 2                                           91, 20, 26
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# 10                                          32
# 2                                           66
# 1 47                                        8
# 1 66                                        8, 16, 25, 32, 66, 47
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4


#      example 1

stack = []
lines = int(input())

for _ in range(lines):
    query = input().split()
    if query[0] == "1":
        stack.append(int(query[1]))
    elif stack:
        if query[0] == "2":
            stack.pop()
        elif query[0] == "3":
            print(max(stack))
        elif query[0] == "4":
            print(min(stack))

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")


#      example 2

stack = []
lines = int(input())


functions = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None
}

for _ in range(lines):
    query = input().split()
    functions[query[0]](*query[1:])

print(*reversed(stack), sep=", ")