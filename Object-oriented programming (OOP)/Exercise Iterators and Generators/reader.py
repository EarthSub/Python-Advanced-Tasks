# Create a generator function called read_next() which should receive a different number of arguments (all iterable).
# On each iteration, the function should return each element from each sequence.


#                                             Examples

# Test Code                                                                                   Output

# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):                    string2dict
#     print(item, end='')

# Test Code                                                                                   Output

# for i in read_next("Need", (2, 3), ["words", "."]):                                         N
#     print(i)                                                                                e
#                                                                                             e
#                                                                                             d
#                                                                                             2
#                                                                                             3
#                                                                                             words
#                                                                                             .


def read_next(*collections):
    for collection in collections:
        yield from collection
        # for el in collection:
        #     yield el



for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print()

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
