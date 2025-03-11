# You are given a file called numbers.txt with the following content:

# 1
# 2
# 3
# 4
# 5

# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.


result = 0

with open("numbers.txt") as num:
    content = num.read().split("\n")
    for line in content:
        result += int(line)

print(result)
