# There is a robotics factory. The current project is assembly-line robots.

# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free, it should take a product for processing and log its name, product, and processing start time.

# Each robot processes a product coming from the assembly line.
# A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
# If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.

# The robots are standing in line in the order of their appearance.

# Input

#     · On the first line, you will receive the robots' names and their processing times in the format:
#       "robotName-processTime;robotName-processTime;robotName-processTime..."
#     · On the second line, you will get the starting time in the format "hh:mm:ss"
#     · Next, until the "End" command, you will get a product on each line.

# Output

#     · Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"


#                         Examples

# Input                                           Output

# ROB-15;SS2-10;NX8000-3                          ROB - detail [08:00:01]
# 8:00:00                                         SS2 - glass [08:00:02]
# detail                                          NX8000 - wood [08:00:03]
# glass                                           NX8000 - apple [08:00:06]
# wood
# apple
# End

# Input                                           Output

# ROB-8                                           ROB - detail [08:00:00]
# 7:59:59                                         ROB - wood [08:00:08]
# detail                                          ROB - glass [08:00:16]
# glass                                           ROB - sock [08:00:24]
# wood
# sock
# End


from collections import deque


robots_data = input().split(";")
robot_info = []
for robot in robots_data:
    robot_name, process_time = robot.split("-")
    robot_info.append({"name": robot_name, "time": int(process_time), "busy_until": 0})

hours, minutes, seconds = [int(n) for n in input().split(":")]
starting_time = (hours * 3600) + (minutes * 60) + seconds

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    current_product = products.popleft()
    starting_time += 1
    is_taken = False

    for robot in robot_info:
        if robot["busy_until"] <= starting_time:
            robot["busy_until"] = starting_time + robot["time"]
            h = starting_time // 3600
            m = (starting_time % 3600) // 60
            s = (starting_time % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)


