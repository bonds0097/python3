#!/usr/bin/env python3

test = 2520

while True:
    for i in range(20, 0, -1):
        if test % i != 0:
            test += 2
            break
    else:
        break

print(test)
