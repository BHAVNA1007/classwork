#12_common_ele_bw_two_list

n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr1 = []

i =0
while i < n:
   x = int(input('Element: '))
   arr1.append(x)
   i += 1
print(arr1)

arr2 = []

i =0
while i < n:
   x = int(input('Element: '))
   arr2.append(x)
   i += 1
print(arr2)

common = []

i = 0
while i < len(arr1):
    if arr1[i] in arr2:
       common.append(arr1[i])   
    i += 1
print(common)


'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr1 = []

for i in range(n):
   x = int(input('Element: '))
   arr1.append(x)
   
print(arr1)

arr2 = []

for i in range(n):
   x = int(input('Element: '))
   arr2.append(x)
   
print(arr2)

common = []

for i in arr1:
    if i in arr2:
       common.append(i)   

print(common)
'''