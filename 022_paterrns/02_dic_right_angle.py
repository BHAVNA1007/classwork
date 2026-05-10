#02_dic_right_angle

'''
54321
4321
321
21
1
'''
'''
n = int(input("Enter a number: "))

i = n

while i >= 1:
     
     print()
     
     j = i
     while j >= 1:

        print(j, end=' ')
        j -= 1

     i -= 1
'''

'''
1234
234
34
4
'''
n = int(input("Enter a number: "))

i = 1

while i <= n:

    print()
    j = i
    while j <= n:
       print(j, end="")

       j += 1
    i += 1