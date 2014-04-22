#!/usr/bin/env python3

import urllib.request
import re

key = "25357"
pattern = re.compile("and the next nothing is (\d+)")

while True:
    response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}".format(key))
    data = response.read().decode('utf-8')
    result = pattern.search(data)
    if result:
        key = result.group(1)
        print(key)
    else:
        print(data)
        break
