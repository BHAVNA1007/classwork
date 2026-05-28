#10_second_largest
'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

i =0
while i <n:
   x = int(input('Element: '))
   arr.append(x)
   i += 1
print(arr)

unique = []
i = 0
while i < len(arr):
   if arr[i] not in unique:
      unique.append(arr[i])
   i += 1
print(unique)

arr = unique
arr.sort()
print(arr[-2])

'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

for i in range(n):
   x = int(input('Element: '))
   arr.append(x)
print(arr)

unique = []
for i in arr:
   if i not in unique:
      unique.append(i)
print(unique)

arr = unique
arr.sort()
print(arr[-2])




