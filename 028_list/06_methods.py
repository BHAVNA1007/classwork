#06_methods

#4. sorted

a = [11,3,4,24,9]
b = sorted(a)
print(a)
print(b)

a=['deepika123','rashmika33','www1','rrr','deepika']
b = sorted(a)
print(a)
print(b)


#5. reverse()

a=[11,3,4,24,9]
a.reverse()
print(a)

a=['deepika123','rashmika33','www1','rrr','deepika']
a.reverse()
print(a)


#6. copy()
a =[11,3,4,24,9]
b = a.copy()
print(a)
print(b)
a[0] = 99
print(a)
print(b)

print(id(a))
print(id(b))


#7. max()
a = [11, 3, 4, 24, 9]
print(max(a))


#8. min()
a=[11,3,4,24,9]
print(min(a))


#9. sum()
a=[10,8,77]
print(sum(a))

print(sum(a,100))

'''
#TypeError: unsupported operand type(s) for +: 'int' and #'str'
a = ['abc','xyz']
print(sum(a))
'''

#10. any()
a= [0, False, None]
print(any(a))

a= [1, False, None]
print(any(a))

#11. all()
a= [0, False, None]
print(all(a))

a= [1, 'asd', 'xy']
print(all(a))

a= [1, 'asd', 0]
print(all(a))

#12. enumerate()
names = ['xyz','abc','www']
for index, value in enumerate(names):
   print('index is', index,'and', value)

#13. zip()
names = ['xyz','abc','www']
marks = [80,90,70]
for n, m in zip(names, marks):
    print("name",n,"and","mark",m)


names = ['xyz','abc','www']
names1 = ['xyz','abc','www1']

for n,m in zip(names, names1):
    if n == m:
        print("same")
    else:
        print("not same")


names = ['xyz','abc','www']
price = [100, 400]

for n, m in zip(names,price):
     print(n,'->',m)


#14. list()

a= 'deepika'
print(list(a))


#15. filter()
#16. map()












