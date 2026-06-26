#07_timedelta

from datetime import datetime, timedelta

today = datetime.now()
print(today)                 #2026-06-26 20:35:49.532298

exp = today + timedelta(days=7)

print(exp)         #2026-07-03 20:35:49.532298



dob1 = datetime(2026,2,26)
dob2 = datetime(2000,2,7)

d = dob1 - dob2

print(type(d))   #<class 'datetime.timedelta'>

print(d)  #9516 days, 0:00:00

print(d.seconds)  #0

