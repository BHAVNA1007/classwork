''' input_function :it used to take input from the user

name = input("enter your name")
print(f"Name is {name}")

'''

''' input() function always returns data in string format
a = input("first number")
b = input("second number")
print(a+b)'''

'''
a = int(input("enter first number"))
b = int(input("enter second number"))
print(type(a))
print(type(b))
print(a+b)
'''

'''
salary1 = float(input("first salary"))
salary2 = float(input("second salary"))
print("total salary is", salary1+salary2)
'''

'''taking multiple input in 1 line.
here we have name and address if we put only one value it will be thorw error like : 
ValueError: not enough values to unpack (expected 2, got 1)'''

'''
name,address=input("enter name and address").split()
print("name is", name)
print("Address is", address)
'''

'''
marks1,marks2=input("enter both marks").split()
print(marks1)
print(marks2)
marks1= int(marks1)
marks2= int(marks2)
print(marks1+1)
print(marks2+1)
'''

# map() : function 
'''
marks1,marks2=map(int,input("enter both marks").split())
print(marks1)
print(marks2)
print(marks1+1)
print(marks2+2)
'''
'''input function takes input as string "20 20" after that split() function split it using space ["20","20"] now map() function convert each string into integer [20 , 20]'''

'''
data = input("enter both marks").split()
print(data)
print(data[0])
print(data[1])
'''

'''TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'' 

m1,m2 = int(input("enter both marks").split())
print(m1)
print(m2)

'''
#solution for this error
m1,m2=map(float,input("enter both marks").split())
print(m1)
print(m2)




