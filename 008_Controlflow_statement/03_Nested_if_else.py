'''
Nested_if_else 

syntax: 

if condition1:
    if condition2:
        statement x
    else:
        statement y
else:
    if condition3:
        statement alpha
    else:
        statement beta
'''

'''
a= int(input("Enter first number = "))
b= int(input("Enter second number = "))
c= int(input("Enter third number = "))

if a > b:
    if a > c:
        print("a is greater")
    else:
        print("c is greater")
else:
   if b > c:
       print("b is greater")
   else:
       print("c is greater") 
'''



'''
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
d = int(input("Enter fourth number = "))


if a>b:
    if a>c:
        if a>d:
           print("a is greater")
        else:
           print("b is greater")
    else:
        if c>d:
           print("c is greater") 
        else:
           print("d is greater")
else:
    if b>c:
       if b>d:
          print("b is greater")
       else:
          print("d is greater")
    else:
       if c>d:
          print("c is greater")
       else:
          print("d is greater")

'''


'''
age = int(input("Enter age = "))
citizen = input("are u indian (yes/no) = ")

if age >= 18:
    if citizen.lower() == 'yes':
        print("u can vote")
    else:
        print("must be indian")
else:
    print("under age")
print("Done")

'''

username = input("Enter username = ")
password = input("Enter password = ")

if username == "admin":
    if password == "1234":
        print("password is valid")
    else:
        print("invalid password")
else:
    print("invalid username")
print("Done") 


















   

