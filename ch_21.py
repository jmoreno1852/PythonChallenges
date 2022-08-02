# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2

from math import sqrt


coord = [0, 0]  # x,y
dist = 0
while True:
    inp = input().split(" ")
    if inp[0] == "UP":
        coord[1] += int(inp[1])
    if inp[0] == "DOWN":
        coord[1] -= int(inp[1])
    if inp[0] == "LEFT":
        coord[0] -= int(inp[1])
    if inp[0] == "RIGHT":
        coord[0] += int(inp[1])
    if inp[0] == "":
        break
dist = round(sqrt(coord[0]**2 + coord[1]**2))
print(dist)
