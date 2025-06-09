# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
# The first two numbers in the sequence are always 0 and 1.
# Each following Fibonacci number is created by the sum of the current number with the previous one.

#                             Examples

# Test Code                                                   Output

# generator = fibonacci()                                     0
# for i in range(5):                                          1
#     print(next(generator))                                  1
#                                                             2
#                                                             3

# Test Code                                                   Output

# generator = fibonacci()                                     0
# for i in range(1):
#     print(next(generator))



def fibonacci():
    current_number, next_number = 0, 1
    while True:
        yield current_number
        current_number, next_number = next_number, current_number + next_number



generator = fibonacci()
for i in range(5):
    print(next(generator))

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
