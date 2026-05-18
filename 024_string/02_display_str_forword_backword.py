#02_display_str_forword_backword

str = input('Enter the string: ')

n = len(str)
print(n)
i = 0
while i< n:
   print() 
   print(i,str[i],end='')
   i += 1


i = n-1
while i> 0:
   print()
   print(str[i],end='')
   i -= 1


i = -1
while i>=-n:
   print()
   print(str[i],end='')
   i -= 1


print("another one")
for i in str:
   print(i)

print('arre ye last he')
for i in range(len(str)):
    print(str[i]) 

print("one more type")
for i in range(n-1,-1,-1):
    print(i,str[i]) 










 