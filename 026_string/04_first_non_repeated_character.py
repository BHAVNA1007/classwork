'''
04_first_non_repeated_character
'''

s = input('Enter the string: ')
i = 0
f = 0
while i < len(s):
   count = 0
   j = 0
   while j <len(s):
      if s[i] == s[j]:
         count = count + 1
      j = j+1
   if count == 1:
      print('first non rep',s[i])
      f = 1
      break
   i = i + 1

if f == 0:
   print('No Non rep found')  