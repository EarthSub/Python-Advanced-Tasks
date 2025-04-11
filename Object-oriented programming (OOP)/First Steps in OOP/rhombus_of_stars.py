# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:


            # Examples

# Input                   Output

# 1                       *

# Input                   Output

# 2                       *
#                        * *
#                         *

# Input                   Output

# 3                       *
#                        * *
#                       * * *
#                        * *
#                         *

# Input                   Output

# 4                       *
#                        * *
#                       * * *
#                      * * * *
#                       * * *
#                        * *
#                         *



def print_row(n, star_count):
    for row in range(n - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


n = int(input())

for stars_count in range(1, n):
    print_row(n, stars_count)
for stars_count in range(n, 0, -1):
    print_row(n, stars_count)