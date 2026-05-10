#operators:operators are special symbols which are you used #perform special oprations

#arithmetic_oprators + - * / %

a=10
b=20
print(a+b)
print(a-b)
print(a*b)


a="10"
b="20"
print(a+b)


'''
#TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(a-b)

#TypeError: can't multiply sequence by non-int of type 'str'
print(a*b)

#TypeError: can't multiply sequence by non-int of type 'float'
print("deepika"*5.5)

'''
print("deepika"*5)

print(10/2)
print(7/2)

#ZeroDivisionError: division by zero :  print(10/0)

print(10//3)
print(9//2)
print(-13//3)


print(5%2)
print(27%30)
print(-5%2)
print(-5%-2)
print(5%-2)

#for finding last digit of the given number
print(197%10)

#for remove last digit of the given number
print(197//10)

x=164
y=x%10
print(y*y)


x=x//10
y=x%10
y=print(y*y)

x=x//10
y=x%10
print(5.25%2)



