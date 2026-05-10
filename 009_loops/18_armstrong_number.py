#18_armstrong_number

num = int(input("Enter a number = "))
t = len(str(num))

temp = num
sum = 0

while num > 0:
    rem = num % 10
    sum = sum + rem ** t 
    num = num // 10
if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")


