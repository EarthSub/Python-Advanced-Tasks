# You are commanding a spaceship navigating through uncharted space in search of Planet B.
# The journey is perilous, with meteorites that drain your resources and the constant danger of running out of fuel.
# Your mission is to reach Planet B and save humanity.

# You will be given an integer N representing the size of the space field,
# which is a square grid (each position on the grid represents a sector of space).
# On the next N lines, you will receive the rows of the space grid with symbols,
#     separated by a single space (" "). See the Examples section.

#     · Your spaceship starts at a random position, marked by 'S'.
#     · Meteorites are scattered across space, marked by 'M'.
#         o Each time you pass through a meteorite sector, your resources are decreased by 5 units.
#     · Planet B, your destination, is marked by 'P'.
#     · There are space stations, marked by 'R' (for "Resources").
#         o Where you can refuel and gain 10 units of resources (up to a maximum of 100 units).
#     · All other sectors are empty and marked by '.'.

# Mission Rules:

#     · Your mission is to reach Planet B ('P') with the resources you have and gain during the journey.
#     · Your spaceship starts with 100 units of resources initially at a position, marked by 'S'.
#         o When the spaceship makes the first move, its starting position is marked by '.'.
#     · You will be given commands to move the spaceship.
#         o The valid commands are: "up", "down", "left", and "right".
#     · Each move decreases your resources by 5 units.
#         o If the spaceship moves to a sector with a space station ('R'), you gain 10 units of resources, and the station remains in place.
#     § You can refuel at the same station each time you encounter it. But your resources cannot go above 100 units.
#         If they do, set them to 100.
#         o If the spaceship moves into a sector with a meteorite ('M'), an additional 5 units are subtracted from your resources,
#             and the meteorite is destroyed by the collision (replaced by '.').
#         o If your resources drop below 5 units before reaching Planet B or a space station to refuel, the mission fails,
#             and the spaceship is stranded in space.
#     § Remember the last known position of the spaceship.
#         o If the spaceship moves out of the grid's boundaries, it is considered lost in space and the mission ends immediately with a failure.
#     § Remember the last known position of the spaceship before moving out of boundaries.

# Input

#     · On the first line, you will receive an integer N (the size of the square grid).
#     · The next N lines will represent the grid, with each sector marked as 'S', 'M', 'P', 'R', or '.'.
#         o Letters 'S'and 'P'appear only once. o Symbols are separated by a single space (" "). See the Examples section.
#     · After the grid, a series of valid movement commands will follow, each on a new line.

# Output

#     · On the first line:
#         o If the spaceship reaches Planet B with zero or more resources, print:
#     § "Mission accomplished! The spaceship reached Planet B with {resources} resources left."
#         o If the spaceship runs out of resources before reaching Planet B or a space station, print:
#     § "Mission failed! The spaceship was stranded in space."
#         o If the spaceship exits the grid's boundaries and gets lost in space, print:
#     § "Mission failed! The spaceship was lost in space."
#     · On the next lines:
#         o Print the final state of the grid, with the spaceship's last known position marked by 'S'.
#     § If the spaceship successfully landed on Planet B, it is not displayed on the grid. § Symbols should be separated by a single space (" "). See the Examples section.

# Constraints

#     · The size of the square matrix (grid) will be between [2 -10] inclusive.
#     · Each sector will be marked as 'S', 'M', 'P', 'R', or '.'.
#         o Letters 'S'and 'P'appear only once.
#     · There will always be enough commands to either succeed or fail the mission.
#     · The spaceship starts with 100 units of resources initially.


#          Examples

# Input               Output

# 3                   Mission accomplished! The spaceship reached Planet B with 85
# S . .               resources left.
# . M .               . . .
# . R P               . . .
# right               . R P
# down
# down
# right


#          Comment

# The spaceship starts at (0,0) with 100 units of resources.
# There is one meteorite ('M') at (1,1), and a space station ('R') at (2,1).
# Planet B ('P') is located at (2,2).
# Moves:
# Move 1 (right): The spaceship moves to (0,1), -5 units for the move (95 remaining).
# Move 2 (down): The spaceship moves to (1,1), hitting the meteorite, -5 units for the move and -5 units for the
# meteorite (85 remaining). The meteorite is replaced by '.'.

# Move 3 (down): The spaceship moves to (2,1), -5 units for the move (80 remaining), and refuels at the space
# station, gaining +10 units (90 remaining).

# Move 4 (right): The spaceship moves to Planet B (2,2), -5 units for the move (85 remaining). Mission accomplished!


size = int(input())
space_grin = [input().split() for _ in range(size)]

ship = []
for row in range(size):
    for col in range(size):
        if space_grin[row][col] == "S":
            ship = [row, col]
            space_grin[row][col] = "."
            break

fuel = 100
moves = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

while True:
    if fuel < 5:
        print("Mission failed! The spaceship was stranded in space.")
        space_grin[ship[0]][ship[1]] = "S"
        break

    fuel -= 5
    command = input()
    r = ship[0] + moves[command][0]
    c = ship[1] + moves[command][1]

    if 0 <= r < size and 0 <= c < size:
        ship = [r, c]
        if space_grin[r][c] == "R":
            fuel = min(100, fuel + 10)
        elif space_grin[r][c] == "M":
            fuel -= 5
            space_grin[r][c] = "."
        elif space_grin[r][c] == "P":
            print(f"Mission accomplished! The spaceship reached Planet B with {fuel} resources left.")
            break
    else:
        print("Mission failed! The spaceship was lost in space.")
        space_grin[ship[0]][ship[1]] = "S"
        break


[print(*row) for row in space_grin]
