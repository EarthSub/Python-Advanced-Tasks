# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.

# Print the result back on the console.


#                         Examples

# Input                                               Output

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5                 (2 + 3)
#                                                     ((3 + 1)
#                                                     (2 - (2 + 3) * 4 / (3 + 1)))

# (2 + 3) - (2 + 3)                                   (2 + 3)
#                                                     (2 + 3)


expression = input()
stack = []


for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        starting_index = stack.pop()
        print(expression[starting_index:index+1])
