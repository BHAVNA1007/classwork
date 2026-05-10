#04_prime_number
'''
x = int(input("Enter first number = "))
y = int(input("Enter second number = "))

while x <= y:
    n = x
    flag = True
    

    if n > 1:
       i = 2
       
       while i < n:
           if n % i == 0:
               flag = False
               break
           i += 1
       if flag == True:
           print(n)
       x += 1  
'''

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))

while x <= y:
    n = x
    if n > 1:
        i = 2
        while i < n:
           if n % i == 0:
              break
           i += 1
        else:
            print(n)
    x += 1
