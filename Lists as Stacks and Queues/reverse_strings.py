# Write a program that:

# · Reads an input string
# · Reverses it using a stack
# · Prints the result back on the console


#             Examples

# Input                       Output

# I Love Python               nohtyP evoL I

# Stacks and Queues           seueuQ dna skcatS


some_text = list(input())

while some_text:
    print(some_text.pop(), end="")
