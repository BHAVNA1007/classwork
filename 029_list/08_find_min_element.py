#08_find_min_element
#using for
'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

for i in range(n):
   x = int(input('Element: '))
   arr.append(x)
print(arr)

min = arr[0]
for i in range(1,n):
   if arr[i] < min:
      min = arr[i]
print(min)

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

min = arr[0]
i = 1
while i < len(arr):
  if arr[i] < min:
      min = arr[i]
  i += 1   
print(min)




