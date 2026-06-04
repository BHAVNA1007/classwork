#04_Tuple_methods

t = (10, 10, 30, 40, 50)
print(t)

print('count',t.count(10))

print('index',t.index(40))

print('maximum',max(t))

print('minimum',min(t))

print('sum of all',sum(t))


# iteration tuple
for i in t:
   print(i)
print()


for i in range(len(t)):
    print(t[i])

#tuple concatination
t1 = (10,20,30,40,50)
t2 = (99,100)
print(t1+t2)