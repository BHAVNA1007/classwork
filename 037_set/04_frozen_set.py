#04_frozen_set

f = frozenset([1,2,3,4,5,5,4,88,77,345,3])
print(f)                 #frozenset({1, 2, 3, 4, 5, 77, 88, 345})
print(type(f))          #<class 'frozenset'>

f1 = frozenset((1,2,3,4,5,5,4,88,77,345,3))
print(f1)          #frozenset({1, 2, 3, 4, 5, 77, 88, 345})

f2 = frozenset("deepika padukon")
print(f2)    #frozenset({'a', 'p', 'k', 'n', 'd', ' ', 'e', 'u', 'i', 'o'})


s = {1,2,3,3}
print(id(s))     #1407979001152

s.add(99)
print(s)        #{99, 1, 2, 3}
print(id(s))    #1407979001152

'''
f = frozenset([6,7,8,9])
f.add(99)
print(f)  #AttributeError: 'frozenset' object has no attribute 'add'
'''

f1= frozenset([6,7,8,9])
f2 = frozenset([6,77,88,9])

print(f1 | f2)  #frozenset({6, 7, 8, 9, 77, 88})

print(f1 & f2)  #frozenset({9, 6})

f1 |= f2

print(f1)   #frozenset({6, 7, 8, 9, 77, 88})

'''
f1 = frozenset([6,7,8,9])
f2 = frozenset([6,77,88,9])

f1 = f2.update() #AttributeError: 'frozenset' object has no attribute 'update
'''