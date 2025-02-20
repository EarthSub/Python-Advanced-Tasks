# Write a function named math_operations that receives a different number of floats as arguments and 4 keyword arguments.
# The keys will be single letters: "a", "s", "d", and "m", and the values will be numbers.

# You need to take each float argument from the sequence and do mathematical operations as follows:

#     · The first element should be added to the value of the key "a"
#     · The second element should be subtracted from the value of the key "s"
#     · The third element should be divisor to the value of the key "d"
#     · The fourth element should be multiplied by the value of the key "m"
#     · Each result should replace the value of the corresponding key
#     · You must repeat the same steps consecutively until you run out of numbers

# Beware: You cannot divide by 0. If the operation could throw an error, you should skip the operation and continue to the next one.

# After you finish calculating all numbers, sort the four elements by their values in descending order.
# If two or more values are equal, sort them by their keys in ascending order (alphabetically).

# In the end, return each key-value pair in the format "{key}: {value}" on separate lines.
# Each value should be formatted to the first decimal point.

# For more clarifications, see the examples below.


#                                         Examples

# Test Code                                                                               Output

# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,                   d: 33.0
# d=33, m=15))                                                                            s: 15.1
#                                                                                         a: 9.1
#                                                                                         m: -58.5

# Test Code                                                                               Output

# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-                   a: 5.1
# 2.3), d=0, m=0))                                                                        d: 0.0
#                                                                                         m: 0.0
#                                                                                         s: 0.0

# Test Code                                                                               Output

# print(math_operations(6.0, a=0, s=0, d=5, m=0))                                         a: 6.0
#                                                                                         d: 5.0
#                                                                                         m: 0.0
#                                                                                         s: 0.0


def math_operations(*args, **kwargs):
    for arg in range(len(args)):
        if arg % 4 == 0:
            kwargs["a"] += args[arg]
        elif arg % 4 == 1:
            kwargs["s"] -= args[arg]
        elif arg % 4 == 2:
            if args[arg] != 0:
                kwargs["d"] /= args[arg]
        elif arg % 4 == 3:
            kwargs["m"] *= args[arg]
    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{key}: {value:.1f}" for key, value in result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))