
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''


def is_prime(n):
    if n == 0 or n == 1:
        return False

    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False

        i += 1

    return True


def primes_mutiples_until(end):
    primes, multiples = [], []

    for i in range(2, end+1):

        if is_prime(i):
            primes.append(i)
        else:
            multiples.append(i)

    return primes, multiples


def get_smallest_multiple(end):
    the_number = 1
    primes, multiples = primes_mutiples_until(end)

    for p in primes:
        the_number *= p

    for m in multiples:
        reminder = the_number % m
        if reminder != 0:
            if is_prime(reminder):
                the_number *= reminder
            else:
                for p in primes:
                    if reminder % p == 0:
                        the_number *= p
                        break

    return the_number


end = 10000
print(get_smallest_multiple(end))
