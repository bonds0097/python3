#!/usr/bin/env python3

MAX = 2000000

def applySieve(prime, sieve):
    return [x for x in sieve if x % prime != 0]

prime = 3
sum_primes = 5

sieve = list(range(3, MAX + 1, 2))
while prime < MAX:
    sieve = applySieve(prime, sieve)
    try:
        prime = sieve[0]
    except IndexError:
        break
    sum_primes += prime

print("{0}: {1}".format(prime, sum_primes))
