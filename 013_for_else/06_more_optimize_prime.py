'''
06_more_optimize_prime
'''


num = int(input("Enter the number = "))

if num <= 1:
   print("Not prime")

else:
    for i in range(2, num//2 + 1):
        if num % i == 0:
           print("Not prime")
           break

    else:
        print("prime")
        