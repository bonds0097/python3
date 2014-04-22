#!/usr/bin/env python3

import re

from zipfile import ZipFile

pattern = re.compile("Next nothing is (\d+)")
start = "90052.txt"

with ZipFile('channel.zip') as myzip:
    data = myzip.open(start).readline().decode('UTF-8')
    print(myzip.getinfo(start).comment.decode('UTF-8'))

    while True:
        match = pattern.search(data)

        if not match:
            break
        else:
            name = match.group(1) + ".txt"
            data = myzip.open(name).readline().decode('UTF-8')
            print(myzip.getinfo(name).comment.decode('UTF-8'), end='')
