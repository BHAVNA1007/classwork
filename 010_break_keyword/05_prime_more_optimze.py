'''
05_prime_more_optimze
'''
n = int(input("Enter a number = "))

if n <= 1:
   print(" Not  prime ")
else:
   x = 0
   i = 2
   while i <= n // 2:
       if n % i == 0:
          x = 1
          break
       i += 1 
   if x == 0:
       print("prime")
   else:
       print("Not prime")
    


