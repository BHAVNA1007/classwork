'''
02_skip_even_number
'''
'''
n = int(input("Enter a number = "))

for i in range(1,n+1):
    if i % 2 == 0:
        continue
    print(i)
'''
n = int(input("Enter a number = "))

i = 0
while i < n:
    i += 1
    if i % 2 == 0:
         continue
   
    print(i)
print("done with the loop")