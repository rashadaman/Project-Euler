'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

number = int(input("The Number: "))

factor = 2
largest_factor = 0

while factor ** 2 <= number:
    if number % factor == 0:
        print(number, '/ %s' % factor)
        number //= factor
        largest_factor = factor

    else:
        if factor == 2:
            factor = 3
        else:
            factor += 2

if number > factor:
    largest_factor = number

print(largest_factor)
