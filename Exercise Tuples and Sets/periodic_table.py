# Write a program that keeps all the unique chemical elements. On the first line,
# you will be given a number n - the count of input lines that you will receive.
# On the following n lines, you will be receiving chemical compounds separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter):


#                                 Examples

# Input               Output                  Input               Output

# 4                   Ce                      3                   Ch
# Ce O                Ee                      Ge Ch O Ne          Ge
# Mo O Ce             Mo                      Nb Mo Tc            Mo
# Ee                  O                       O Ne                Nb
# Mo                                                              Ne
#                                                                 O
#                                                                 Tc


elements = set()

for _ in range(int(input())):
    for element in input().split():
        elements.add(element)

print(*elements, sep="\n")
