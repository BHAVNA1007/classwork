#04_list_methods


#1. index()
a =['deep','rash','www']
print(a.index('deep'))

'''
#ValueError: 'deep1' is not in list
print(a.index('deep1'))
'''

#2. count()
a=['deep','rash','www','deep']
print(a.count("deep"))

a=[10, 20, 30, 10, 10, 10]
print(a.count(10))


#3. sort()
a=['deep','rash','www','deep']
a.sort()

b =[15, 2, 30, 10, 10]
b.sort()
print(a)
print(b)

a=['deep','rash','www','deep']
a.sort(reverse=True)
print(a)

b = [15, 2, 30, 10, 10]
b.sort(reverse = True)
print(a)
print(b)


'''
#TypeError: '<' not supported between instances of 'int' and #'str'
a=['deep',1,2,3.4,2,'rash','www','deep']
a.sort()
print(a)
'''

'''
#TypeError: '<' not supported between instances of 'int' and #'str'
a=['deep',1,'rash',2,'www','deep']
a.sort()
print(a)
'''




