# Having the following code:

# def vowel_filter(function):
#     def wrapper():
#         # TODO: Implement return wrapper
#     return wrapper

# Complete the code, so it works as expected:


#                             Examples

# Test Code                                                   Output

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]                        ["a", "e"]

# print(get_letters())



def vowel_filter(function):
    def wrapper():
        result = function()
        return [el for el in result if el.lower() in "aeuyoi"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

