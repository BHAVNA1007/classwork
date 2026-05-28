#07_find_max_element
#using for
'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

for i in range(n):
   x = int(input('Element: '))
   arr.append(x)
print(arr)

max = arr[0]
for i in range(1,n):
   if arr[i] > max:
      max = arr[i]
print(max)

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

max = arr[0]
i = 1
while i < len(arr):
  if arr[i] > max:
      max = arr[i]
  i += 1   
print(max)




