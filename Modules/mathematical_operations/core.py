

mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Cannot be divided by zero!",
    "^": lambda a, b: a ** b,
}


def execute(num1, sign, num2):
    function = mapper[sign]
    return function(num1, num2)