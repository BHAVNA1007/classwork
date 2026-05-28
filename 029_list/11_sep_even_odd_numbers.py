#11_sep_even_odd_numbers

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

even = []
odd = []
i =0
while i < len(arr):
    if arr[i] % 2 == 0:
       even.append(arr[i])
    else:
       odd.append(arr[i])
    i += 1
print("Even: ",even)
print("odd: ",odd)
'''
n = int(input('Enter the size of list: '))

print('Plz enter the elements...')

arr = []

for i in range(n):
   x = int(input('Element: '))
   arr.append(x)
   
print(arr)

even = []
odd = []

for i in arr:
    if i % 2 == 0:
       even.append(i)
    else:
       odd.append(i)
   
print("Even: ",even)
print("odd: ",odd)

