# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with
# the given tag, and return the new result. For more clarification, see the examples below


#                             Examples

# Test Code                                               Output

# @tags('p')                                              <p>Hello you!</p>
# def join_strings(*args):
#     return "".join(args)
# print(join_strings("Hello", " you!"))

# Test Code                                               Output

# @tags('h1')                                             <h1>HELLO</h1>
# def to_upper(text):
#     return text.upper()
# print(to_upper('hello'))



def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
