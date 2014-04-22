#!/usr/bin/env python3

from random import randrange, choice
from string import ascii_lowercase as lc
from time import time, ctime

tlds = ('com', 'edu', 'net', 'org', 'gov');

fout = open('redata.txt', 'w')

for i in range(randrange(10, 21)):
    dtint = randrange(2**32)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    output = '{0}::{1}@{2}.{3}::{4}-{5}-{6}\n'.format(dtstr, login, dom,
                                                    choice(tlds), dtint, llen,
                                                    dlen)
    fout.write(output)

fout.close()

