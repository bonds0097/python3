#!/usr/bin/env python

import pprint, pickle

input = open("banner.p", "r")

data = pickle.load(input)
print(data)
for line in data:
    print ''.join(elmt[0] * elmt[1] for elmt in line)

input.close()
