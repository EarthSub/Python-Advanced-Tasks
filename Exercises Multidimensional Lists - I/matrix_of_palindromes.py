# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.

#     · Rows define the first and the last letter: row 0 à 'a', row 1 à 'b', row 2 à 'c', …
#     · Columns + rows define the middle letter:
#         o column 0, row 0 à 'a', column 1, row 0 à 'b', column 2, row 0 à 'c', …
#         o column 0, row 1 à 'b', column 1, row 1 à 'c', column 2, row 1 à 'd', …

# Input

#     · The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
#     · r and c are integers in the range [1, 26]


#          Examples

# Input               Output

# 4 6                 aaa aba aca ada aea afa
#                     bbb bcb bdb beb bfb bgb
#                     ccc cdc cec cfc cgc chc
#                     ddd ded dfd dgd dhd did

# Input               Output

# 3 2                 aaa aba
#                     bbb bcb
#                     ccc cdc


rows, columns = [int(n) for n in input().split()]

start = ord("a")

for row in range(rows):
    for col in range(columns):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=" ")
    print()