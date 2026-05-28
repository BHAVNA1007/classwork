#04_add_odd_index_ele
#for loop
'''
n = int(input("Enter size: "))
print("plz enter elements...")

arr = []
for i in range(n):
    x = int(input("element: "))
    arr.append(x)

print(arr)

sum = 0
for i in range(1,n,2):
    sum += arr[i]
print(sum)
'''

#while loop

n = int(input("Enter size: "))
print("plz enter elements...")

arr = []
i = 0
while i<n:
    x = int(input("element: "))
    arr.append(x)
    i += 1 
print(arr)

sum = 0
i = 1
while i < len(arr):
    sum += arr[i]
    i += 2 
print(sum)



