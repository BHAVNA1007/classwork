#05_nested_tuple

t1 = ((10,20),(30,40))
print(t1)
print(t1[0])
print(t1[1])


#membership operator:

t = (10, 20, 30, 40)
print(20 in t)
print(50 not in t)


t1 = (1,2,8) #True
t2 = (1,2,4) #True
print(t1<t2) #False


#tuple deletion

t1 = (1,2,8)
del t1
print(t1)
#NameError: name 't1' is not defined. Did you mean: 't'?