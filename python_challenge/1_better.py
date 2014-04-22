#!/usr/bin/env python3

import string

cipher = 'abcdefghijklmnopqrstuvwxyz'
plain =  'cdefghijklmnopqrstuvwxyzab'
rotation = str.maketrans(cipher, plain)

ciphertext = "map"
plaintext = ciphertext.translate(rotation)

print(plaintext)
