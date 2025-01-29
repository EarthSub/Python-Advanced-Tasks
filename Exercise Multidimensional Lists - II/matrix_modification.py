# Write a program that reads a matrix from the console and changes its values. On the first line,
# you will get the matrix's rows - N. You will get elements for each column on the following N lines,
# separated with a single space. You will be receiving commands in the following format:

#     · "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#     · "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.

# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in the range [0; len() – 1].
#
# When you receive "END", you should print the matrix and stop the program.


#                 Examples

# Input                           Output

# 3                               6 2 3
# 1 2 3                           4 3 6
# 4 5 6                           7 8 9
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# Input                           Output

# 4                               Invalid coordinates
# 1 2 3 4                         Invalid coordinates
# 5 6 7 8                         -41 2 3 4
# 8 7 6 5                         5 6 7 8
# 4 3 2 1                         8 7 6 5
# Add 4 4 100                     4 3 2 101
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END


rows = int(input())

matrix = [[int(n) for n in input().split()]for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    first_index, second_index, current_value = [int(n) for n in command[1:]]
    if 0 <= first_index < rows and 0 <= second_index < rows:
        if command[0] == "Add":
            matrix[first_index][second_index] += current_value
        elif command[0] == "Subtract":
            matrix[first_index][second_index] -= current_value
    else:
        print("Invalid coordinates")

for any_list in matrix:
    print(*any_list)


