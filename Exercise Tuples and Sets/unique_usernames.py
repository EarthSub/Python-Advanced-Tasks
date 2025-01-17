# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
# On the first line, you will receive an integer N. On the next N lines, you will receive a username.
# Print the collection on the console (the order does not matter):


#                                       Examples

# Input                   Output                      Input                   Output

# 6                       George                      10                      Peter
# George                  Peter                       Peter                   Maria
# George                  NiceGuy1234                 Maria                   George
# George                                              Peter                   Steve
# Peter                                               George                  Alex
# George                                              Steve
# NiceGuy1234                                         Maria
#                                                     Alex
#                                                     Peter
#                                                     Steve
#                                                     George


set_of_usernames = set()

for _ in range(int(input())):
    set_of_usernames.add(input())

# print("\n".join(set_of_usernames))
print(*set_of_usernames, sep="\n")


