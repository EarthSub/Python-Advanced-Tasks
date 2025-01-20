# We think the process of making honey is amazing! Let's learn more about how bees make honey.

# Worker bees collect nectar. When a worker-bee has found enough nectar,
# she returns to the hive to drop off the load and pass the nectar to waiting bees so they can really start the honey-making process.

# You will receive 3 sequences:

#     · a sequence of integers, representing working bees
#     · a sequence of integers, representing nectar
#     · a sequence of symbols – "+", "-", "*", or "/", representing the honey-making process.

# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey waiting for bees made with the collected nectar.

# Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:

#     · If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
#     · If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee
#       with the next nectar's value until the bee collects enough nectar.

# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made.
# Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:

# "{matched_bee} {symbol} {matched_nectar}"

# The result represents the honey that is made from the passed nectar.
# The calculation should always return the absolute value of the result.
# After the calculation, remove the bee, the nectar, and the symbol.

#     · If the symbol is "/" and the nectar’s value is 0 (zero), skip the calculation and remove the bee, the nectar, and the symbol.

# Stop making honey when you are out of bees or nectar.

# Input

#     · On the first line, you will be given the values of bees - integers, separated by a single space
#     · On the second line, you will be given the nectar's values - integers, separated by a single space
#     · On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space

# Output

#     · On the first line - print the total honey made:
#         o "Total honey made: {total honey}"
#     · On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
#         o "Bees left: {bee1}, {bee2}, … {beeN}"
#         o "Nectar left: {nectar1}, {nectar2}, … {nectarN}"

# Constraints

#     · All the bee's values will be integers in the range [0, 150]
#     · Nectar's values will be integers in the range [0, 150]
#     · There always will be enough symbols in the sequence of symbols


#                                     Examples

# Input                       Output                                  Comment

# 20 62 99 35 0 150           Total honey made: 148                   First, compare 20 to 10. 20 is bigger than 10, so
# 120 60 10 1 70 10           Bees left: 99, 35, 0, 150               remove 10. Then compare 20 to 70. 20 is less
# + - + + / * - - /                                                   than 70, so the bee could return to the hive.
#                                                                     Honey made with given nectar is 20 + 70 = 90.

#                                                                     Next, compare 62 to 1. 62 is bigger than 1, so
#                                                                     remove 1. Compare 62 to 10. 62 is bigger than
#                                                                     10, so remove 10. Compare 62 to 60. 62 is
#                                                                     bigger than 60, so remove 60. Compare 62 to
#                                                                     120. 60 is less than 120, so the bee could return
#                                                                     to the hive. Honey made with given nectar is 62
#                                                                     - 120 = (-58). (-58) is negative, and its absolute
#                                                                     value is 58, so the calculation result is 58.

#                                                                     Total honey made: 90 + 58 = 148.

#                                                                     Print the desired text.

# Input                       Output

# 30                          Total honey made: 4500
# 15 9 5 150 8                Nectar left: 15, 9, 5
# * + + * -


from collections import deque

bees = deque(int(n) for n in input().split())
nectar = [int(n) for n in input().split()]
honey_making_process = deque(input().split())

honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}


while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operators[honey_making_process[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        honey_making_process.popleft()
    elif nectar[-1] < bees[0]:
        nectar.pop()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(n) for n in nectar])}")
