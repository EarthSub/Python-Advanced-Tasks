# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).


#                                     Examples

# Test Code                                                               Output

# result = dictionary_iter({1: "1", 2: "2"})                              (1, '1')
# for x in result:                                                        (2, '2')
#     print(x)

# Test Code                                                               Output

# result = dictionary_iter({"name": "Peter",
# "age": 24})
# for x in result:
#     print(x)



class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dict_tuple):
            i = self.i
            self.i += 1
            return self.dict_tuple[i]
        raise StopIteration



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
