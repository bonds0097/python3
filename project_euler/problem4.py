#!/usr/bin/env python3
import itertools

def isPalindrome(int):
    int = str(int)
    if int == int[::-1]:
        return True
    else:
        return False

largest_palindrome = -1

for x,y in itertools.product(range(111,1000), range(111, 1000)):
    product = x * y
    if isPalindrome(product) and (product) > largest_palindrome:
        largest_palindrome = product

print(largest_palindrome)
