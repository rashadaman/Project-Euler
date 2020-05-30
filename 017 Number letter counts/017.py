'''
Number letter counts
==================================================

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''

NAMES = {0:0,1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
         10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,
         20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

hundred_and = 10
one_thousand = 11

def count_letters():
    number=1000
    result = 0
    
    if number < 20 :
        print('the number must be bigger than 20')
        return None
    
    ####################  1-9 الآحاد  ############################
    n_1_9 =  sum(NAMES[i] for i in range(1,10))

    ####################  10-19 العشرات  ########################
    n_10_19 = sum(NAMES[i] for i in range(10,20))
    
    ####################  20-90 العشرات  ########################
    n_20_90 = sum(NAMES[i] for i in range(20,100,10))
    
    ####################  1-99 الأعداد ###########################
    n_1_99 = n_1_9 * 9  + n_10_19 + n_20_90 * 10
    
    #################### 100-900 المئات ########################
    unwanted_and = 9 * len('and')
    
    #100, 200, 300, ...
    hundreds = 100 * (n_1_9 + 9 * hundred_and) - unwanted_and
    
    n_1_999 = n_1_99 + 9 * n_1_99 + hundreds 

    #################### الآلاف ########################
    result += one_thousand + n_1_999
    
    return result

print(count_letters())