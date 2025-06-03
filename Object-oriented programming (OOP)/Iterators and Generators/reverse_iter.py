# Create a class called reverse_iter which should receive an iterable upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.


#                                 Examples

# Test Code                                                           Output

# reversed_list = reverse_iter([1, 2, 3, 4])                          4
# for item in reversed_list:                                          3
# print(item)                                                         2
#                                                                     1



class reverse_iter:

    def __init__(self, data):
        self.data = data

        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.data[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
