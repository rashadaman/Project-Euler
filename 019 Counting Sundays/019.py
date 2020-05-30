'''
Counting Sundays
==================================================

You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

import calendar


def how_many(day_name, start_year, end_year):
    """
    الدالة ترجع كم مرة تكرر اليوم المعطى لها فى الفترة الزمنية المعطاة
    """
    occurrence = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            start_day, number_of_days = calendar.monthrange(year, month)
            
            if day_name < start_day: 
                wanted_day_date = ((day_name + 7) - start_day) + 1
            else:    
                wanted_day_date = (day_name - start_day) + 1
            
            while number_of_days >= wanted_day_date:
                occurrence += 1
                wanted_day_date += 7                
    
    return occurrence



def starts_with(day_name, start_year, end_year):
    """
    الدالة ترجع عدد الشهور التى تبدأ باليوم المعطى لها فى الفترة الزمنية المعطاة
    """
    number_of_months = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            start_day, number_of_days = calendar.monthrange(year, month)
            
            if start_day == day_name:
                number_of_months +=1
                
    return number_of_months



start_year , end_year = 1901, 2000
all_sundays = 0
day = {
    'mon':0,
    'tue':1,
    'wed':2,
    'thu':3,
    'fri':4,
    'sat':5,
    'sun':6
}
        
print(starts_with(day['sun'], start_year, end_year))
