#type_casting
'''
#impicit_casting

a=10
b=2.5
c=a+b
print("c")
print(type(c))
d=a*b
print(d)
print(type(d))

'''

'''
#explit_conversion
#int() it convert float, string, bool into integer
#here decimal point is turncated

a=int(10.5)
print(a)
print(type(a))

a=int("10")
print(a)
print(type(a))

a=int(True)
print(a)
print(type(a))
'''

'''
ValueError: invalid literal for int() with base 10: '10.9'
a=int("10.9")
print(a)
print(type(a))


a=int(float("10.9"))
print(a)
print(type(a))
'''

#float()

a=float(10)
print(a)
print(type(a))


a=float("10.5")
print(a)
print(type(a))

'''
ValueError: could not convert string to float: 'deepika'
a=float("deepika")
print(a)
print(type(a))
'''

print(float(True))
print(float(False))

'''
x=float(10+2j)
print(x)
print(type(x))
'''


'''
#str() it converts int, float, bool, complex, into, string

a=str(10)
b=str(12.56)
c=str(True)
d=str(3+4j)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
'''


'''
#bool()  it converts int, float, string into True and False

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("deepika"))
print(bool([]))
print(bool([1,2,3]))
print(bool(-10))
print(bool(0.0001))
print(bool(0.0))
print(bool(10+20j))
print(bool(0+0))
'''


#complex() it converts int, float, string into complex
print(complex(10))
print(complex(10,20))
print(complex("10"))

#ValueError: invalid literal for int() with base 10: '10x'
#print(int("10x"))

print(bool("False"))

print(complex(True))
print(complex(False))


#ValueError: complex() arg is a malformed string
#print(complex("abc"))
print(complex(True, False))





