#04_pattern
'''
1**********1
12********21
123******321
1234****4321
12345**54321
123456654321
'''
'''
n = int(input('Enter a number: '))
i = 1
while i<=n:
    print()
    inc = 1
    while inc<=i:
       print(inc,end='')
       inc += 1

    s = 1 
    while s <= (n-i)*2:
       print("*",end='')
       s += 1
  
    dec = i
    while dec >= 1:
       print(dec,end='') 
       dec -= 1 
    i += 1 
'''
'''
 *****
  ***
   *
'''
'''
n = int(input("Enter a number: "))
i = 1
while i<=n:
   print()
   inc = 1
   while inc<=i:
      print(" ",end='')  
      inc += 1
   s = 1
   while s<(n-i)*2:
      print("*",end='')
      s += 1
   dec = i
   while dec >= 1:
      print(" ",end='')
      dec -= 1
   i += 1  
'''
'''
     1
    21
   321
  4321    
'''
'''
n = int(input("Enter a number : "))
i = 1
while i<=n:
   print()
   space = 1
   while space <= n-i:
      print(' ',end=' ')
      space += 1
   j=1
   while j<=i:
     print(j,end=" ")
     j = j+1
   i += 1 
'''
'''
   A
  AB
 ABC
ABCD
'''
n = int(input("Enter a number : "))
i = 1
while i <= n:
   print()
   space = 1
   while space <= n-i:
      print(' ',end="")
      space += 1
   j = 1
   ch = 65
   while j <= i:
      print(chr(ch),end="")
      ch += 1
      j += 1
   i += 1 
   
 





        
       
        