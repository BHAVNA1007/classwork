#count digit in num

num = int(input("count digit in a number = "))

count = 0
while num > 0:
   digit = num % 10
   count += 1
   num = num // 10
print("number of digit in given number is = ", count)