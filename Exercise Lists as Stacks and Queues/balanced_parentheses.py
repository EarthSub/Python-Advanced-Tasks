# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that
# occurs after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].

# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.

# Input

#     · On a single line, you will receive a sequence of parentheses.

# Output

#     · For each test case, print on a new line "YES" if the parentheses are balanced.
#     · Otherwise, print "NO"

# Constraints

#     · 1 ≤ lens ≤ 1000, where the lens is the length of the sequence
#     · Each character of the sequence will be one of {, }, (, ), [, ]


#             Examples

# Input                     Output

# {[()]}                    YES

# {[(])}                    NO

# {{[[(())]]}}              YES


#       example 1

string = input()

stack = []
parentheses = {')': '(', '}': '{', ']': '['}

for char in string:
    if char in parentheses.values():
        stack.append(char)
    elif char in parentheses.keys():
        if stack and stack[-1] == parentheses[char]:
            stack.pop()
        else:
            print("NO")
            exit()

if not stack:
    print("YES")
else:
    print("NO")


#      example 2

expression = input()

opening_parentheses = "([{"
closing_parentheses = ")]}"
stack = []

for char in expression:
    if char in opening_parentheses:
        stack.append(char)
    elif char in closing_parentheses:
        if not stack:
            print("NO")
            break
        last_parentheses = stack.pop()
        if opening_parentheses.index(last_parentheses) != closing_parentheses.index(char):
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")