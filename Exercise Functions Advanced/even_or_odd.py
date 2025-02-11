# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.


#                                 Examples

# Test Code                                                   Output

# print(even_odd(1, 2, 3, 4, 5, 6, "even"))                   [2, 4, 6]

# Test Code                                                   Output

# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))       [1, 3, 5, 7, 9]


def even_odd(*args):
    command = args[-1]
    if command == "even":
        even = [num for num in args[:-1] if num % 2 == 0]
        return even
    if command == "odd":
        odd = [num for num in args[:-1] if num % 2 == 1]
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))