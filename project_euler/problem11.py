#!/usr/bin/env python3

def prodlist(seq):
    if len(seq) == 0:
        return 0
    product = 1
    for s in seq:
        product *= int(s)
    return product

def maxprod(row, col, grid):
    products = []
    # Right
    if col < 17:
        products.append(prodlist(grid[row][col:col+4]))
    # Left
    if col > 2:
        products.append(prodlist(grid[row][col-3:col+1]))
    # Up
    if row > 2:
        subgrid = grid[row-3:row+1]
        seq = [row[col] for row in subgrid]
        products.append(prodlist(seq))
    # Down
    if row < 17:
        subgrid = grid[row:row+4]
        seq = [row[col] for row in subgrid]
        products.append(prodlist(seq))
    # Up-Right
    if col < 17 and row > 2:
        seq = []
        for i in range(4):
            seq.append(grid[row-i][col+i])
        products.append(prodlist(seq))
    # Up-Left
    if col > 2 and row > 2:
        seq = []
        for i in range(4):
            seq.append(grid[row-i][col-i])
        products.append(prodlist(seq))
    # Down-Right
    if col < 17 and row < 17:
        try:
            seq = []
            for i in range(4):
                seq.append(grid[row+i][col+i])
            products.append(prodlist(seq))
        except:
            print("Failed down-right for {0}, {1}.".format(row, col))
    # Down-Left
    if col > 2 and row < 17:
        seq = []
        for i in range(4):
            seq.append(grid[row+i][col-i])
        products.append(prodlist(seq))
    return max(products)


grid = open("problem11.in").readlines()
grid =[line.split() for line in grid]
grid

max_product = -1

for i, row in enumerate(grid):
    for j in range(len(row)):
        max_product = max([max_product, maxprod(i, j, grid)])

print(max_product)

