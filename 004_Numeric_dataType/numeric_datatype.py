#numeric_datatype
'''Integer :the integer class represent negative and positive whole number the length of an integer has no limits'''
'''
a=10
b=-10
c=999999999999
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

c= 99_99_88_88_999
print(c)
#remove underscore in the output 99998888999

print(type(c))
#<class 'int'>

'''
'''
c=_66
print(c)
# NameError: name '_66' is not defined
'''
'''
c=99_88_
print(c)
#SyntaxError: invalid decimal literal
'''
'''
a=0b1011
print(a)
#convert it decimal  output: 10
'''

'''
b=0B1111 #binary
print(b)
print(type(b))

a=0O137 #octal
print(a)
print(type(a))

a=0xABC #hexadecimal
print(a)
print(type(a))

b= 0xa
print(b)
print(type(b))


#a=0xdeepika
#print(a)
#SyntaxError: invalid hexadecimal literal

a= 0xA
print(a)


# Base_conversion bin() , oct() , hex()

print(bin(15))
print(bin(0o127))
print(oct(15))
print(oct(0B1111))
print(hex(15))
print(hex(0B1111))

'''

'''
# float_datatype
x=3.14
y=0.0012
z=0.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


x=985_123.4_986_111
print(x)
print(type(x))

'''
'''
# SyntaxError: invalid decimal literal
x=893_._156
print(x)


#binary,octal and hexadecimal cannot work with float
#SyntaxError: invalid syntax
x=0x154.84
print(x)


x=5/2
print(x)
print(type(x))

x=5//2
print(x)
print(type(x))
'''
'''
#math.ceil() round-up the value. math.floor() round-down the value
import math
a=3.7
print(math.ceil(a))

print(math.floor(a))
'''
'''
import math
#abs() convert + int - and vise warsa
b=-5.6
print(abs(b))

#convert into nearest integer
a=3.7
print(round(a))
'''
'''
import math
a=3.7467
print(round(a,3))

print(round(a,2))
print(round(a,1))
'''
'''
#here 2e2 means 10 to the power 2
import math
a=1.2e2
print(a)
print(type(a))

a=1.2e3
print(a)
print(type(a))
'''
'''
# complex_numbers: denots with j 
z= 3+4j
print(z)
print(type(z))

y= -1+2j
print(y)
print(type(y))

x=3+4j
print(x.real)
print(x.imag)

x=complex(input("enter complex number"))
print(x.real)
print(x.imag)
'''
'''
SyntaxError: invalid decimal literal
x=3+4i
print(x.real)
print(x.imag)
'''
'''
x=0b1111+0b1111j
print(x.real)
print(x.imag) 

'''
'''
#SyntaxError: invalid binary literal
x=0B1111+4j
print(x.real)
print(x.imag)
'''

#addition of two complex number is complex

x=3+4j
y=9+5j
print(x+y)
print(x-y)
print(x*y)
print(x/y)





