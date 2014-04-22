#!/usr/bin/env python3

import string

ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
plaintext = ""

for char in ciphertext:
    if char in string.ascii_lowercase:
        plaintext += chr(ord(char) + 2)
    else:
        plaintext += char

print(plaintext)
