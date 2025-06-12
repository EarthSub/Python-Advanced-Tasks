# Create a decorator called type_check. It should receive a type (int/float/str/…),
# and it should check if the parameter passed to the decorated function is of the type given to the decorator.
# If it is, execute the function and return the result, otherwise return "Bad Type".


#                             Examples

# Test Code                                               Output

# @type_check(int)                                        4
# def times2(num):                                        Bad Type
#     return num*2

# print(times2(2))
# print(times2('Not A Number'))

# Test Code                                               Output

# @type_check(str)
# def first_letter(word):
#     return word[0]

# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))



def type_check(param_type):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, param_type):
                return "Bad Type"
            return func(param)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))

print()

@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
