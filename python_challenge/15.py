#!/usr/bin/env python3

import datetime

target = datetime.date(1, 1, 26)

while target.year < 2014:
    if (target.weekday() == 0 and str(target.year)[0] == '1' and str(target.year)[-1] == '6'
        and target.year % 4 == 0):
        print(target.year)
    target = target.replace(year=target.year+1)
