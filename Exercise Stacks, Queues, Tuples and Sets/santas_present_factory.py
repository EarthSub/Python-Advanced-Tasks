# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.

# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
# After that, you will be given another sequence of integers – their magic level.

# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:

#     Present                 Magic needed

#     Doll                    150
#     Wooden train            250
#     Teddy bear              300
#     Bicycle                 400

# You should take the last box with materials and the first magic level value to craft a toy.
# Their multiplication calculates the total magic level. If the result equals one of the levels described in the table above,
# you craft the present and remove both materials and magic value. Otherwise:

#     · If the product of the operation is a negative number, you should sum the values together,
#         remove them both from their positions, and add the result to the materials.
#     · If the product doesn('t equal one of the magic levels in the table and is a positive number,
#         remove only the magic value and increase the material value by 15.)
#     · If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.

# Stop crafting presents when you run out of boxes of materials or magic-level values.

# Your task is considered done if you manage to craft either one of the pairs:

#     · a doll and a train
#     · a teddy bear and a bicycle

# Input

#     · The first line of input will represent the values of boxes with materials - integers, separated by a single space
#     · On the second line, you will be given the magic values - integers again, separated by a single space

# Output

#     · On the first line - print whether you've succeeded in crafting the presents:
#         o "The presents are crafted! Merry Christmas!"
#         o "No presents this Christmas!"
#     · On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
#         o "Materials left: {material_N}, {material_N-1}, … {material_1}"
#         o "Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
#     · On the next lines print the presents you have crafted, ordered alphabetically in the format:
#         o "{toy_name1}: {amount}
#         {toy_name2}: {amount}
#         ...
#         {toy_nameN}: {amount}"

# Constraints

# · All the materials' values will be integers in the range [-100, 100]
# · Magic level values will be integers in the range [-100, 100]
# · In all cases, at least one present will be crafted


#                                 Examples

# Input                           Output                                  Comment

# 10 -5 20 15 -30 10              The presents are crafted!               First, we have 40*10=400, which is the
# 40 60 10 4 10 0                 Merry Christmas!                        needed magic for a bicycle. Remove both.
#                                 Materials left: 20, -5, 10              60*(-30) = -1800 (negative). 60+(-30) = 30.
#                                 Bicycle: 1                              Remove 60 and -30. Add 30 to materials.
#                                 Teddy bear: 2                           30*10=300 (bear). Remove both.
#                                                                         4*15=60, so remove 4, and the material is
#                                                                         increased by 15 (15+15=30).
#                                                                         10*30=300 (bear).
#                                                                         Print the desired text.

# 30 5 15 60 0 30                 No presents this Christmas!
# -15 10 5 -15 25                 Materials left: 20, 30
#                                 Doll: 1
#                                 Teddy bear: 1

# 30 10                           No presents this Christmas!
# 15 10 5 0 10                    Magic left: 5, 0, 10
#                                 Doll: 1
#                                 Teddy bear: 1


from collections import deque


materials = [int(n) for n in input().split()]
magic = deque([int(n) for n in input().split()])


presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}


while materials and magic:
    product = materials[-1] * magic[0]
    if product in presents:
        if presents[product] not in crafted_presents:
            crafted_presents[presents[product]] = 0
        crafted_presents[presents[product]] += 1
        materials.pop()
        magic.popleft()
    elif product < 0:
        materials.append(materials.pop() + magic.popleft())
    elif product not in presents and product > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 or magic[0] == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()
        continue

if ("doll" in crafted_presents and "Wooden train" in crafted_presents) or ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(mt) for mt in materials]))}")
if magic:
    print(f"Magic left: {', '.join([str(mg) for mg in magic])}")

for key, value in sorted(crafted_presents.items()):
    print(f"{key}: {value}")