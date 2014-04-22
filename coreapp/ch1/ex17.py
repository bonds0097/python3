#!/usr/bin/env python3

import re
import time

# Get data from file.
data = open('redata.txt', 'r').readlines()

# Pattern to extract timestamp and unix time.
pattern = re.compile('^(.*)::.*::(\d+)-.*$')

for i, line in enumerate(data):
    match = pattern.match(line)
    if match is not None:
        timestamp = match.group(1)
        unix_time = match.group(2)
        if timestamp == time.ctime(int(unix_time)): pass
        else: print("File is corrupt. Line " + str(i + 1) + " timestamps did not match.")
    else: print("File is corrupt. Unable to parse line " + str(i + 1) + ".")
