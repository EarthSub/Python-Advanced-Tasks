# Write a program that draws the figure below depending on n.


#                          Examples

# Input           Output              Input           Output

# 2               **                  5               *****
#                 *                                   ****
#                 #                                   ***
#                 ##                                  **
#                                                     *
#                                                     #
#                                                     ##
#                                                     ###
#                                                     ####
#                                                     #####


def print_figure(n):
    if n <= 0:
        return

    # Pre-action: print n asterisks
    print('*' * n)

    # Recursive call
    print_figure(n - 1)

    # Post-action: print n hashtags
    print('#' * n)


n = int(input())
print_figure(n)
