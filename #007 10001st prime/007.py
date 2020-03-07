"""
10001st prime
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

#! NEVER USE AND INCREAS BY 2
#! ==============
# i = 1
# n = 2
#! ==============

# i = 2
# n = 3

i = 1000
n = 7919
index = 10001


def is_prime(number):
    if number % 2 == 0:
        return False

    f = 3
    while f**2 <= number:
        if number % f == 0:
            return False
        f += 2

    return True


while i < index:
    n += 2

    if is_prime(n):
        i += 1


print(n)
