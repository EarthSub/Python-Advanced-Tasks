# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0. Before you print the result,
# replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words


#                             Examples

# text.txt                                                output

# -I was quick to judge him, but it                       fault@ his wasn't it but him@ judge to
# wasn't his fault.                                       quick was @I
# -Is this some kind of joke?! Is it?                     safer@ is It here@ hide @Quick@
# -Quick, hide here. It is safer.


characters_to_replace = ["-", ",", ".", "!", "?"]

with open("exercise.txt") as file:
    lines = file.readlines()

for index in range(0, len(lines), 2):
    for char in characters_to_replace:
        lines[index] = lines[index].replace(char, "@")
    current_word = reversed(lines[index].split())
    print(" ".join(current_word))