#!/usr/bin/env python3

from PIL import Image

img = Image.open("cave.jpg")

width, height = img.size

pixels = ((x,y) for x in range(0, width) for y in range(0, height))

for x, y in pixels:
    if x % 2 == 0 or y % 2 == 0:
        img.putpixel((x,y), 0)

img.save("cave.jpg")
