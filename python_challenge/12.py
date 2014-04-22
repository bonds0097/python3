#!/usr/bin/env python3

evil = open("evil2.gfx", 'rb').read()
images = {
    0:open('evil1.jpg', 'wb'),
    1:open('evil2.png', 'wb'),
    2:open('evil3.gif', 'wb'),
    3:open('evil4.png', 'wb'),
    4:open('evil5.jpg', 'wb')}

index = 0
for byte in evil:
    images.get(index).write(byte.to_bytes(1, 'big'))
    if index == 4: index = 0
    else: index += 1

for image in images.values():
    image.close()


