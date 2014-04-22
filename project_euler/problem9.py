#!/usr/bin/env python3

import itertools

possibles = itertools.product(range(1000), repeat=3)

for a,b,c in possibles:
    if a + b + c == 1000 and (a**2 + b**2) == c**2:
        print(a * b * c)
        break
