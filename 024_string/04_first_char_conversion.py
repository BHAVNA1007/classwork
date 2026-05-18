'''
04_first_char_conversion
'''
str = input('Enter the string: ')

result = ' '
i = 0

while i<len(str):
   if str[i]>="a" and str[i]<="z" :  
       if i==0 or str[i-1]==" " :
           upper = ord(str[i])-32
           result = result+chr(upper)
       else:
           result = result + str[i]

   else:
         result = result + str[i]  
 
   i += 1

print(result,end=' ')



str = input('Enter a string : ')
res = ' '
words = str.split()

for w in words:
    res = res + w.capitalize()+' '

print(res)



str = input('Enter the string: ')
res = str.title()
print(res)













 













