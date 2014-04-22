#!/usr/bin/env python3

def displayPathtoPrincess(n,grid):
    robot_loc = (n // 2, n // 2)

    # Find the princess.
    princess_loc = (-1, -1)
    corners = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n -1)]

    for i, j in corners:
        if grid[i][j] == "p":
            princess_loc = (i, j)
            break

    # Calculate distance from princess.
    x = robot_loc[1] - princess_loc[1]
    y = robot_loc[0] - princess_loc[0]

    if x > 0: x_dir = "LEFT\n"
    else: x_dir = "RIGHT\n"

    if y > 0: y_dir = "UP\n"
    else: y_dir = "DOWN\n"

    print((x_dir * abs(x)) + (y_dir * abs(y)))


m = int(input())
grid = []
for i in range(0, m):
    grid.append(list(input().strip()))

displayPathtoPrincess(m,grid)
