#02_accesing_tuple_ele

t = (10, 20, 30)
print(t)

print(t[0])
print(t[-1])

print(t[1:3])

'''
#TypeError: 'tuple' object does not support item assignment
t = (10, 20, 30)
t[0] = 99
print(t)
'''

t = ([10,20],30)
print(id(t))           #2478274723264

t[0].append(4)
print(t)              #([10, 20, 4], 30)
print(id(t))   #2478274723264