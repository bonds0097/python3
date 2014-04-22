#!/usr/bin/env python3

MAX = 150000
primes_found = 2

def applySieve(prime, sieve):
    return [x for x in sieve if x % prime != 0]

prime = 3

sieve = list(range(3, MAX + 1, 2))
while primes_found < 10001:
    sieve = applySieve(prime, sieve)
    prime = sieve[0]
    primes_found += 1
    print("{0}: {1}".format(primes_found, prime))
    if prime >= MAX or prime == -1:
        break

print(prime)
print(primes_found)
