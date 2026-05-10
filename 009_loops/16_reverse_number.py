#16_reverse_number 

"""
num = int(input("Enter a number = "))

rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print("revers of a number is ", rev) 
"""

# one more methode using string and for loop 

num = input("Enter a number = ")

rev = ""

for d in num:
   
   rev = d + rev
   
print("reverse number is ", rev)