'''
Amicable numbers
==================================================

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

'''
def d(n):
    if n < 2:
        return 0
    
    f = 2
    total = 1
    while f**2 <= n:
        if n % f == 0:
            total += f
            other = n // f
            if other > f:
                total += other

        f += 1
    
    return total


def start(limit=10000):
    result = 0
    for n in range(int(limit)):
        d_n = d(n)
        if d_n == n:
            continue
            
        d_d_n = d(d_n) 
        if d_d_n == d_n:
            continue
        
        if d_d_n == n:
            result += n

    
    return result

print(start())