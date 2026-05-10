'''
06_prime_fullyOptimize
'''
import math
n = int(input("Enter a number "))
if n <= 1:
    print("not prime")
else:
    x = 0
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            x = 1
            break
        i += 1
    if x == 0:
        print("prime")
    else:
        print("Not prime") 