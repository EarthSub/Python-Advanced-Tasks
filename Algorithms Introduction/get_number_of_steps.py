def get_operations_count(n):
    counter = 0
    for i in range(n):
        for j in range(n):
            counter += 1
    return counter


print(get_operations_count(5))