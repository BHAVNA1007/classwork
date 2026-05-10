#03_max_number

'''
a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))

max = a if a>b else b
print(max)
'''

'''
a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))

print("a is greater ") if a > b else print("b is greater")
'''

'''
x = 10 if 20<30 else 40 if 40<60 else 70
print(x)
'''

'''
x = 10 if 200<30 else 40 if 50<60 else 70
print(x)
'''

'''
x = 10 if 200<30 else 40 if 500<60 else 70
print(x)
'''

'''
a = 100
b = 200
c = 30
max = a if a>b and a>c else b if b>c else c
print(max, "is greater")
'''

'''
a = int(input("Enter a = "))
b = int(input("Enter b = "))
print("Equal " if a==b else "greater" if a>b else "small" )
'''

'''
i = 1
while i<=10:
     print(i, "even") if i % 2 == 0 else print(i, "odd")
     i = i + 1
'''

i = 1
while i<= 10:
    print(i,"even" if i%2==0 else "odd")
    i = i+1

