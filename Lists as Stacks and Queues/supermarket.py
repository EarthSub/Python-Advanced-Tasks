# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program that reads lines of input consisting of a customer('s name and adds it to the end of
# a queue until "End" is received. If, in the meantime, you receive the command "Paid",
# you should print each customer in the order they are served (from the first to the last one) and empty the queue.)

# When you receive "End", you should print the count of the remaining
# people in the queue in the format: "{count} people remaining.".


#              Examples

# Input                       Output

# George                      George
# Peter                       Peter
# William                     William
# Paid                        4 people remaining.
# Michael
# Oscar
# Olivia
# Linda
# End

# Anna                        3 people remaining.
# Emma
# Alexander
# End


from collections import deque


queue = deque()

while True:
    client_name = input()
    if client_name == "End":
        break
    elif client_name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(client_name)

print(f"{len(queue)} people remaining.")
