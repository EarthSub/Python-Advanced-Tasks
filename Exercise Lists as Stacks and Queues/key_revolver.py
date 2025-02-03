# Our favorite super-spy action hero Sam is back from his vacation, and it is time to go on a mission.
# He needs to unlock a safe locked by several locks in a row, which all have varying sizes.

# The hero possesses a special weapon called the Key Revolver, with special bullets.
# Each bullet can unlock a lock with a size equal to or larger than the size of the bullet.
# The bullet goes into the keyhole, then explodes, completely destroying it.
# Sam doesn't know the size of the locks, so he needs to just shoot at all of them until the safe runs out of locks.

# What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze,
# keeps his top-secret Georgian Chacha Brandy recipe inside.
# It's valued differently across different times of the year, so Sam's boss will tell him what it('s worth over the radio.
# One last thing, every bullet Sam fires will also cost him money, which will be deducted from his pay from the price of the intelligence.)

# Good luck, operative.

# Input

#     · On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
#     · On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
#     · On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
#     · On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
#     · On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]

# After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back while going through the bullets back-to-front.
# If he successfully destroyed a lock, print "Bang!", then remove the lock. If not, print "Ping!", leaving the lock intact. The bullet is removed in both cases.

# If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. If there aren't any bullets left, don't print it.

# The program ends when Sam runs out of bullets or the safe runs out of locks.

# Output

#     · If Sam manages to open the safe, print: "{bullets_left} bullets left. Earned ${money_earned}"
#     · Otherwise, print: "Couldn't get through. Locks left: {locks_left}"

# Make sure to include the price of the bullets when calculating the money earned.

# Constraints

#     · The input will be within the constraints specified above and will always be valid. There is no need to check it explicitly.
#     · There will never be a case where Sam breaks the lock and ends up with а negative balance.


#                                     Examples

# Input                               Output                              Comments

# 50                                  Ping!                               20 shoots lock 15 (ping)
# 2                                   Bang!                               10 shoots lock 15 (bang)
# 11 10 5 11 10 20                    Reloading!                          11 shoots lock 13 (bang)
# 15 13 16                            Bang!                               5 shoots lock 16 (bang)
# 1500                                Bang!                               Bullets' cost: 4 * 50 = $200
#                                     Reloading!                          Earned: 1500 – 200 = $1300
#                                     2 bullets left. Earned $1300

# Input                               Output                              Comments

# 20                                  Bang!                               5 shoots lock 13 (bang)
# 6                                   Ping!                               10 shoots lock 3 (ping)
# 14 13 12 11 10 5                    Ping!                               11 shoots lock 3 (ping)
# 13 3 11 10                          Ping!                               12 shoots lock 3 (ping)
# 800                                 Ping!                               13 shoots lock 3 (ping)
#                                     Ping!                               14 shoots lock 3 (ping)
#                                     Couldn't get through. Locks left: 3

# Input                               Output                              Comments

# 33                                  Bang!                               10 shoots lock 10 (bang)
# 1                                   Reloading!                          11 shoots lock 20 (bang)
# 12 11 10                            Bang!                               12 shoots lock 30 (bang)
# 10 20 30                            Reloading!                          Bullets' cost: 3 * 33 = $99
# 100                                 Bang!                               Earned: 100 – 99 = $1
#                                     0 bullets left. Earned $1


from collections import deque

price_for_bullet = int(input())
size_of_a_barrel = int(input())
number_of_bullets = [int(n) for n in input().split()]
locks = deque(int(n) for n in input().split())
intelligence = int(input())

number_of_shots_fired = 0
current_barrel_size = size_of_a_barrel
while number_of_bullets and locks:
    bullet_size = number_of_bullets.pop()
    if bullet_size <= locks[0]:
        locks.popleft()
        current_barrel_size -= 1
        number_of_shots_fired +=1
        print("Bang!")
    else:
        current_barrel_size -= 1
        number_of_shots_fired += 1
        print("Ping!")
    if current_barrel_size == 0 and number_of_bullets:
        current_barrel_size = size_of_a_barrel
        print("Reloading!")


bullets_price = number_of_shots_fired * price_for_bullet
money_earned = intelligence - bullets_price

if not locks:
    print(f"{len(number_of_bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
