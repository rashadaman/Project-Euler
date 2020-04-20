'''
Longest Collatz sequence
==================================================

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def longest_collatz(the_end):
    '''
    تقوم تلك الدالة بحساب العدد
    الذى سيأخذ أكبر عدد من الخطوات حتى يصل الى رقم 1 
    ملاحظة
    ======
    الرقم المعطى للدالة غير مضمون فى الحسابات
    '''
    
    the_end = int(the_end)
    
    tree = {1:1}
    for i in range(2, the_end):
        # عدد الخطوات
        length = 1 
        
        # اخذنا نسخة من الرقم لاننا سنقوم
        #بتغيير قيمة تلك النشخة بدلا من الرقم الاصلى
        n = i
        while n != 1:
            # تأكد اذا ما كان الرقم قد حسبناه مسبقا أم لا
            if tree.get(n, False):
                length += tree[n]
                break
            
            # القاعدة
            n =  (n // 2) if n % 2 == 0 else (3*n + 1) 
            length += 1

        tree[i] = length
    
#     print(tree)    # ===> للتوضيح فقط
    
    # تقوم بارجاع المفتاح صاحب اكبر قيمة فى القاموس 
    return max(tree, key=tree.get)


longest_collatz(1e6)
