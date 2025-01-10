# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid.
# Every nth toss, the child holding the potato leaves the game. When a kid leaves the game,
# it passes the potato to the next kid. It continues until there is only one kid left.

# Create a program that simulates the game of Hot Potato. On the first line,
# you will receive kids names, separated by a single space. On the second line,
# you will receive the nth toss (integer) in which a child leaves the game.

# Print every kid who is removed from the circle in the format "Removed {kid}". In the end,
# print the only kid left in the format "Last is {kid}".


#                             Examples

# Input                                                       Output

# Tracy Emily Daniel                                          Removed Emily
# 2                                                           Removed Tracy
#                                                             Last is Daniel

# George Peter Michael William Thomas                         Removed Thomas
# 10                                                          Removed Peter
#                                                             Removed Michael
#                                                             Removed George
#                                                             Last is William

# Removed Michael Removed George Last is William              Removed George
# 1                                                           Removed Peter
#                                                             Removed Michael
#                                                             Removed William
#                                                             Last is Thomas


#        example 1

from collections import deque

children_names = deque(input().split())
toss = int(input())

while len(children_names) != 1:
    for child in range(toss - 1):
        children_names.append(children_names.popleft())
    print(f"Removed {children_names.popleft()}")

print(f"Last is {''.join(children_names)}")


#        example 2

children_names = deque(input().split())
toss = int(input()) - 1

while len(children_names) > 1:
    children_names.rotate(-toss)
    removed_child = children_names.popleft()
    print(f"Removed {removed_child}")

print(f"Last is {children_names[0]}")
