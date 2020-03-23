'''
Summation of primes
==================================================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

'''

def m2(n):
    primes = [False, True] * (n // 2) + [False]
    primes[1], primes[2] =  False, True

    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            number_of_multiples = ((n-p*p) // (2*p)) + 1
            try:
                primes[p*p::p * 2] = [False] * number_of_multiples
            except:
                break
    return sum([i*number for i,number in enumerate(primes)])


n = 2e6
print(m2(int(n)))