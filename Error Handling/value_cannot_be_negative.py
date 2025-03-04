# Create your own exception called ValueCannotBeNegative.
# Write a program that reads five numbers from the console (on separate lines).
# If a negative number occurs, raise the exception.


#              Examples

# Input                       Output

# 1                           Traceback (most recent call last):
# 4                               File ".\value_cannot_be_negative.py", line 8, in <module>
# -5                                  raise ValueCannotBeNegative
# 3                           __main__.ValueCannotBeNegative
# 10


class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
