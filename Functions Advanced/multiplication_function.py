# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and
# returns the result of the multiplication of all of them. Submit only your function in the Judge system.


#                         Examples

# Test Code                                           Output

# print(multiply(1, 4, 5))                            20
# print(multiply(4, 5, 6, 1, 3))                      360
# print(multiply(2, 0, 1000, 5000))                   0


def multiply(*args):
    result = 1
    if args:
        for num in args:
            result *= num
    else:
        return ""
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
print(multiply())