#sum of n digit 

num = int(input("sum of a number digit ="))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("Sum of all digit is =", sum)    