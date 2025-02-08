# Write a function called operate that receives an operator ("+", "-", "*" or "/") as а first argument and multiple numbers (integers) as
# additional arguments (*args). The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.

# Submit only your function in the Judge system.

# Note: Be careful when you have multiplication and division


#                                         Examples

# Test Code                               Output                          Comment

# print(operate("+", 1, 2, 3))            6                               1 + 2 + 3 = 6

# Test Code                               Output                          Comment

# print(operate("*", 3, 4))               12                              3 * 4 = 12


def operate(operator, *args):
    result = ""
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == "*":
        result = args[0]
        for num in args[1:]:
            result *= num
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Division by zero is not allowed."
            result /= num
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))