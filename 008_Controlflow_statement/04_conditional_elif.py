'''
04_conditional_elif
it is used to check multiple conditions sequentialy.

syntax:

if condition1:
    statement1

elif condition2:
    statement2

elif condition:
    statement3

elif condition4:
    statement4

else:
    last statement

'''

'''
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))

if a>b and a>b:
   print("a is greater ")
elif b>c:
   print("b is greater")
else:
   print("c is greater")
print("Done")
'''



a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
d = int(input("Enter fourth number = "))

if a>b and a>c and a>d:
    print("a is greater")

elif b>c and b>d:
    print("b is greater")
elif c>d:
    print("c is greater")

else:
    print("d is greater")




