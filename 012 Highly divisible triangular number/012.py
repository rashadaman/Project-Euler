def get_triangle_at(index):
    return index * (index + 1) // 2
        
def get_fact_num(number):
    factors = {2:0}
    f = 2
    while f ** 2 <= number:
        if number % f == 0 :
            previous_count = factors.get(f, 0)
            factors[f] = previous_count + 1
            number = number // f
        else:
            if f == 2:
                f = 3
                continue
            f += 2
    
    if number > f:
        factors[number] = 1
            
    numeber_of_factors = 1
    for v in factors.values():
        numeber_of_factors *= (v+1)

    return numeber_of_factors#, factors
    
def find_triangle_by(number_of_factors):
    """
    تلك الدالة ترجع اول رقم عدد عوامله اكبر من 
    <number_of_factors> عدد العوامل المعطى للدالة
    """
    index = 1
    triangle = get_triangle_at(index)

    while get_fact_num(triangle) <= number_of_factors:
        index += 1
        triangle = get_triangle_at(index)

    return triangle


number_of_factors = 500

print(find_triangle_by(number_of_factors))