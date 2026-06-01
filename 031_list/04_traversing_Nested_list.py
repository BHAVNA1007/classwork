#04_traversing_Nested_list

a  = [
       [10,20,30],
       [40,50,60],
       [70,80,90]  
     ]

print(a[0])
print(a[1])
print(a[2])
print()


for r in a:
   print(r)


a  = [
       [10,20,30],
       [40,50,60],
       [70,80,90]  
     ]

for i in a:
   for j in i:
       print(j)


a  = [
       [10,20,30],
       [40,50,60],
       [70,80,90]  
     ]

for i in a:
   for j in i:
       print(j,end=' ')
   print()






