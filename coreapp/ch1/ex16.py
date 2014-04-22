#!/usr/bin/env python3

import re

# Get data from file.
data = open('redata.txt', 'r').readlines()

# Dictionary to count day of the week ocurrences.
days = dict.fromkeys(('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'), 0)

# Pattern to extract day of the week.
pattern = re.compile('^(' + '|'.join(days.keys()) + ')')

for line in data:
    match = pattern.match(line)
    if match is not None: days[match.group(1)] += 1
    else: print("Day of week not found.")

print(days)
