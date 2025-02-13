# Write a concatenate() function that receives some strings as arguments and some named arguments
# (the key will be a string, and the value will be another string).

# First, you should concatenate all arguments successively. Next,
# take each key successively, and if it is present in the resulting string,
# change all matching parts with the key's value. In the end, return the final string.

# See the examples for more clarification.


#                                 Examples

# Test Code                                                           Output

# print(concatenate("Soft", "UNI", "Is", "Grate", "!",                SoftUniIsGreat!
# UNI="Uni", Grate="Great"))

# Test Code                                                           Output

# print(concatenate("I", " ", "Love", " ", "Cythons",                 I Love Python
# C="P", s="", java='Java'))


def concatenate(*args, **kwargs):
    sentence = ''.join(args)
    for key, value in kwargs.items():
        sentence = sentence.replace(key, value)
    return sentence


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",
C="P", s="", java='Java'))