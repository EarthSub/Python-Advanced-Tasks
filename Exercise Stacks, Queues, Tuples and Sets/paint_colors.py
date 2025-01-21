# You will have to find all possible color combinations that can be used.

# Write a program that finds colors in a string.
# You will be given a string on a single line containing substrings (separated by a single space)
# from which you will be able to form the following colors:

# Main colors: "red", "yellow", "blue"

# Secondary colors: "orange", "purple", "green"

# To form a color, you should concatenate the first and the last substrings and check if
# you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.

# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:

#     · orange = red + yellow
#     · purple = red + blue
#     · green = yellow + blue

# Note: You could find some of the main colors needed to keep a secondary color after it is found.

# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
# return them in the middle of the original string. If the string contains an odd number of substrings,
# you should put the substrings one position ahead.

# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",
# so you should remove the last character and return them in the middle of the string: "r by yellow".

# In the end, print out the list with colors in the order in which they are found.

# Input

#     · Single line string.

# Output

#     · The list with the collected colors.

# Constraints

#     · You will not receive an empty string.
#     · Please consider only the colors mentioned above.
#     · There won't be any cases with repeating colors.


#                     Examples

# Input                                       Output

# d yel blu e low redd                        ['yellow', 'blue', 'red']

#                     Comment

# First, we take "d" and "redd". After combining those substrings, we don't get any of the needed colors, so we
# remove the last characters from both substrings and return them in the middle of the original string, and it becomes
# "yel blu red e low".
# After that, we take "yel" and "low" so the first color we add to our list is yellow, and the string we are searching in
# looks as follows: "blu red e"
# Then we take "blu" and "e", and since this color is one of the searched ones (blue), we add it to our collection, and
# the state of the string is now "red".
# We should take the last substring and check if it matches some of the colors, and since it does, we add it (red) to our
# colors collection.
# Finally, we print all the colors found: yellow, blue, and red in the format shown above.

# Input                                       Output

# r ue nge ora bl ed                          ['red', 'blue']

#                      Comment

# We don't keep orange because we don't have yellow in the final list of colors (combining red and yellow gives us
# orange).

# Input                                       Output

# re ple blu pop e pur d                      ['red', 'purple', 'blue']


from collections import deque


initial_data = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
colors = []

while initial_data:
    first_string = initial_data.popleft()
    last_string = initial_data.pop() if initial_data else ""
    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            colors.append(color)
            break
    else:
        if len(first_string) > 1:
            initial_data.insert(len(initial_data) // 2, first_string[:-1])
        if len(last_string) > 1:
            initial_data.insert(len(initial_data) // 2, last_string[:-1])

for color in colors:
    if color in secondary_colors:
        for current_color in secondary_colors[color]:
            if current_color not in colors:
                colors.remove(color)

print(colors)