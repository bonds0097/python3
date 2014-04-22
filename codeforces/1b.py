#!/usr/bin/env python3

import re

tests = int(input())

excel = re.compile("^([A-z]+)(\d+)$")
rc = re.compile("^R(\d+)C(\d+)$")

for test in range(tests):
    coords = input()
    if excel.match(coords):
        print("Case {0} is excel.".format(test))
    elif rc.match(coords):
        print("Case {0} is rc.".format(test))
    else:
        print("Could not determine type for case {0}".format(test))
