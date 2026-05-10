#01_right_angle


'''
1
12
123
1234

n = int(input("Enter a number: "))

i = 1

while i<=n :
      print()
      j = 1
      while j<=i:
         print(j, end=" ")
         j += 1

      i += 1

'''
'''

*
**
***
****
*****

n = int(input("Enter a number: "))

i = 1

while i <= n:
    print()

    j = 1
    while j <= i:

       print("*", end='')
       j += 1

    i += 1
'''

*****
****
***
**
*

n = int(input("Enter a number: "))
i = 1

while i <= n:
    print()
    j = n
    while j>=i:
        print("*",end =" ")
        j -= 1

    i += 1
              
