# There is a party at SoftUni. Many guests are invited, and there are two types of them:
# Regular and VIP. When a guest comes, check if they exist on any of the two reservation lists.

# On the first line, you will receive the number of guests – N.
# On the following N lines, you will be receiving their reservation codes.
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit.
# Keep in mind that all reservation numbers must be unique.

# After that, you will be receiving guests who came to the party until you read the "END" command.

# In the end, print the number of guests who did not come to the party and their reservation numbers:

#     · The VIP guests must be first.
#     · Both the VIP and the Regular guests must be sorted in ascending order.

#                          Examples

# Input           Output              Input           Output

# 5               2                   6               3
# 7IK9Yo0h        7IK9Yo0h            m8rfQBvl        7ugX7bm0
# 9NoBUajQ        tSzE5t0p            fc1oZCE0        UgffRkOn
# Ce8vwPmE                            UgffRkOn        m8rfQBvl
# SVQXQCbc                            7ugX7bm0
# tSzE5t0p                            9CQBGUeJ
# 9NoBUajQ                            2FQZT3uC
# Ce8vwPmE                            2FQZT3uC
# SVQXQCbc                            9CQBGUeJ
# END                                 fc1oZCE0
#                                     END


number_of_guests = int(input())

vip = set()
regular = set()

for _ in range(number_of_guests):
    guest = input()
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

guests_in_party = input()

while guests_in_party != "END":
    if guests_in_party in vip:
        vip.remove(guests_in_party)
    elif guests_in_party in regular:
        regular.remove(guests_in_party)
    guests_in_party = input()

print(len(vip) + len(regular))
for guest in sorted(vip):
    print(guest)
for guest in sorted(regular):
    print(guest)

