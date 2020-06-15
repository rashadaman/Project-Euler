'''
Names scores
==================================================

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

'''
import string
alphabet_list = list(string.ascii_uppercase)


def extract_names_from(file_path):
    """
    الدالة تقوم باستخراج الاسماء من الملف المعطى
    """
    names = None
    
    with open(file_path) as file:
        # name[1:-1] حتى لا ندرج علامات التنصيص فى الاسم
        names = [name[1:-1] for name in file.read().split(',')]
    
    # ترتيب الاسماء ابجديا دون الحاجة لانشاء مجموعة جديدة
    names.sort()
    
    return names 

def calc_names_in_file(path):
    """
    الدالة تقوم بارجاع مجموع الارقام الموافقة لكل اسم فى الملف المعطى
    """
    
    names_list = extract_names_from(path)
    sum_file = 0
    for rank, name in enumerate(names_list):
        # مجموع ترتيب حروف الاسم
        name_total = 0
        for letter in name:
            #  اضف واحد لان الترتيب يبدا من رقم صفر
            # بينما الترتيب فى السئال يبدأ من رقم 1
            name_total += (alphabet_list.index(letter) + 1)

        # اضف واحد لان الترتيب يبدا من رقم صفر
        # بينما الترتيب فى السئال يبدأ من رقم 1
        sum_file += name_total * (rank + 1)

    print(sum_file)

calc_names_in_file('./names.txt')