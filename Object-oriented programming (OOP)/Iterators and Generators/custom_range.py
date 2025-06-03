# Create a class called custom_range that receives a start (int) and an end (int) upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).


#                             Examples

# Test Code                                                   Output

# one_to_ten = custom_range(1, 10)                            1
# for num in one_to_ten:                                      2
# print(num)                                                  3
#                                                             4
#                                                             5
#                                                             6
#                                                             7
#                                                             8
#                                                             9
#                                                             10



class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.temp = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.temp += 1
        if self.temp > self.end:
            raise StopIteration
        return self.temp



one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)