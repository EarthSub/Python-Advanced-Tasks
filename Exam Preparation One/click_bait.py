# Main Idea

# Your task is to simulate a "content optimization" process for a website using two sequences of scores and design
# an algorithm for a website to process user engagement on two types of content:

#     ⦁	Suggested Links - processed using the FIFO principle
#     ⦁	Featured Articles - processed using the LIFO principle

# You must follow specific rules to process the elements and calculate an Engagement Value,
# which determines if the target goal is achieved.

# Input Data

#     ⦁	The first line contains space-separated integers representing the engagement scores of Suggested Links
#     ⦁	The second line contains space-separated integers representing the popularity scores of Featured Articles
#     ⦁	The third line contains a single integer - the Target Engagement Value

# Rules

# You should repeatedly perform the following steps until one of the sequences becomes empty:

# Take one element from each sequence:

#     ⦁	Take the first element from the Suggested Links
#     ⦁	Take the last element from the Featured Articles

# Compare the two elements:

#     ⦁	Identify the greater element and the smaller element
#     ⦁	Remember the sequence of origin of the greater element, you will need it later

# Calculations:

#     ⦁	Find the remainder between the two elements. The greater element will be used as a dividend and the smaller as a divisor using a ⦁	Modulo Operation
#     ⦁	If the greater element is from the Featured Articles (LIFO) collection:
#         ⦁	Add the remainder to the Final Feed Collection as a positive element
#         ⦁	Double the remainder and return the result to the LIFO collection (at the end). If the remainder equals zero, skip this operation and proceed with the next calculation
#     ⦁	If the greater element is from the Suggested Links (FIFO) collection:
#         ⦁	Add the remainder to the Final Feed Collection as a negative element
#         ⦁	Double the remainder and return the result to the FIFO collection (at the end). If the remainder equals zero, skip this operation and proceed with the next calculation
#     ⦁	If elements are equal add zero (0) to the Final Feed Collection and do not return anything to the LIFO or FIFO collections

# After processing:

# Find the Total Engagement Value as a sum of all elements in the Final Feed Collection.

#     ⦁	If the Total Engagement Value is greater than or equal to the Target Engagement Value, the goal has been achieved. See the Examples section
#     ⦁	If the Total Engagement Value is less than the Target Engagement Value, the goal has not been achieved
#         ⦁	Calculate how far short the Total Engagement Value is from the target by subtracting the Total Engagement Value from the Target Engagement Value: Shortfall = Target - Total

# Print the Final Feed collection on the Console, comma, and space separated (", ").
# Print the appropriate output for the engagement value on the Console. See the Examples section.

# Input

#     ⦁	On the first line, you will receive a sequence of integers, representing the engagement scores of
#     Suggested Links, space separated (" ")
#     ⦁	On the second line, you will receive a sequence of integers, representing the popularity scores of
#     Featured Articles, space separated (" ")
#     ⦁	On the third line, you will receive a single integer representing the Target Engagement Value

# Output

#     ⦁	Print the Final Feed Collection:
#     "Final Feed: {element1}, {element2} … {elementn}"
#     ⦁	Calculate the Total Engagement Value:
#         ⦁	If the Total Engagement Value is greater than or equal to the target, print:
#         "Goal achieved! Engagement Value: {total_engagement_value}"
#         ⦁	If the Total Engagement Value is less than the target (Shortfall = Target - Total), print:
#         "Goal not achieved! Short by: {shortfall}"

# Constraints

#     ⦁	Always process elements in the order described
#     ⦁	All of the given numbers will be valid integers in the range [1-1000]
#     ⦁	Use modulo operation (%) to calculate the remainder
#     ⦁	Pay attention to the sign of the remainder in the Final Feed
#     ⦁	Both sequences will initially have at least one element.


#                     Examples

# Input	                                Output

# 25 10                                   Final Feed: 5, 0
# 40 30                                   Goal not achieved! Short by: 30
# 35
#                     Comment

# First round: Take 25 from the Featured Articles and 30 from the Suggested Links. The greater value is 30,
# the smaller value is 25, and the remainder is 30%25 = 5. Add +5 to the Final Feed
# (positive because the greater element is from the LIFO collection).
# Double the Remainder: 5×2=10, and return it to the original collection - LIFO collection.
# Collections updated state:
# Featured Articles: [10]
# Suggested Links: [40,10]
# Final Feed: [5]
# Second Round: Take 10 from the Featured Articles and 10 from the Suggested Links.
# There is no greater or smaller value. Add 0 to the Final Feed.
# Skip the step for returning the doubled remainder to the original collection as it equals zero (0×2=0).
# Collections updated state:
# Featured Articles: []
# Suggested Links: [40]
# Final Feed: [5,0]
# The Featured Articles collection is empty, so the program ends and the result is printed on the console.

# Input	                                Output

# 45 65 35 25 70                          Final Feed: -5, 0, -5, -5, -10, 5, 0
# 15 30 20 10 5 40                        Goal not achieved! Short by: 75
# 55

# Input	                                Output

# 12 18 971 65 31                         Final Feed: 9, 0, -3, 45, 28, 2
# 1 3 121 500 4 33                        Goal achieved! Engagement Value: 81
# 80

# Input	                                Output

# 77 233 12 66 6 34                       Final Feed: -11, 67, 2, -2, 0, -10, 0
# 1 12 900 999 33                         Goal achieved! Engagement Value: 46
# 26


from collections import deque


suggested_links = deque(int(n) for n in input().split())
featured_articles = [int(n) for n in input().split()]
target = int(input())

final_feed_collection = []
while suggested_links and featured_articles:
    if featured_articles[-1] > suggested_links[0]:
        remainder = featured_articles.pop() % suggested_links.popleft()
        final_feed_collection.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)
    elif featured_articles[-1] < suggested_links[0]:
        remainder = suggested_links.popleft() % featured_articles.pop()
        final_feed_collection.append(-abs(remainder))
        if remainder != 0:
            suggested_links.append(remainder * 2)
    else:
        suggested_links.popleft()
        featured_articles.pop()
        final_feed_collection.append(0)

total = sum(final_feed_collection)

print(f"Final Feed: {', '.join(str(el) for el in final_feed_collection)}")

if total >= target:
    print(f"Goal achieved! Engagement Value: {total}")
else:
    print(f"Goal not achieved! Short by: {target - total}")
