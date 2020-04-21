'''
Lattice paths
==================================================

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

'''
from math import factorial

def number_of_paths_in(square_grid_length):
    '''
    يقوم بحساب عدد المسارات فى 
    رقعة مربعة طول ضلعها معطى للدالة
    '''
    # مجموع الخطوات حتى يصل الى النهاية
    total_steps = 2 * square_grid_length
    
    #  قانون التوافيق
    total_paths =\
    factorial(total_steps) // (factorial(total_steps - square_grid_length) * factorial(square_grid_length)) 
    
    return total_paths


print(number_of_paths_in(20))