#14_perfect_number  using while loop
'''
n = int(input("Enter a number = "))
sum = 0
i = 1
while i < n:
    if n % i == 0:
        sum = sum + i
    i = i+1
if n == sum:
    print(n, "is perfect")
else:
    print(n, "is not perfect")
'''

'''
#now jump into optimize solution for the perfect num
n = int(input("Enter a number = "))
sum = 0
i = 1
while i<n :
    if n%i == 0:
        sum += i
    i += 1
if sum == n:
    print("perfect")
else:
    print("not perfect")

'''


# using for loop 

'''
n = int(input("Enter a number = "))
sum = 0

for i in range(1, n):
     if n % i == 0:
         sum += i
if n == sum:
    print("perfect")
else:
    print("not perfect")

'''


#now tooo  optimize solution for the perfect num
n = int(input("Enter a number = "))
sum = 0

for i in range(1, n//2 +1):
     if n % i == 0:
         sum += i
if n == sum:
    print("perfect")
else:
    print("not perfect")






     
   

