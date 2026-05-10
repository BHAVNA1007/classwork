#05_armstrong_number

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))

for n in range(x,y+1):
    
    temp = n
    power = len(str(n))
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + digit**power
        temp = temp // 10
    if total == n:
        print(total)