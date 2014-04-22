#!/usr/bin/env python3

from PIL import Image

img = Image.open("oxygen.png")

width, height = img.size

message = []
search_width = 0
height /= 2

while search_width < width:
    search = (search_width, height)
    message.append(chr(img.getpixel(search)[0]))
    search_width += 7

print("".join(message))

url = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join([chr(i) for i in url]))
