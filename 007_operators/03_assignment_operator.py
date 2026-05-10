#assignment_operator: assignd value right to left side

a=10
print(a)

'''
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

10=20
'''

a=10
a+=5
print(a)

a-=5
print(a)

a*=5
print(a)

a/=5
print(a)

a%=5
print(a)


a=b=c=d=10
print(a,b,c,d)

'''
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='   a+b=2?
a=5
b=10
a+b=2
print(a,b)
'''

a=5
b=2
a+=b*3
print(a,b)

a=5
a*=-2
print(a)


