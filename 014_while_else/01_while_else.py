'''
01_while_else

'''

attempts = 0

while attempts < 3:
     password = input('Enter the password = ')
     if password == 'admin':
         print('access granted')
         break
     attempts += 1

else:

     print("Too many faild attepts") 