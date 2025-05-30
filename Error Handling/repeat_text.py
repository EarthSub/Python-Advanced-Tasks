# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
# If the user passes a non-integer type for the times variable, handle the exception and print a message "Variable times must be an integer".


#              Examples

# Input                       Output

# Hello                       Variable times must be an integer
# Bye

# Input                       Output

# Hello                       HelloHello
# 2


text = input()

try:
    multiplier = int(input())
    print(text * multiplier)
except ValueError:
    print("Variable times must be an integer")


