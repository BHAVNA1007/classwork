#03_pattern
'''
1
22
333
4444
55555
'''
'''
n = int(input("Enter a number:"))

i = 1

while i<=n:

    print()
    
    j = 1
    while j <= i:

        print(i, end=" ")

        j = j + 1  
    i = i + 1
'''

'''
1
**
123
****
12345
'''
'''
n = int(input("Enter a number: "))

i = 1

while i<= n:
    print()

    j = 1
    while j <= i: 
       if i % 2 ==0:
          print("*",end=' ')
       else:
          print(j,end=' ')

       j = j+1
    i = i+1

'''
'''
1 
1 *
1 * 3
1 * 3 *
1 * 3 * 5
'''
'''
n = int(input("Enter a number: "))

i = 1

while i<=n:
    print()
    j = 1
    while j<=i:
      if j % 2 == 0:
          print("*",end=" ")
      else:
          print(j, end=' ')
      j += 1
    i = i + 1    
'''
'''
1
23
345
6789
'''
n = int(input("Enter a number: "))
i = 1
k = 1
while i<=n:
    print()
    j = 1
    while j<=i:
       print(k,end=' ')
       
       j = j+1
       k += 1
    i = i+1









