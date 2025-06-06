# Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
# Implement an iterator to return the given elements, so they form a string with a length - the given number.
# If the number is greater than the number of elements, then the sequence repeats as necessary.
# For more clarification, see the examples:


#                                 Examples

# Test Code                                                       Output

# result = sequence_repeat('abc', 5)                              abcab
# for item in result:
#     print(item, end ='')

# Test Code                                                       Output

# result = sequence_repeat('I Love Python', 3)                    I L
# for item in result:
#     print(item, end ='')



class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            index = self.i % len(self.sequence)
            self.i += 1
            return self.sequence[index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
