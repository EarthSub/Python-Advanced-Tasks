# Write a program that gathers a sum of money using the least possible number of coins.
# This is the range of possible coin values:

#     · { 1, 2, 5, 10, 20, 50 }

# You will receive the desired sum. The goal is to reach the sum using as few coins as possible using a greedy approach.
# We'll assume that each coin value and the desired sum are integers.

# Input

#     · On the first line, you will receive the coins.
#     · On the next line, you will receive the target sum.


# Hints

# Greedy Approach

# In the context of this problem, a greedy algorithm employs a strategy to iteratively select the optimal coin values.
# It strives to choose the best possible coin value, starting with the largest and progressing to the next largest,
# until the desired sum is attained or there are no more coin values left. The number of coins to take for each value may vary.
# In scenarios where the desired sum is significantly larger than individual coin values,
# returning the result as a List[] could be inefficient and may even lead to exceptions.
# A more practical approach is to utilize a dictionary {key: int, value: int}, where the keys represent the coin values,
# and the values indicate the number of coins to take for each specified coin value. For example,
# if the coin values are {1} and the target sum is 42, instead of returning a list with 42 elements,
# a more efficient choice is to return a dictionary with a single key-value pair: {1, 42}.


#                                     Examples

# Input                               Output                                      Comments

# 1, 2, 5, 10, 20, 50                 Number of coins to take: 21                 18*50 + 1*20 + 1*2 +
# 923                                 18 coin(s) with value 50                    1*1 = 900 + 20 + 2 +
#                                     1 coin(s) with value 20                     1 = 923
#                                     1 coin(s) with value 2
#                                     1 coin(s) with value 1

# Input                               Output                                      Comments

# 1                                   Number of coins to take: 42
# 42                                  42 coin(s) with value 1

# Input                               Output                                      Comments

# 3, 7                                11                                          Cannot reach the
# 11                                                                              desired sum with
#                                                                                 these coin values

# Input                               Output                                      Comments

# 1, 2, 5                             Number of coins to take: 406230826          The solution should
# 2031154123                          406230824 coin(s) with value 5              be fast enough to
#                                     1 coin(s) with value 2                      handle a combination
#                                     1 coin(s) with value 1                      of small coin values
#                                                                                 and a large desired sum



def choose_coins(coins, target_sum):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while target_sum != 0 and index < len(coins):
        count_coins = target_sum // coins[index]

        target_sum %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if target_sum != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"
        for value, count in used_coins.items():
            result += f"{count} coin(s) with value {value}\n"
        return result.strip()


coin_input = input()
coins = list(map(int, coin_input.split(", ")))

target_sum = int(input())

result = choose_coins(coins, target_sum)
print(result)
