#04_datetime


#date

from datetime import date

today = date.today()
print(today)    #2026-06-26

print(today.year) #2026
print(today.month) 	#6
print(today.day)  #26



#datetime

from datetime import datetime

now = datetime.now()

print(now)    #2026-06-26 19:25:49.318040

print(now.year)  #2026
print(now.month)   #6
print(now.minute)  #28
#print(now.second)  


#custom date time

now = datetime(2025,2,20,10,30,0)
print(now)   #2025-02-20 10:30:00





