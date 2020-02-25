'''
A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''



def is_palindromic(number):
    number_str = str(number)
    return number_str == number_str[::-1]


def optimized_is_palindromic(number):
    reverse = 0
    i = number
    
    while i > 0:
        reverse = reverse * 10 + i % 10
        i //= 10
        
    return reverse == number

# x = 565
# print(is_palindromic(x))
# print(optimized_is_palindromic(x))


result = 0

result = 0


for i in range(990, 99, -11):
    for j in range(999, 99, -1):
        product = i * j
        
        if product < result:
            break
            
        if optimized_is_palindromic(product):
            result = product
            break

        
print(result)