#08_calendar


import calendar

print(calendar.calendar(2026))  
'''
It will print all the months of the year.
'''

print(calendar.month(2026,7))
'''

     July 2026
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
'''



print(calendar.weekday(2026,7,18)) #5


print(list(calendar.day_name))
'''
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
'''

print(list(calendar.month_name))
'''
['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
'''


print(calendar.isleap(2028)) #True