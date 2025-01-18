# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.


#                                 Examples

# Input                   Output                  Input                   Output

# SoftUni rocks            : 1 time/s             Why do you like          : 4 time/s
#                         S: 1 time/s             Python?                 ?: 1 time/s
#                         U: 1 time/s                                     P: 1 time/s
#                         c: 1 time/s                                     W: 1 time/s
#                         f: 1 time/s                                     d: 1 time/s
#                         i: 1 time/s                                     e: 1 time/s
#                         k: 1 time/s                                     h: 2 time/s
#                         n: 1 time/s                                     i: 1 time/s
#                         o: 2 time/s                                     k: 1 time/s
#                         r: 1 time/s                                     l: 1 time/s
#                         s: 1 time/s                                     n: 1 time/s
#                         t: 1 time/s                                     o: 3 time/s
#                                                                         t: 1 time/s
#                                                                         u: 1 time/s
#                                                                         y: 3 time/s


#       example 1

text = input()
set_of_symbols = set()

for char in text:
    set_of_symbols.add(char)

for char in sorted(set_of_symbols):
    print(f"{char}: {text.count(char)} time/s")

#       example 2

text = input()

[print(f"{char}: {text.count(char)} time/s") for char in sorted(set(text))]

