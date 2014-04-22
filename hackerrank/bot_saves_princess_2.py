#!/usr/bin/env python3

def displayPathtoPrincess(n, robot_loc, grid):
    # Find the princess.
    princess_loc = (-1, -1)

    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == "p":
                princess_loc = (i, j)
                break

    if princess_loc == (-1, -1): exit("ERROR: Could not find princess.")

    # Calculate distance from princess.
    x = robot_loc[1] - princess_loc[1]
    y = robot_loc[0] - princess_loc[0]

    if x == 0 and y == 0: return

    if x > 0: x_dir = "LEFT\n"
    else: x_dir = "RIGHT\n"

    if y > 0: y_dir = "UP\n"
    else: y_dir = "DOWN\n"

    if abs(x) >= abs(y): print(x_dir)
    else: print(y_dir)


m = int(input())
robot_loc = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, m):
    grid.append(list(input().strip()))

displayPathtoPrincess(m, robot_loc, grid)
