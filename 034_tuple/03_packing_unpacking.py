#03_packing_unpacking

#packing
t = 10, 20, 30
print(t)

#unpacking
a,b,c = (10,20,30)
print(a)
print(b)
print(c)

a, *b = (10,20,30)
print(a)
print(b)


a,*b,c = (10, 20, 30, 40, 50)
print(a)
print(b)
print(c)

 