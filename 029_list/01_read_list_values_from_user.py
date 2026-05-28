'''
#01_read_list_values_from_user

a=list(map(int,input('Enter numbers: ').split()))
print(a)

a=list(map(int,input('Enter numbers: ').split(",")))
print(a)
'''

n = int(input('Enter the number of element: '))
marks = []
print('plz enter all elements... ')

for i in range(n):
   x = int(input('Enter num: '))
   marks.append(x)
print(marks)

