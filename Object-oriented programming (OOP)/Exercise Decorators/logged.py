# Create a decorator called logged. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called. See the examples for more clarification.

# Hints

#     · Use {func}.__name__ to get the name of the function
#     · Call the function to get the result
#     · Return the result

#                             Examples

# Test Code                                               Output


# @logged                                                 you called func(4, 4, 4)
# def func(*args):                                        it returned 6
#     return 3 + len(args)
# print(func(4, 4, 4))

# Test Code                                               Output

# @logged                                                 you called sum_func(1, 4)
# def sum_func(a, b):                                     it returned 5
#     return a + b
# print(sum_func(1, 4))




def logged(function):
    def wrapper(*args):
        result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {result}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

print()

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
