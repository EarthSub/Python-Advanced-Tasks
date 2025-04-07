# Paul is extremely passionate about football.
# He can't wait to meet his friends every day after school and enjoy his favorite game together.

# On the first line, you will be given a sequence of integers representing the values of strength required to kick the ball.

# In the next line, you will be given another sequence of integers representing the values of accuracy needed to direct the ball.
# See the Examples section below.

# Until there are strengths and accuracies available, the program continues running.
# You need to sum the last strength and the first accuracy, then compare the result (see the Examples section):

#     · If the sum of the strength and the accuracy is equal to 100, there is a goal:
#         o Remove both values (the strength and the accuracy) from their sequences.
#         o You should keep track of the scored goals in total:
#             § Increase total scored goals by 1 (one).
#     · If the sum of the strength and the accuracy is less than 100:
#         o If the value of the strength is smaller than the value of the accuracy:
#             § Remove the value of the strength from the sequence.
#         o If the value of the strength is greater than the value of the accuracy:
#             § Remove the value of the accuracy from the sequence.
#         o If both values are equal (strength = accuracy):
#             § Sum the strength and accuracy values (strength + accuracy).
#               Return the summation result to the strength sequence (at its initial position).
#             § Remove the accuracy.
#         · If the sum of the strength and the accuracy is greater than 100:
#         o Decrease the strength value by 10. Return it to the strength sequence (at its initial position).
#         o Move the accuracy value to the end of the accuracy sequence.

# Input / Constraints

#     · On the first line, you will receive integers representing the values of the strength, separated by a single space.
#     · On the second line, you will receive integers representing the values of the accuracy, separated by a single space.
#     · The size of the two sequences may differ.
#     · All given numbers will be valid integers in the range [10 - 90] and are divisible only by 10.

# Output

# The output of your program should be printed on the Console, on separate lines, formatted according to the following rules:

#     · If Paul succeeded in scoring of exactly 3 (three) goals:
#         o "Paul scored a hat-trick!"
#     · If Paul failed to score a single goal:
#         o "Paul failed to score a single goal."
#     · If Paul scored more than 3 (three) goals:
#         o "Paul performed remarkably well!"
#     · If Paul scored more than 0 (zero) but less than 3 (three) goals:
#         o "Paul failed to make a hat-trick."
#     · Finally, print the total goals scored by Paul if there are any:
#         o "Goals scored: {total goals}"
#     · At the end of the program
#         o If there are any values in the strength sequence, print:
#             § "Strength values left: {strenght1}, {strenght2}, (…),{strenghtn}"
#         o If there are any values in the accuracy sequence, print:
#             § "Accuracy values left: {accuracy1}, {accuracy2}, (…),{accuracyn}"
#         o If there are no values in one or both sequences, skip the printing.


#                             Examples

# Input                       Output                                  Comment

# 10 20 30 40 90              Paul scored a hat-trick!                The first pair consists of the last strength with a
# 20 70 20 30 60              Goals scored: 3                         value of 90 and the first accuracy with a value of
#                             Strength values left: 10, 20            20. The sum (90+20 = 110) is greater than 100, so
#                                                                     we decrease the value of the strength by 10 and
#                                                                     move the accuracy value to the end of its
#                                                                     sequence.
#                                                                     Now, the sequences are as follows:
#                                                                     10 20 30 40 80
#                                                                     70 20 30 60 20
#                                                                     We repeat the same operation.
#                                                                     80+70 = 150 ->
#                                                                     10 20 30 40 70
#                                                                     20 30 60 20 70
#                                                                     70+20 = 90 -> The sum of the two elements is less
#                                                                     than 100 and the strength value is greater than
#                                                                     the accuracy value, so we remove the accuracy
#                                                                     value. Now, the sequences are as follows:
#                                                                     10 20 30 40 70
#                                                                     30 60 20 70
#                                                                     70+30 = 100 -> The sum is equal to 100. Paul
#                                                                     scores a goal we add it to the total scored goals
#                                                                     and both values are removed from the
#                                                                     sequences. Now, the sequences are as follows:
#                                                                     10 20 30 40
#                                                                     60 20 70
#                                                                     40+60 = 100 -> One more goal is scored. We add
#                                                                     it to the total goals and remove both values
#                                                                     again. Now, the sequences are as follows:
#                                                                     10 20 30
#                                                                     20 70
#                                                                     30+20 = 50 -> Less than 100, accuracy less than
#                                                                     strength, we remove the accuracy value. Now,
#                                                                     the sequences are as follows:
#                                                                     10 20 30
#                                                                     70
#                                                                     30+70 = 100 -> Goal!
#                                                                     Since there are no more elements in the
#                                                                     accuracy sequence, the program ends. The
#                                                                     correct output is printed on the Console.

# Input                       Output                                  Comment

# 10 20 30 40                 Paul performed remarkably well!         40+60 = 100 -> Goal!
# 60 70 80 90                 Goals scored: 4                         Sequences look like this after this turn:
#                                                                     10 20 30
#                                                                     70 80 90
#                                                                     30+70 = 100 -> Goal!
#                                                                     10 20
#                                                                     80 90
#                                                                     20+80 = 100 -> Goal!
#                                                                     10
#                                                                     90
#                                                                     10+90 = 100 -> Goal!
#                                                                     Since there are no more elements in both
#                                                                     sequences, the program ends. The correct output
#                                                                     is printed on the Console.

# Input                       Output                                  Comment

# 10 10 10                    Paul failed to make a hat-trick.        10+10 = 20 -> The sum if less than 100. Since
# 10 10 90                    Goals scored: 1                         both values are equal, we take the value of the
#                             Strength values left: 10, 10            strength, increase it by the value of the accuracy
#                                                                     put it back on the top of the sequence, and
#                                                                     remove the value of accuracy.
#                                                                     Now, the sequences are as follows:
#                                                                     10 10 20
#                                                                     10 90
#                                                                     20+10 = 30 -> The sum is less than 100 and the
#                                                                     strength value is greater than the accuracy
#                                                                     value. We remove the accuracy value. Now, the
#                                                                     sequences are as follows:
#                                                                     10 10 20
#                                                                     90
#                                                                     20+90 = 110 -> The sum is greater than 100 and
#                                                                     we take the strength value, decrease it by 10
#                                                                     and put it back on the top of the sequence.
#                                                                     Since there is only one element in the accuracy
#                                                                     sequence, we do not move it. Now, the
#                                                                     sequences are as follows:
#                                                                     10 10 10
#                                                                     90
#                                                                     10+90 = 100 -> Goal! We add it to the total
#                                                                     goals scored by Paul and remove both elements
#                                                                     from their sequences.
#                                                                     Since there are no more elements in the
#                                                                     accuracy sequence, the program ends. The
#                                                                     correct output is printed on the Console.

# Input                       Output                                  Comment

# 10 30 10                    Paul failed to score a single           10+10 = 20 ->
# 10 10 10                    goal.                                   10 30 20
#                             Strength values left: 10, 30, 20        10 10
#                                                                     0+10 = 30 ->
#                                                                     10 30 20
#                                                                     10
#                                                                     20+10 = 30 ->
#                                                                     Since there are no more elements in the
#                                                                     accuracy sequence, the program ends. The
#                                                                     correct output is printed on the Console.



from collections import deque


strength = [int(s) for s in input().split()]
accuracy = deque(int(a) for a in input().split())

goals_scored = 0

while strength and accuracy:
    if strength[-1] + accuracy[0] == 100:
        strength.pop()
        accuracy.popleft()
        goals_scored += 1
    elif strength[-1] + accuracy[0] < 100:
        if strength[-1] < accuracy[0]:
            strength.pop()
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        elif strength[-1] == accuracy[0]:
            strength[-1] += accuracy[0]
            accuracy.popleft()
    elif strength[-1] + accuracy[0] > 100:
        strength[-1] -= 10
        accuracy.rotate(-1)

if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
elif goals_scored > 3:
    print("Paul performed remarkably well!")
elif 0 < goals_scored < 3:
    print("Paul failed to make a hat-trick.")

if goals_scored:
    print(f"Goals scored: {goals_scored}")

if strength:
    print(f"Strength values left: {', '.join(str(s) for s in strength)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(str(a) for a in accuracy)}")
