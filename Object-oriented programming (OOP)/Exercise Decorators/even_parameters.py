# Create a decorator function called even_parameters.
# It should check if all parameters passed to a function are even numbers and only then execute the function and return the result.
# Otherwise, don't execute the function and return "Please use only even numbers!"


#                                 Examples

# Test Code                                                       Output

# @even_parameters                                                6
# def add(a, b):                                                  Please use only even numbers!
#     return a + b

# print(add(2, 4))
# print(add("Peter", 1))

# Test Code                                                       Output

# @even_parameters                                                384
# def multiply(*nums):                                            Please use only even numbers!
#     result = 1
#     for num in nums:
#        result *= num
#     return result

# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8)




def even_parameters(func):
    def wrapper(*args):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print()

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
