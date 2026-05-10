'''
07_most_optimize

'''
import math
num = int(input("Enter the number = "))

if num <= 1:

   print("Not prime ")
else:
   for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
   else:
       print("Prime")  
