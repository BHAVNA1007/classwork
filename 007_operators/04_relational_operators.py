#Relational_operators < > <= >= == !=  allowed you to compare #two values and return a boolean result either True or False


a=5
b=2
print(a==b)

print(a<b)

print(a>b)

print(a!=b)


c=5
print(a<5)
print(a<=c)

print(c<=a)

print(a!=c)

print(5==5.0)
print(3.5>2)

a="deepika"
b="rashmika"
print(a<b)


# ord()  used for unicode number
print(ord("a"))
print(ord("A"))

print(ord("@"))


print("apple"=="apple")
print("apple"=="Apple")

a="Bdeepika"
b="Arashmika"
print(a<b)

a="dee"
b="dee"
print(a<b)

a="deeA"
b="deeA"
print(a<b)

'''
string  follows dictionary order comparision done char by char it usses unicode value
''' 

a="dog"
b="cat"
print(a>b)
print(5=="5")

'''
#TypeError: '>' not supported between instances of 'str' and #'bool'
a="True"
b=False
print(a>b)
'''

print(5=="5")
'''
TypeError: '>' not supported between instances of 'int' and 'str'
print(5>"5")
'''

'''
print(True==True)
print(True==False)
print(False!=True)

print(True<False)
print(True>False)
print(False<=True)
print(True>=False)
'''
'''
print(0==False)
print(1==True)
# doubt----->>>>> print(2==True)
print(""==False)
print([]==False)
'''
print(5<2==3)
print(10<20<30)

print(3<4!=2<5!=6==4>7)

a=10==20==30==40
print(a)

a=10==5+5==3+7==2*5
print(a)

a="a"==97
print(a)

a=10==10.0
print(a)


