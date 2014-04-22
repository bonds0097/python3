#!/usr/bin/env python3

import re

# Get data from file.
data = open('redata.txt', 'r').readlines()

# Pattern to extract timestamp and unix time.
pattern = re.compile('^(.*\d)?::')

for i, line in enumerate(data):
    match = pattern.match(line)
    if match is not None:
        print(match.group(1))
    else: print("File is corrupt. Unable to parse line " + str(i + 1) + ".")
