#06_strptime

from datetime import datetime

str = "20-02-2026"

dt = datetime.strptime(str, "%d-%m-%Y") #2026-02-20 00:00:00

print(dt)

print(type(dt)) #<class 'datetime.datetime'>



str = input("Enter date(dd-mm-yyyy): ")

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)


str = input("Enter DOB(dd-mm-yyyy): ")
now = datetime.now()
dt = datetime.strptime(str, "%d-%m-%Y")

age = now.year - dt.year

print(age)