#!/usr/bin/env python3

# Head ends here
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        output = "CLEAN"
    elif posr % 2 == 0:
        if posc < 4:
            output = "RIGHT"
        else:
            output = "DOWN"
    elif posr % 2 == 1:
        if posc > 0:
            output = "LEFT"
        else:
            output = "DOWN"
    else:
        output = "I don't know what to do."

    print(output)

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
