#12_factorial 

'''
n = int(input("Enter a number = "))

fact = 1
for i in range(1, n+1):
    fact = fact *i
print("factorial is = ", fact)
'''

'''
n = int(input("Enter a number = "))

fact = 1

for i in range(n, 0, -1):
     fact = fact * i
print("Factorial of a number is =",fact)
'''

import math

n = int(input("Enter a number = "))

print("factorial is ", math.factorial(n))

