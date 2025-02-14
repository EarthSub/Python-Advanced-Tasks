# Create a function called func_executor() that can receive a different number of tuples,
# each of which will have exactly 2 elements: the first will be a function,
# and the second will be a tuple of the arguments that need to be passed to that function.
# You should execute each function and return its result in the format:

# "{function name} - {function result}"

# For more clarification, see the examples below.


#                             Examples

# Test Code                                               Output

# def sum_numbers(num1, num2):                            sum_numbers - 3
#     return num1 + num2                                  multiply_numbers - 8
# def multiply_numbers(num1, num2):
#     return num1 * num2

# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))


# Test Code                                               Output

# def make_upper(*strings):                               make_upper - ('PYTHON', 'SOFTUNI')
#     result = tuple(s.upper() for s in strings)          make_lower - ('python', )
#     return result

# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result

# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))


def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")
    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))