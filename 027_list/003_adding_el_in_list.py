#003_adding_el_in_list
#append()

'''
l = [10,20,30,40,50]
l.append(60)
print(l)

l = []
for i in range(1, 101):
   if i%2 == 0:
      l.append(i)
print(l)

l2 = []
for i in range(2,101,2):
    l2.append(i)
print(l2)
'''

'''
#insert()

l =[10,20,30]
l.insert(1,99)
print(l)

a =[10,20,30]
a.insert(-10,9999)
a.insert(10,7777)

print(a.index(9999))
print(a.index(7777))
print(a)


l = [10,20,30]
l.insert(len(l),99)
print(l)
'''

'''
#extend()

a = [10, 20, 30]
a.extend([40,50,60])
print(a)

b =[40,50]
a.extend(b)
print(a)


#diff b/w append() & extend()

a=[10,20,30]
a.append([40,50])
print(a)

a.extend([40,50])
print(a)

a = [10,20,30]
a.append("hello")
print(a)
a.extend("hello")
print(a)

'''













