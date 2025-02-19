# Write a function called fill_the_box that receives a different number of arguments representing:

#     · the height of a box
#     · the length of a box
#     · the width of a box
#     · different numbers - each representing the quantity of cubes. Each cube has an exact size of 1 x 1 x 1
#     · a string "Finish"

# Your task is to fill the box with the given cubes until the current argument equals "Finish"

# Input

#     · There will be no input. Just parameters passed to your function.

# Output

# The function should return a string in the following format:

#     · If, in the end, there is free space left in the box, print:
#         o "There is free space in the box. You could put {free space in cubes} more cubes."
#
#     · If there is no free space in the box, print:
#         o "No more free space! You have {cubes left} more cubes."


#                                         Examples

# Test Code                               Output                              Comment

# print(fill_the_box(2, 8,                There is free space in              The size of the box: 2 * 8 * 2 = 32
# 2, 2, 1, 7, 3, 1, 5,                    the box. You could put 13           We put the cubes consistently. In the
# "Finish"))                              more cubes.                         end, there is more free space left.

# Test Code                               Output                              Comment

# print(fill_the_box(5, 5,                No more free space! You             The size of the box: 5 * 5 * 2 = 50
# 2, 40, 11, 7, 3, 1, 5,                  have 17 more cubes.                 We put the cubes consistently. First, we
# "Finish"))                                                                  put 40 cubes and there is free space
#                                                                             left. Then we try to put 11 cubes, but
#                                                                             there is only space for 10.
#                                                                             Cubes left: 1 + 7 + 3 + 1 + 5 = 17

# Test Code                               Output

# print(fill_the_box(10, 10,              There is free space in
# 10, 40, "Finish", 2, 15,                the box. You could put
# 30)                                     960 more cubes.


def fill_the_box(h, l, w, *args):
    dimensions = h * l * w
    boxes_left = 0

    for arg in args:
        if arg == "Finish":
            break
        boxes_left += arg

    if dimensions > boxes_left:
        return f"There is free space in the box. You could put {dimensions - boxes_left} more cubes."
    return f"No more free space! You have {boxes_left - dimensions} more cubes."





print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(5, 5,
2, 40, 11, 7, 3, 1, 5,
"Finish"))

print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))