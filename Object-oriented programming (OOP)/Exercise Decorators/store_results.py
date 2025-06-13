# Create a class called store_results. It should be used as a decorator and store information about the
# executed functions in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"


#                         Examples

# Test Code                                       results.txt

# @store_results                                  Function 'add' was called. Result: 4
# def add(a, b):                                  Function 'mult' was called. Result: 24
#     return a + b

# @store_results
# def mult(a, b):
#     return a * b

# add(2, 2)
# mult(6, 4)



class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as file:
            result = self.function(*args, **kwargs)
            file.write(f"Function '{self.function.__name__}' was called. Result: {result}\n")

        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)