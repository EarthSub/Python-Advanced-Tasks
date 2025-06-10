# Having the following code:
#
#     def number_increment(numbers):
#         def increase():
#             # TODO: Implement return increase()
#         return increase()
#
# Complete the code, so it works as expected.
#
#
#                             Examples
#
# Test Code                                               Output
#
# print(number_increment([1, 2, 3]))                      [2, 3, 4]



def number_increment(numbers):
    def increase():
        return [num+1 for num in numbers]
    return increase()


print(number_increment([1, 2, 3]))