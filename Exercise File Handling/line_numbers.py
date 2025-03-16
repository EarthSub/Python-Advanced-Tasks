# Write a program that reads a text file, inserts line numbers in front of each line,
# and counts all the letters and punctuation marks. The result should be written in another text file.


#                             Examples

# text.txt                                                output.txt

# -I was quick to judge him, but it                       Line 1: -I was quick to judge him, but it
# wasn't his fault.                                       wasn't his fault. (37)(4)
# -Is this some kind of joke?! Is                         Line 2: -Is this some kind of joke?! Is it?
# it?                                                     (24)(4)
# -Quick, hide here. It is safer.                         Line 3: -Quick, hide here. It is safer.
#                                                         (22)(4)


from string import punctuation


with open("exercise.txt", "r") as infile, open("exercise_two.txt", "w") as outfile:
    lines = infile.readlines()
    line_number = 1

    for line in lines:
        line_content = line.strip()
        letters = sum(1 for char in line_content if char.isalpha())
        punctuations = sum(1 for char in line_content if char in punctuation)
        result_line = f"Line {line_number}: {line_content} ({letters})({punctuations})\n"
        outfile.write(result_line)
        line_number += 1
