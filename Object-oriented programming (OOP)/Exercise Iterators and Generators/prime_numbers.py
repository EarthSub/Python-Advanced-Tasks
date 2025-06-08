# Create a generator function called get_primes() which should receive a list of integer numbers and
# return a list containing only the prime numbers from the initial list.
#
#
#                                     Examples
#
# Test Code                                                                       Output
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))                               [2, 3, 5]
#
# Test Code                                                                       Output
#
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))                                    []



from math import sqrt


def get_primes(numbers):
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))
