# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
# Implement the __iter__ and __next__ functions.
# The iterator should return the count numbers (starting from 0) with the given step.
# For more clarification, see the examples:


#                             Examples

# Test Code                                                   Output

# numbers = take_skip(2, 6)                                   0
# for number in numbers:                                      2
# print(number)                                               4
#                                                             6
#                                                             8
#                                                             10

# Test Code                                                   Output

# numbers = take_skip(10, 5)                                  0
# for number in numbers:                                      10
# print(number)                                               20
#                                                             30
#                                                             40



class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.count:
            return self.i * self.step
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)



numbers = take_skip(10, 5)
for number in numbers:
    print(number)
