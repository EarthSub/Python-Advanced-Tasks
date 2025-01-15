# Write a program, which will take a list of names and print only the unique names in the list.

# The order in which we print the result does not matter.


#                                       Examples

# Input           Output          Input           Output          Input           Output

# 8               Alan            7               Easton          6               Adam
# Lee             Joey            Lyle            Lyle            Adam
# Joey            Lee             Bruce           Alice           Adam
# Lee             Joe             Alice           Bruce           Adam
# Joe             Peter           Easton          Shawn           Adam
# Alan                            Shawn                           Adam
# Alan                            Alice                           Adam
# Peter                           Shawn
# Joey


num = int(input())

set_of_names = set()

for _ in range(num):
    current_name = input()
    set_of_names.add(current_name)

for name in set_of_names:
    print(name)
