#!/usr/bin/env python3

def generate_seq(next, prev):
    # Parse number from left to right.
    prev = str(prev)
    next = []

    prev_char = ""
    count = 0

    for char in prev:
        if char == prev_char:
            count += 1
            prev_char = char
        else:
            next.append(str(count))
            next.append(prev_char)
            prev_char = char
            count = 1


    # Append the last bits.
    next.append(str(count))
    next.append(prev_char)

    return int("".join(next).strip())


a = [1]

for i in range(1, 31):
    a.append(generate_seq(i, a[i-1]))

print(len(str(a[30])))
