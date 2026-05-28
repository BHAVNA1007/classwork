#06_add_even_element
#using for
'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

for i in range(n):
   x = int(input('Element: '))
   arr.append(x)
print(arr)

sum = 0
for i in range(n):
   if arr[i] % 2 == 0:
      sum += arr[i]
print(sum)

'''
#using while

n = int(input('Enter the size of list: '))
print('Plz enter the elements...')

arr = []
i = 0
while i<n:
   x = int(input('Element: '))
   arr.append(x)
   i += 1
print(arr)

sum = 0
i = 0
while i < len(arr):
  if arr[i] % 2 == 0:
     sum += arr[i]
  i += 1   
print(sum)




   
    

   
    
