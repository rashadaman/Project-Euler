'''
Power digit sum
==================================================

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?

'''

def digit_sum (base=2, power=1000):
    number = int(base**power)
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
        
    return result

print(digit_sum())