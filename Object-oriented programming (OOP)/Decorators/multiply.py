# Having the following code:

# def multiply(times):
#     def decorator(function):
#         # TODO: Implement
#     return decorator

# Complete the code, so it works as expected.


#                                 Examples

# Test Code                       Output                      Comment

# @multiply(3)                                                First, we add 3 to 10 = 13, and then we multiply the
# def add_ten(number):                                        result by 3: 13 * 3 = 39
#     return number + 10          39

# print(add_ten(3))

# Test Code                       Output                      Comment

# @multiply(5)                                                (6 + 10) * 5 = 80
# def add_ten(number):
#     return number + 10          80

# print(add_ten(6))



def multiply(number):
    def function(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * number
        return wrapper
    return function



@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))