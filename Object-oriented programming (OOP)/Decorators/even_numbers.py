# Having the following code:

# def even_numbers(function):
#     def wrapper(numbers):
#         # TODO: Implement
#     return wrapper

# Complete the code, so it works as expected.


#                             Examples

# Test Code                                                   Output

# @even_numbers
# def get_numbers(numbers):
#     return numbers                                          [2, 4]

# print(get_numbers([1, 2, 3, 4, 5]))



def even_numbers(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el % 2 == 0]
    return wrapper



@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))