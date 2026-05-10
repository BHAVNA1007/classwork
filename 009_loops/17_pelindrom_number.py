#17_pelindrom_number

n = int(input("Enter a number = "))

rev = 0
new_num = n

while n > 0:
   rem = n % 10
   rev = rev * 10 + rem
   n = n // 10
if new_num == rev:
   print("pelindrom")
else:
   print("Not pelindrom")