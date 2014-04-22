#!/usr/bin/env python3

from PIL import Image

source = Image.open("wire.png")
target = Image.new("RGB", (100, 100))

step = 100
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
iterations = 0
current = (-1, 0)
pixel = 0

while step > 0:
    for direction in directions:
        if iterations % 2 == 1:
            step -= 1
        count = 0
        print("Step: {0}".format(step))
        while count < step:
            current = current[0] + direction[0], current[1] + direction[1]
            print(current)
            target.putpixel(current, source.getpixel((pixel, 0)))
            count += 1
            pixel += 1
        iterations += 1

target.save("spiral.png")
target.show()


