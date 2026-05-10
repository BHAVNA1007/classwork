#numbers between two number

num1 = int(input("Enter fist num = "))
num2 = int(input("Enter second num = "))

if num1 <= num2:
    while num1 <= num2:
        print(num1)
        num1 += 1
else:
    while num1 >= num2:
        print(num1)
        num1 -= 1
print("done")
