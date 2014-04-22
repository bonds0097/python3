#!/usr/bin/env python3
import math

data = input().split()

n = int(data[0])
m = int(data[1])
a = int(data[2])

width = math.ceil(n / a)
length = math.ceil(m / a)

print(width * length)
