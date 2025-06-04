# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.


#                             Examples

# Test Code                                                   Output

# for char in reverse_text("step"):                           pets
# print(char, end='')


def reverse_text(text):

    index = len(text) - 1
    while index >= 0:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
