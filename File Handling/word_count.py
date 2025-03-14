# Write a program that reads a list of words from the file words.
# txt and finds how many times each of the words is contained in another file text.txt.
# Matching should be case-insensitive.

# The results should be written into other text files. Sort the words by frequency in descending order.


#                                             Examples

# words.txt                   input.txt                                           output.txt

# quick is fault              -I was quick to judge him, but it                   is - 3
#                             wasn't his fault.                                   quick - 2
#                             -Is this some kind of joke?! Is it?                 fault - 1
#                             -Quick, hide here…It is safer.


import re

with open("words.txt") as file:
    searched_words = file.read()

searched_words = searched_words.split()

with open("input.txt") as file:
    text = file.read()

data = {}

for searched_word in searched_words:
    pattern = rf"\b{searched_word}\b"
    result = re.findall(pattern, text, re.IGNORECASE)
    data[searched_word] = len(result)

sorted_data = sorted(data.items(), key=lambda x: -x[1])

with open("output.txt", "a") as file:
    for key, value in sorted_data:
        file.write(f"{key} - {value}\n")
