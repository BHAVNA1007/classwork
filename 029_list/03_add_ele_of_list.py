#03_add_ele_of_list
'''
# for loop
n = int(input("Enter size of list: "))

arr = []
print('Plz enter elements...') 
for i in range(n):
   x = int(input("element: "))
   arr.append(x)
print(arr)

sum = 0
for i in arr:
   sum += i
print(sum)
'''

'''
#while loop
n = int(input("Enter size of list: "))

arr = []
print('Plz enter elements...') 
i = 0
while i< n:
   x = int(input("element: "))
   arr.append(x)
   i += 1
print(arr)

sum = 0
i = 0
while i<len(arr):
   sum += arr[i]
   i += 1
print(sum)
'''

#using sum() method
n = int(input("Enter size of list: "))

arr = []
print('Plz enter elements...') 
i = 0
while i< n:
   x = int(input("element: "))
   arr.append(x)
   i += 1
print(arr)

total = sum(arr)
print(total)






   
  
   

