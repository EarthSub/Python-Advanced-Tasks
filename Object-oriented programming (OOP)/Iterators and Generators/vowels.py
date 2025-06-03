# Create a class called vowels, which should receive a string.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.


#                                 Examples

# Test Code                                                           Output

# reversed_list = reverse_iter([1, 2, 3, 4])                          A
# for item in reversed_list:                                          e
# print(item)                                                         i
#                                                                     u
#                                                                     y
#                                                                     o


class vowels:

    def __init__(self, text):
        self.text = text

        self.vowel = [ch for ch in self.text if ch.lower() in "aeiuyo"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.vowel):
            raise StopIteration
        return self.vowel[self.index]



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
